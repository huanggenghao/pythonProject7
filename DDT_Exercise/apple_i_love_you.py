# -*- coding: utf-8 -*-            
# @Author : ben
# @Time : 2024/1/17 13:57
import turtle

# 设置画布的大小和背景颜色
turtle.setup(800, 600)
turtle.bgcolor("black")

# 创建一个红色的苹果形状
turtle.color("red")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# 写下“我爱你”的文字
turtle.penup()
turtle.goto(-50, 50)
turtle.color("white")
turtle.write("我爱你", font=("Arial", 30, "bold"))

# 隐藏画笔
turtle.hideturtle()

# 点击关闭窗口时退出程序
turtle.done()