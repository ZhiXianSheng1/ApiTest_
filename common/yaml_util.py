import os
import yaml
#读取
def read_yaml(key):
    with open(os.getcwd()+'/data.yaml',mode='r',encoding='utf-8') as f:
        value = yaml.safe_load(f)
        return value[key]
#写入
def write_yaml(data):
    with open(os.getcwd()+'/data.yaml',mode='a',encoding='utf-8') as f:
        value=yaml.dump(data=data,stream=f,allow_unicode=True)
#清除
def clean_yaml(data={}):
    with open(os.getcwd()+'/data.yaml',mode='w',encoding='utf-8') as f:
        f.truncate()