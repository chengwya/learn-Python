# my_list = ['黑马程序员', '创智', '黑马程序员', '创智', 'itheima', 'itheima', 'itcast', 'best']
# set1 = set()
# for element in my_list:
#     set1.add(element)
# print(set1)

# # 定义字典字面量
# {key: value, key: value, .......,key: value}
# # 定义字典常量
# my_dict = {key: value, key: value, ......, key: value}
# # 定义空字典
# my_dict = {}
# my_dict = dict()

# my_dict1 = {"小明": 18, "小红": 19, "小王": 20}
# my_dict2 = {}
# my_dict3 = dict()
# print(f"mydict1字典的内容是{my_dict1},类型是{type(my_dict1)}")
# print(f"mydict2字典的内容是{my_dict2},类型是{type(my_dict2)}")
# print(f"mydict3字典的内容是{my_dict3},类型是{type(my_dict3)}")
#
# # 重复Key的字典
# my_dict4 = {"小明": 18, "小明": 20, "小红": 19}
# print(f"重复Key的my_dict4的内容是{my_dict4}")

# my_dict = {"小明": 18, "小红": 19, "小王": 20}
# print(my_dict["小明"]) # 18
# print(my_dict["小红"]) # 19
# print(my_dict["小王"]) # 20

# score_dict = {"小明": {"语文": 80, "数学": 90, "英语": 81},
#              "小红": {"语文": 85, "数学": 88, "英语": 83},
#              "小王": {"语文": 87, "数学": 80, "英语": 87}}
# print(f"考试信息是：{score_dict}")
# Xiaohong_English_score = score_dict["小红"]["英语"]
# print(f"小红的英语成绩是{Xiaohong_English_score}")

# a = 10
# b = 3
# print(f"a + b = {a + b}")
# print(f"a - b = {a - b}")
# print(f"a * b = {a * b}")
# print(f"a / b = {a / b}")
# print(f"a ** b = {a ** b}")
# print(f"a % b = {a % b}")
# print(f"a // b = {a // b}")

# a = 10
# b = 3
# print(f"a == b = {a == b}")
# print(f"a != b = {a != b}")
# print(f"a > b = {a > b}")
# print(f"a < b = {a < b}")
# print(f"a >= b = {a >= b}")
# print(f"a <= b = {a <= b}")

# a, b, c, d = 1, 2, 3, 4
# print(f"a+b>d and c+d>a = {a+b>d and c+d>a}")
# print(f"a+c>b or a+b>d = {a+c>b or a+b>d}")
# print(f"not a = {not a}")
# a = 10
# b = 3
# a = b
# print(f"a = b = {a}")
# a = 10
# b = 3
# a += b
# print(f"a += b = {a}")
# a = 10
# b = 3
# a -= b
# print(f"a -= b = {a}")
# a = 10
# b = 3
# a *= b
# print(f"a *= b = {a}")
# a = 10
# b = 3
# a /= b
# print(f"a /= b = {a}")
# a = 10
# b = 3
# a %= b
# print(f"a %= b = {a}")
# a = 10
# b = 3
# a **= b
# print(f"a **= b = {a}")
# a = 10
# b = 3
# a //= b
# print(f"a //= b = {a}")

# print("Hello")
# print("Python")

# name1 = "小明"
# name2 = "小红"
# age = 18
# print("我的名字是%s" % name1)
# print("我的名字是%s,年龄是%d" % (name2, age))

# name1 = "小明"
# name2 = "小红"
# age = 18
# print("我的名字是{}".format(name1))
# print("我的名字是{},年龄是{}".format(name2, age))

name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
print("我的名字是{},年龄是{}".format(name, age))
