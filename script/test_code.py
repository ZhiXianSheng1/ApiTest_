class Test_fuix:
    """
    调用获得token的接口，确保后续接口能正常调用
    """

    def test_token(self, get_token):
        pass

    """
    获取新闻列表的接口请求
    """

    def test_news_datalists(self, get_news_datalists):
        print(get_news_datalists)

    """
        获取新闻内容的接口请求
    """

    def test_news_data(self, get_news_data):
        print(get_news_data)

    """
       获取新闻内容的接口请求
    """

    def get_news_collect(self, get_news_collect):
        print(get_news_collect)

    """
        获取新闻内容的接口请求
    """

    def test_news_talk(self, get_news_talk):
        print(get_news_talk)

# if __name__ == '__main__':
#     Test_fuix().get_login_fixture()

'''
request 是 pytest的内置fixture
'''
