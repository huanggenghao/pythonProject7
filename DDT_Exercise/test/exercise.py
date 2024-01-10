# -*- coding: utf-8 -*-            
# @Author : ben
# @Time : 2024/1/4 10:14
# import unittest
# from ddt import ddt, data, unpack
# import sys
#1.如何显示字符串反转
# import os

import logging

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

logging.basicConfig(level='DEBUG')





