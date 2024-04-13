# from pymysql import Connection
# # 获取到MySQL数据库的链接对象
# conn = Connection(
#     host="localhost",    # 主机名
#     port=3306,           # 端口
#     user="root",         # 账户名
#     password="123456"    # 密码
# )
#
# print(conn.get_server_info()) # 打印MySQL数据库信息
#
# # conn.close() # 关闭到数据库的链接
#
# from pymysql import Connection
# # 获取到MySQL数据库的链接对象
# conn = Connection(
#     host="localhost",    # 主机名
#     port=3306,           # 端口
#     user="root",         # 账户名
#     password="123456",   # 密码
#     autocommit= True     # 设置自动提交
# )
#
# cursor = conn.cursor() # 获取游标对象
# conn.select_db("world") # 选择数据库
# cursor.execute("insert into student values(7, '小东', 20)") # 用游标对象，执行SQL语句
# conn.commit() # 确认
# conn.close() # 关闭

# from pyspark import SparkConf,SparkContext # 导包
# conf = SparkConf().setMaster("local[*]").setAppName(("test_spark")) # 创建SparkConf类对象
# sc = SparkContext(conf=conf) # 基于SparkConf类对象创建SparkContext类对象
#
# rdd = sc.textFile("E:/learn - coding/Python/2024_04_13/hello.txt")
# print(rdd.collect())
# rdd1 = sc.parallelize([1, 2, 3])
# rdd2 = sc.parallelize((1, 2, 3))
# rdd3 = sc.parallelize("hello")
# rdd4 = sc.parallelize({1, 2, 3})
# rdd5 = sc.parallelize({"key1":1, "key2": 2})

# print(rdd1.collect()) # 输出RDD内容
# print(rdd2.collect()) # 输出RDD内容
# print(rdd3.collect()) # 输出RDD内容
# print(rdd4.collect()) # 输出RDD内容
# print(rdd5.collect()) # 输出RDD内容

# sc.stop() # 停止SparkContext对象的运行
#
# from pyspark import SparkConf,SparkContext
# import sys
# import os
# print(sys.executable)
# os.environ['PYSPARK_PYTHON'] = "E:/learn - coding/Python/2024_04_13/.venv/Scripts/python.exe"
#
#
# conf = SparkConf().setMaster("localhost[*]").setAppName("test_spark")
# sc = SparkContext(conf=conf)
#
# rdd = sc.parallelize([1, 2, 3])
#
# def func(data):
#     return data + 3
#
# rdd2 = rdd.map(func)
# print(rdd2.collect())
#
# rdd3 = rdd.map(lambda x: x * 10).map(lambda x: x + 2 )
# print(rdd3.collect())

# def outer(logo):
#     def inner(msg):
#         print(f"<logo>{msg}<logo>")
#     return inner
#
# fn1 = outer("Hello")
# fn1("world")
# fn1("World")
#
# fn2 = outer("Python")
# fn2("hello")
# fn2("Hello")

# def account_Create(amount_Init=0):
#     def atm(num, deposit=True):
#         nonlocal amount_Init
#         if deposit:
#             amount_Init += num
#             print(f"存款+{num}，账户余额{amount_Init}")
#         else:
#             amount_Init -= num
#             print(f"存款-{num}，账户余额{amount_Init}")
#     return atm
#
# fn = account_Create()
# fn(100)
# fn(300, True)
# fn(200, False)

# def outer(func):
#     def inner():
#         print("11111")
#         func()
#         print("22222")
#     return inner
# @outer
# def sleep():
#     import random
#     import time
#     print("睡觉Zzzz")
#     time.sleep(random.randint(1,3))
#
# sleep()

# from test02 import str_tool
#
# s1 = str_tool
# s2 = str_tool
# print(s1)
# print(s2)
# """
# <test02.strTools object at 0x000001BFBED43EF0>
# <test02.strTools object at 0x000001BFBED43EF0>
# """

# class Person:
#     pass
#
# class Worker(Person):
#     pass
# class Student(Person):
#     pass
# class Teacher(Person):
#     pass
#
# class Factory:
#     def get_person(self,person_Type):
#         if person_Type == 'w':
#             return Worker()
#         elif person_Type == 's':
#             return Student()
#         else:
#             return Teacher()
#
# factory = Factory()
# worker = factory.get_person('w')
# student = factory.get_person('s')
# teacher = factory.get_person('t')

import threading
import time

def Coffee(msg):
    while True:
        print(msg)
        time.sleep(1)

def Tea(msg):
    while True:
        print(msg)
        time.sleep(1)

# 创建进程
coffee_thread = threading.Thread(target=Coffee, args=("喝咖啡"))
tea_thread = threading.Thread(target=Tea, args={"msg": "喝茶"})

# 执行进程
coffee_thread.start()
tea_thread.start()