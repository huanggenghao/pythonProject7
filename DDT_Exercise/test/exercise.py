# -*- coding: utf-8 -*-            
# @Author : ben
# @Time : 2024/1/4 10:14
# import unittest
# from ddt import ddt, data, unpack
# import sys
#1.如何显示字符串反转
# import os

# import logging
# import os.path
# import time

# str = 'abcdef'
#
# str1 = str[::-1]
#
# print(str1)
#2.如何实现把英语字符转化大小写
# str2 = 'aBCd'
#
# str3 = []
#
# for i in str2:
#     str = i.lower()
#     str3.append(str)
# print(str3)

# 3.打印出100-900中的水仙花数

# number = []
#
# for i in  range(100,999):
#     # print(i)
#     if i == ((i//100)**3)+(((i%100)//10)**3)+(((i%100)%10)**3):
#         print(i)
#         number.append(i)
# print(number)

# a = 153
#
# b = a//100
#
# c = (a%100)//10
#
# d = ((a%100)%10)**3
#
# print(b,c,d)

# 4.如何实现取一组数中，倒数第二小的数，不可以使用内置函数

# number = [1,3,9,4,2]
#
# for i in range(1,len(number)):
#     for j in range(0,len(number)-i):
#         if number[j]>number[j+1]:
#             number[j],number[j+1]=number[j+1],number[j]
# print(number)
# print(number[1])
# 5.对字符串可以直接取值
# a = '123'
#
# print(a[0])
# print(a[1])
# print(a[2])

# 6.不定长函数**用法
# # 如何去掉字典里面的括号
# def hanshu(**one):
#     print("我是一个学习者,我叫："+str(one).replace("{","").replace("}",""))
#
# hanshu(one='happy',one1='ben')


# case_data = ['xiaoming','xiaohong','xiaohuang']
# @ddt
# class TestDemo(unittest.TestCase):
#     @data(*case_data)  # 在测试函数上使用@data(*case_data)进行数据解压，然后每一个元素传入测试函数
#     def test_case(self,name):
#         print(str(name)+"：欢迎你加入我们的团队")
# 获取列表的值
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# class Student(object):
#
#     def get_score(self):
#          return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# def bubble_sort(arr):
#     n = len(arr)
#
#     # 遍历数组，执行n-1轮冒泡
#     for i in range(1,n):
#         # 在每一轮中比较相邻元素并交换位置
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     return arr
#
# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = bubble_sort(arr)
# print(sorted_arr)



# 如何取字典里面嵌套字典
# a={
#    "student1": {
#        "name": "小明",
#        "age": 12
#    },
#    "student2": {
#        "name": "小张",
#        "age": 20
#    }
# }
# print(a['student1']['name'])




# 如何取字典里面嵌套列表，列表里面嵌套字典
# a ={
#   "users": [
#     {
#       "id": 1,
#       "name": "John",
#       "age": 25
#     },
#     {
#       "id": 2,
#       "name": "Alice",
#       "age": 30
#     },
#     {
#       "id": 3,
#       "name": "Bob",
#       "age": 35
#     }
#   ]
# }
# print(a["users"][1]['id'])

# print(sys.path)

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score >= 80 and self.score <= 100 :
#             return 'A'
#         elif self.score >= 60 and self.score < 80 :
#             return 'B'
#         elif self.score >= 0 and self.score < 60 :
#             return 'C'
#         elif self.score >= 101 or self.score <=-1 :
#             raise ValueError
#
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
# if __name__ == '__main__':
#     unittest.main()
# 文件的io
# file_path = os.path.abspath(os.path.dirname(__name__))
#
# file_name ='network.txt'
#
# file_path1 = os.path.join(file_path,file_name)

# print(file_path1)

# with open(file_path1,'r',encoding='utf-8') as f:
#     information = f.readlines()
#
# for i in information:
#     print(i)


# 如何写文件到日志

# logging.basicConfig(level=logging.DEBUG)
#
#
# # 写法有误
# file_path = os.path.abspath(os.path.dirname(__name__))
# file_path1 = os.path.join(file_path, 'log')

# print(file_path1)

# 对文件进行判空操作
# if os.path.exists(file_path1):
#     pass
# else:
#     os.mkdir(file_path1)

# # log_path是存放日志的路径
# cur_path = os.path.dirname(os.path.realpath(__file__))
# log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# # 如果不存在这个logs文件夹，就自动创建一个
# if not os.path.exists(log_path):
#     os.mkdir(log_path)



# logname = os.path.join(file_path1,'%s.log' %time.strftime('%Y_%m_%d_%H_%M_%S'))
#
# # 创建日志处理器，并将日志记录到文件中
# handle = logging.FileHandler(logname,'a',encoding='utf-8')
#
# # 设置日志处理器的日志级别为DEBUG
# handle.setLevel(logging.DEBUG)
#
# # 定义日志格式
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#
# handle.setFormatter(formatter)
#
# logging.getLogger(' ').addHandler(handle)
#
# logging.debug('写入数据')
#
# handle.close()
#  正则表达式

# def match(pattern, string, flags=0):
#     """Try to apply the pattern at the start of the string, returning
#     a Match object, or None if no match was found."""
#     return _compile(pattern, flags).match(string)

# 这段代码是一个函数定义，它使用正则表达式的模式（pattern）来尝试匹配字符串（string），并返回一个Match对象，如果没有找到匹配则返回None。
#
# 函数的参数包括pattern（正则表达式模式）、string（要匹配的字符串）和flags（可选的标志参数，用于指定匹配的方式）。函数内部通过调用_compile函数来编译正则表达式模式，并使用match方法来尝试匹配字符串。如果找到匹配，则返回一个Match对象；如果未找到匹配，则返回None。
#
# 这段代码的目的是：封装了正则表达式模式的匹配过程，使其更易于使用。它提供了一种简单的方式来尝试匹配字符串，并返回匹配结果。

# re模块中match(pattern,string[,flags]),检查string的开头是否与pattern匹配。

# re模块中research(pattern,string[,flags]),在string搜索pattern的第一个匹配值
# import re
#
# if re.match(r'\d{3}\-\s+\d{3,8}','1110- 11111'):
#     print("匹配成功")
# else:
#     print('匹配失败')
#
# if re.search(r'\d{3}\-\s+\d{3,8}','1110- 111'):
#     print("匹配成功")
# else:
#     print('匹配失败')

#获取当前的时间
# import datetime
#
# # now = datetime.datetime.now()
#
# #把str转换为datetime
#
# now = datetime.datetime.strptime('2024-01-15 10:36:01','%Y-%m-%d %H:%M:%S')
#
# print(now)

# from collections import Counter
# def count():
#     c = Counter()
#     for ch in 'programming':
#       c[ch] = c[ch]+1
#     return c
#
#
#
# print(count())
#对文件的操作
# import os
# #nt代表window
# print(os.name)

#拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数

# c ='/user/bat/username.txt'
#
# print(os.path.split(c))

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
#
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 程序运行的过程中，所有的变量都是在内存中
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# import pickle
# d = dict(name='Bob', age=20, score=88)
# print(type(d))
# print(type(pickle.dumps(d)))
# import json
#
# d=['a','b',{'name':'ben','age':'28'}]
#
# print(json.dumps(d))

# 如何启动一个子进程并结束
# from multiprocessing import Process
# import os
# def childprocess():
#     print("run children id is "+str(os.getpid()))
#
# if __name__=='__main__':
#
#     print('parent process is '+str(os.getpid()))
#     p = Process(target=childprocess)
#     print('children process will start')
#     p.start()
#     p.join()
#     print('children ending')
# %s是格式化字符串中的占位符，表示要插入一个字符串
# import os
# print(os.path)
# print('原来是这个用法 %s' %os.path)

# import time,threading
#
#
#
# def loop():
#     print("thread %s is running" % threading.current_thread().name)
#     n = 0
#
#     while n < 5:
#         n = n + 1
#         print("thread %s >>> %s" % (threading.current_thread().name, n))
#
#     print("thread %s is ending" % threading.current_thread().name)
#
# print("thread %s is running" % threading.current_thread().name)
#
# t = threading.Thread(target=loop,name='loopthread')
#
# t.start()
#
# t.join()
#
# print("thread %s is ending"%threading.current_thread().name)
# import copy
#
#
# a = [10, 20, [5, 6]]
# b = copy.copy(a)
# print("a", a)
# print("b", b)
# b.append(30)
# print(a)
# print(b)
# b[2][0] = 1
# print(b[2][0])
# print(a)
# print(b)
# b[2].append(7)
# print("浅拷贝......")
# print("a", a)
# print("b", b)
# s = 'hello world'
# dict = {}
# for i in s:
#     if i in dict:
#         dict[i]=dict[i]+1
#     else:
#         dict[i]=1
# print(dict)
#
# 经典手写冒泡排序
# a = [1,1,2,3,88,55,77]
#
# for i in  range(len(a)):
#     for j in range(len(a)-i-1):
#         if a[j] > a[j+1]:
#             a[j+1],a[j] = a[j],a[j+1]
# print(a)
# print(a[5])
















