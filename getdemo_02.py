import requests

from config.Conf import ConfigYaml, Configdata


class datab:
    def __init__(self):
        # self.log = my_log("datab")
        self.config_url = ConfigYaml()
        self.config_token = Configdata()

    # @pytest.fixture() #新闻列表接口
    # def get_url(self):
    #     return self.config_url.get_conf_url() + '/news_list?mobile=18289454846&theme_news=国际新闻&page=1&pageSize=20'
    #
    # def get_data(self):
    #     token = self.config_token.get_conf_token()['token']
    #     headers1 = {
    #         'Content-Type': 'application/json',
    #         'token': token
    #     }
    #     self.log.debug("ads")
    #     res = requests.get(url=self.get_url(), headers=headers1)
    #     return res.json()
    #
    # def news_data(self):  # 新闻详情接口
    #     url = self.config_url.get_conf_url() + "/news_details?id=20&status=1"
    #     token = self.config_token.get_conf_token()['token']
    #     headers2 = {
    #         'Content-Type': 'application/json',
    #         'token': token
    #     }
    #     res = requests.get(url=url, headers=headers2)
    #     return res.json()
    #
    # def news_collect(self):  # 新闻收藏接口
    #     url = self.config_url.get_conf_url() + "/collect_news"
    #     token = self.config_token.get_conf_token()['token']
    #     headers = {
    #         'token': token
    #     }
    #     res = requests.post(url=url, headers=headers)
    #     return res.json()

    def news_talk(self):  # 评论新闻接口
        url = "https://demo-api.apipost.cn/api/demo/news_comment?id=20&content=这篇文章写很棒!!"
        token = self.config_token.get_conf_token()['token']
        headers = {
            'token': self.config_token.get_conf_token()['token']
        }
        data = self.config_url.get_conf_data()
        # params = json.dumps(payload)
        res = requests.post(url=url, data=data, headers=headers)
        return res.json()

    # def news_delete(self):  # 新闻评论删除接口
    #     url = self.config_url.get_conf_url() + "/delete_comment"
    #     token = self.config_token.get_conf_token()['token']
    #     headers = {
    #         'token': token
    #     }
    #     payload = {
    #         "id": 20,
    #         "comment_id": 98
    #     }
    #     parmas = json.dumps(payload)
    #     res = requests.delete(url=url, data=parmas, headers=headers)
    #     return res.json()


if __name__ == '__main__':
    db = datab()
    print(db.news_talk())
