import codecs
import logging
import os
import pickle
from typing import Optional


class ParameterPool():
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.parameters = self._load_pool()  # 参数池，保存接口返回参数提取的值，提供给需要的接口请求参数使用
        self.namespace = {}  # 自定义参数池
        self.default_namespace = 'default'  # 默认参数池

    def get(self, key: str, namespace: str = None):
        if not namespace:
            namespace = self.default_namespace
        logging.info(f"从{namespace}得到key的值为{key}")
        if namespace in self.parameters:
            return self.parameters[namespace].get(key)
        raise KeyError(f"{key} 不在{namespace}参数池中")

    def put(self, params: dict, namespace: str = None) -> int:  # namespace工作空间。传值时会分配到自己命名的工作空间，若没有指定，则分配默认空间
        # new_parameters =self._load_pool()
        if self.default_namespace not in self.parameters:
            self.parameters[self.default_namespace] = {}
            logging.info("default工作台不存在，进行初始化为{}")
        # print(f"总参数池：{new_parameters}")
        logging.info("正在写入参数")
        if not isinstance(params, dict):  # 判断传入参数类型
            raise TypeError("params参数必须是字典类型")
        if not namespace:  # 没有namespace参数，默认参数池
            namespace = self.default_namespace  # 放入默认空间
            # print(f"没有参数nomespace{new_parameters[namespace]}")
            # ParameterPool._save_pool()
        elif namespace not in self.parameters:
            self.parameters[namespace] = {}
            # print(f"参数nomespace为新的{new_parameters[namespace]}")
        for k, v in params.items():
            self.parameters[namespace][k] = v
            # print(new_parameters[namespace][k])
            logging.debug(f"保存 {k}={v} 到{namespace}工作池中")
        self._save_pool(self.parameters)
        return len(params)

    def put_all(self, namespace=None, **kwargs):  # 存放方法，可以键值对传参
        self.put(kwargs, namespace)  # 直接用kwargs参数调用put方法

    def clear(self, namespace=None):  # 清理工作空间
        new_parameters = self._load_pool()
        if not namespace:
            pickle.dump({}, open(self.filepath, 'wb'))
            logging.info("参数池已全部清空")
            print("参数池已全部清空")
        else:
            new_parameters.pop(namespace, None)  # 不指定命名空间时,用空字典直接覆盖实现全清空。
            pickle.dump(new_parameters, open(self.filepath, 'wb'))
            logging.info(f"{namespace}的参数池已清空")
            print(f"{namespace}的参数池已清空")

    def print(self, namespace=None):
        new_parameters = self._load_pool()
        if namespace:
            # 打印指定命名空间
            if namespace in new_parameters:
                for key, value in new_parameters[namespace].items():
                    print(f"{namespace}参数池({key}:{value})")
                    logging.debug(f"{namespace}参数池{key} = {value}")
            else:
                logging.debug(f"{namespace}参数池不存在")
        else:
            print(self._load_pool())

    def _save_pool(self, new_params):
        with open(self.filepath, "rb") as f:
            if os.path.getsize(self.filepath) == 0:
                logging.warning("调用_save_pool时，参数文件为空, 默认返回{}")
                existing_params = {}
            else:
                existing_params = pickle.load(f)
            existing_params.update(new_params)
        # 保存到临时文件
        tempfilepath = os.path.join(os.getcwd(), "params_pool_temp.ini")
        with open(tempfilepath, "wb") as tempf:
            pickle.dump(existing_params, tempf)
        # 切换临时文件与原文件
        os.replace(tempfilepath, self.filepath)

    def _load_pool(self):
        # try:
        with open(self.filepath, "rb") as f:
            if os.path.getsize(self.filepath) == 0:
                # 文件空,返回默认空字典
                logging.warning("调用_load_pool时，参数文件为空, 默认返回{}")
                self.parameters = {}
            else:
                self.parameters = pickle.load(f)
        return self.parameters
        # except FileNotFoundError:
        #     return {}


"""作为全局实例初始化
param_pool = ParameterPool()

使用示例
param_pool.put("token", "abcd1234")
token = param_pool.get("token")"""
# if __name__ == '__main__':
#     current_dir = os.path.dirname(__file__)
#     file_path = os.path.join(current_dir, "params_pool.ini")
#     pool = ParameterPool(file_path)
#     # pool.clear()
#     pool.print()
# pool.get('token','test2')
#
#     pool.print()
