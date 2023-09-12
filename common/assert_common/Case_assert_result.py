from common.assert_common.Assert_util import Assert

"""断言判断"""


class Assert_judge:
    @classmethod
    def assert_judge(cls, case_data, api_response):
        if "assert_expression" in case_data:
            assert_r = Assert.assert_resonse(api_response, case_data["assert_expression"])
            return assert_r
        else:
            pass
