from test_data import get_news_data, get_news_datalists, get_news_delete, get_news_collect, get_news_talk
from demo import get_datalists
class Test_fuix:

    # 调用获得token的接口，确保后续接口能正常调用
    def test_token(self, get_token):
        pass

    # 测试新闻列表的接口请求
    def test_news_datalists(self, get_news_datalists):
        print(get_news_datalists)

    #测试新闻内容的接口请求
    def test_news_data(self, get_news_data):
        print(get_news_data)

    # 测试收藏新闻内容
    def test_news_collect(self, get_news_collect):
        print(get_news_collect)

    # 测试评论新闻内容
    def test_news_talk(self, get_news_talk):
        print(get_news_talk)

    # 测试新闻评论删除
    def test_news_delete(self, get_news_delete):
        # assert get_news_delete["status_code"] ==200
        print(get_news_delete)
# if __name__ == '__main__':
#     Test_fuix().get_login_fixture()
#
#
# def test_newslists(get_datalists):
#     print(get_datalists)
