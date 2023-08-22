import jinja2
# 实现接口参数依赖和参数提取的方法
from jsonpath import jsonpath

from common import ParameterPool
from conftest import param_pool


class ParameterSetting:

    # 参数池，保存接口返回参数提取的值，提供给需要的接口请求参数使用
    @classmethod
    def getParams_value(cls, param: str):
        param_pool.get(param)

    def put_params(cls, param: dict):
        param_pool.put_all(param)

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
    def parameter_setting(cls, data: dict, type='get') -> dict:
        """
        :param data: 返回结果提取和参数依赖使用dict，例：{'bill': '$.bill'}
        :param type: save :把数据存到参数池里面无返回，get读取参数池数据并返回新值
        :return:
        """
        # {'b': '$.b','g': '$.g' } 提取格式键+提取表达式
        # for k,v in data.items():
        #     if '$.' in v:
        #         try:
        #             v = jsonpath(param_pool.parameters,v)[0] #eg:v=[333]
        #             data[k] =v
        #         except Exception:
        #             print(f'jsonpath未读取到值，请重新检查')
        #     print(f'最终返回参数{data}')
        if type == 'get':
            for k, v in data.items():  # 1.使用param_pool的get、put方法，避免直接使用参数池,2.尽量不改变入参
                new_data = {}
                if '$.' in v:
                    try:
                        v = param_pool.get(k, 'tesecase_pool')
                    except KeyError:
                        print(f'{k} not exist in pool')
                        new_data[k] = v
                return new_data
        elif type == 'save':
            for k, v in data.items():
                param_pool.put_all(k, v, 'testcase_pool')

    @classmethod
    def extract_value(cls, api_response: dict, extract_key: dict) -> dict:
        """
        :param api_response: 返回通过表达式提取出接口的最终要存的值
        :param extract_key:{'billCOmmonNo': '$.content.billCommonNo'} 提取参数字典
        :return:
        """
        extract_value = {}
        for k, v in extract_key.items():
            try:
                extract_value[k] = jsonpath(api_response, v)[0]
            except TypeError:
                pass
        return extract_value


# if __name__ == '__main__':
#     extract_key={'token': '$.body.data.token'}
#     api_response={'status_code': 200, 'body': {'code': 10000, 'data': {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxODI4OTQ1NDg0NiIsInZlcl9jb2RlIjoi8J6JgCIsImV4cCI6MTY5MjU4NTg3MywiaXNzIjoicHJvOTExIn0.2PRsMj058xcDljH2Emsw6VEdCaqBXyVlJDz6eUJqvtU'}, 'msg': 'success'}}
#     a=ParameterSetting.extract_value(api_response,extract_key)
#     print(a)
if __name__ == '__main__':
    # param_pool.put_all(key='aaa',value='2',aa='3',namespace='key_pool')
    # param_pool.put_all(key='aaa', value='2', aa='3', namespace='key_pool1')
    # param_pool.put_all(key='aaa', value='2', aa='3', namespace='key_pool2')
    # print(param_pool.get('key_pool1'))
    # param_pool.clear('key_pool1')
    print(param_pool.parameters)
