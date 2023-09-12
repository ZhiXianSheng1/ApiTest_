# 重构
# 创建类
import jwt
import requests
class Request:
    # 定义公共方法
    def requests_api(url, method, data=None, json=None, headers=None):
        if method == "get":
            # get请求
            r = requests.get(url, data=data, json=json, headers=headers)
        elif method == "post":
            r = requests.post(url, data=data, json=json, headers=headers)
        elif method == "delete":
            r = requests.delete(url, data=data, json=json, headers=headers)
        # 2.获取结果内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
            # 内容存到字典里
        res = dict()
        res["status_code"] = code
        res["body"] = body
        # res[]
        # 字典返回
        return res

    # 3、重构get/post方法
    # get
    # 1.定义方法# 2.定义参数:url,headers,json,cookies,method 3.调用公共方法
    @classmethod
    def get(cls, url, **kwargs):
        return cls.requests_api(url=url, method="get", **kwargs)

    # post
    # 1.定义方法# 2.定义参数:url,headers,json,cookies,method 3.调用公共方法
    @classmethod
    def post(cls, url, **kwargs):
        return cls.requests_api(url=url, method="post", **kwargs)

    # delete
    # 1.定义方法# 2.定义参数:url,headers,json,cookies,method 3.调用公共方法
    @classmethod
    def delete(cls, url, **kwargs):
        return cls.requests_api(url=url, method="delete", **kwargs)


if __name__ == '__main__':
    data = {
        'mobile': '18289454846',
        'ver_code': '123456'
    }
    re = Request.post(url='https://demo-api.apipost.cn/api/demo/login', data=data)
    print(re)
"""
class Requests:
    @classmethod
    def get(cls,path):
        url=
        headers =
        print(f"url信息{url},headers信息{headers}")
        return request.get(url=url,headers=headers).json
        
    @classmethod
    def post(cls,path,data):
        url=
        headers =
        print(f"url信息{url},headers信息{headers},data信息{data}")
        return request.post(url=url,headers=headers, data=json.dump(data)).json    
    

"""
