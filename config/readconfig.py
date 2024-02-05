# -*- coding: utf-8 -*-            
# @Author : ben
# @Time : 2024/2/4 16:17
import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

conf = configparser.ConfigParser()
conf.read(configPath,encoding="utf-8")



# host = conf.get("DATABASE", "host")
# username = conf.get("DATABASE", "username")
# password = conf.get("DATABASE", "password")
# port = conf.get("DATABASE", "port")
# database = conf.get("DATABASE", "database")
#
# print(host,username,password,port,database)