#
#
# def test_login(get_login_fixture):
#     status_code = get_login_fixture
#     assert status_code == 200


# class TestClass:
#
#   def test_login(self,get_login_fixture):
#     assert get_login_fixture.status_code == 200
#     print(get_login_fixture.json())
# def teardown(self):
#   print("没有随机数哦".center(34,"*"))

# def setup_class(self):
#   print("每个类之前的操作")
#
# def teardown_class(self):
#   print("每个类之后的操作")

import pytest

user = [('张三', '123456'), ('李四', 'abcdefg')]


class TestA:
  @pytest.mark.parametrize(argnames='login', argvalues=user, indirect=True)
  def test_one_param(self, login):
    assert True
