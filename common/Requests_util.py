# 重构
# 创建类
import requests


class Request:
    # 定义公共方法
    def requests_api(methon, url, data=None, json=None, headers=None):
        if methon == "get":
            # get请求
            r = requests.get(url, data=None, json=json, headers=headers)
        elif methon == "post":
            r = requests.post(url, data=None, json=json, headers=headers)
        # 2.获取结果内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 内容存到字典里
        res = dict()
        res["code"] = code
        res["body"] = body
        # 字典返回
        return res

    # 3、重构get/post方法
    # get
    # 1.定义方法
    def get(self, url, **kwargs):
        # 2.定义参数
        # url,headers,json,cookies,method
        # 3.调用公共方法
        return self.requests_api(url, methon="get", **kwargs)

    # post
    # 1.定义方法
    def post(self, url, **kwargs):
        # 2.定义参数
        # url,headers,json,cookies,method
        # 3.调用公共方法
        return self.requests_api(url, methon="post", **kwargs)
