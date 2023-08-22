import ast

from jsonpath import jsonpath


class Assert:
    @classmethod
    def assert_resonse(cls, api_response: dict, assert_list: list):
        new_assert_list = []
        """
        :param api_response: 接口返回值 {'ig':'theshy','code':'200'}
        :param assert_list:yaml里的接口列表
        :return:
        """
        print(f"初始的断言列表{assert_list}")
        for i in assert_list:
            if '$.' in i:
                wz = i.find('$')  # 找到$的位置
                assert_json_path = i[wz:len(i)]  # 获取[$,最后一个数) 注意括号
                # print(f"找到$.的位置{assert_json_path}")cod
                value = jsonpath(api_response, assert_json_path)  # 在api请求里找到这个$.?的值
                # print(f"键的值{value}")
                if not value:
                    # print('表达式提取失败，请检查！')
                    return False
                value = value[0]  # value只有一个值，取出来
                # 用值把表达式替换掉(注意这个需要用变量接住这个替换的新值)
                a = type(value)
                if isinstance(value, int) or isinstance(value, float):  # replace只支持str,因此得做校验
                    value = str(value)
                i = i.replace(assert_json_path, value)  # $.ig 换为value
            new_assert_list.append(i)
        print(f"计划的断言列表{new_assert_list}")

        assert_result_list = []
        status_code = api_response["status_code"]  # 赋值变量，不然eval没法比较
        code = api_response["body"]["code"]
        for i in new_assert_list:
            print(i)
            assert_result = eval(i)  # 在eval里进行比较，返回True,False
            assert_result_list.append(assert_result)
        print(f"最终的断言列表{assert_result_list}")
        if False in assert_result_list:
            return False
        return True
# if __name__ == '__main__':
#     api_response = {'status_code': 200, 'body': {'code': 10000, 'data': {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxODI4OTQ1NDg0NiIsInZlcl9jb2RlIjoi8J6JgCIsImV4cCI6MTY5MjU4ODE1NCwiaXNzIjoicHJvOTExIn0.PZfF7FoCXojjd4nRQZEAuFZWhFj1HpLmvPntGCFW8mc'}, 'msg': 'success'}}
#     # assert_list = ["'12' in '123'", "'ig' == '$.ig'",'2 == 1']
#     # api_response = {'msg': '请求正常','ig': 'theshy'}
#
#     assert_list = ['status_code == $.status_code', 'code == $.body.code']
#     Assert.assert_resonse(api_response,assert_list)
