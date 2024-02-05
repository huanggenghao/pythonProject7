# -*- coding: utf-8 -*-            
# @Author : ben
# @Time : 2024/2/4 10:12

import yaml

# with open('yanl.yaml','r',encoding='utf-8') as f:
#     data = yaml.safe_load(f)
#     # print(type(data))
def read_yaml(self):
    with open(self.filename, encoding='utf-8') as fs:
            # 避免报警告：yaml.FullLoader
        data = yaml.load(fs, Loader=yaml.FullLoader)
        return data
# 访问列表里面嵌套字典的数据
# print(data[0]['persion1']['name'])
# 访问列表里面嵌套字典的数据
# print(data['persion1']['name'])

filename = 'yanl.yaml'

print(read_yaml(filename))

