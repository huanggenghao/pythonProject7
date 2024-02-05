# -*- coding: utf-8 -*-            
# @Author : ben
# @Time : 2024/1/19 15:43
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('www.sina.com.cn',80))

print(s)
