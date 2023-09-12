from common.log_common.log_util import Logger
# 实现接口参数依赖和参数提取的方法
from jsonpath import jsonpath
from conftest import param_pool
class ParameterSetting:
    """
    yaml里的$.token读出来就相当于{"access_token": $.token}
    """
    @classmethod
    def data_is_replace(cls, data):  # data是指yaml里request里的data模块
        """
        :param data:请求参数data和提取extract_key
        :return:返回参数是否需要被替换
        """
        if data is None:
            return False
        for k, v in data.items():
            if isinstance(v, (int, float)):  # 先判断一下data数据类型
                continue
            if '$.' in v:
                return True
        return False

    @classmethod
    def parameter_setting(cls, params: dict, type='get') -> dict:
        """
        :param data: 返回结果提取和参数依赖使用dict，例：{'bill': '$.bill'}
        :param type: save :把数据存到参数池里面无返回，get读取参数池数据并返回新值
        :return:
        """
        if type == 'get':
            for k, v in params.items():  # 1.使用param_pool的get、put方法，避免直接使用参数池,2.尽量不改变入参
                new_data = {}
                if '$.' in v:
                    try:
                        v = param_pool.get(k, 'tesecase_pool')
                        Logger.my_log().info(f"获取命名工作空间为'tesecase_pool'{k}的{v}")
                    except KeyError:
                        print(f'{k} 不在参数池里')
                        Logger.my_log(log_level='WARNING').warning(f'{k} 不在参数池里')
                    new_data[k] = v
                return new_data
        elif type == 'save':
            # for a, v in data.items():   #'status_co1de': 200 若key,value str带引号，可选用put,没带就put_all
            param_pool.put(params, namespace='testcase_pool')
            Logger.my_log().info(f"{params}存于testcase_pool工作空间成功！")

    @classmethod
    def extract_value(cls, api_response=None, case_data=None, extract_response: dict = None,
                      extract_request: dict = None) -> dict:
        """
                :param api_response: 返回通过表达式提取出接口的最终要存的值
                :param extract_key:{'billCOmmonNo': '$.content.billCommonNo'} 提取参数字典
                :return:
                """

        extract_value = {}
        # if not isinstance(extract_from_response, dict):  # 判断传入参数类型
        #     raise TypeError("extract_key参数必须是字典类型")
        #     logging.debug(f"{extract_key}参数必须是字典类型")
        try:
            if extract_response != None:
                Logger.my_log().info(f"extract_response的值为：{extract_response}")
                for k, v in extract_response.items():
                    # data_extract=jsonpath(api_response,v)[0]
                    # print(data_extract)
                    extract_value[k] = jsonpath(api_response, v)[0]
                    # print()
            elif extract_request != None:
                Logger.my_log().info(f"extract_response的值为：{extract_request}")
                for k, v in extract_request.items():
                    extract_value[k] = jsonpath(case_data, v)[0]
        except TypeError:
            raise print("类型异常，请检查！")
        Logger.my_log().info(f'新增参数值为：{extract_value}')
        return extract_value

# if __name__ == '__main__':
#     param_pool.clear()
#     print(param_pool.parameters)
