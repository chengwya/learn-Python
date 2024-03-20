# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = "hello"
# my_set =  {1, 2, 3, 4, 5}
# my_dict = {"key1": 1, "key2": 2, "key3": 3}
# print(max(my_list))  # 10
# print(max(my_tuple)) # 5
# print(max(my_str))   # o
# print(max(my_set))   # 5
# print(max(my_dict))  # key3

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = "hello"
# my_set =  {1, 2, 3, 4, 5}
# my_dict = {"key1": 1, "key2": 2, "key3": 3}
# print(min(my_list))  # 1
# print(min(my_tuple)) # 1
# print(min(my_str))   # e
# print(min(my_set))   # 1
# print(min(my_dict))  # key1

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = "hello"
# my_set =  {1, 2, 3, 4, 5}
# my_dict = {"key1": 1, "key2": 2, "key3": 3}
# print(len(my_list))  # 10
# print(len(my_tuple)) # 5
# print(len(my_str))   # 5
# print(len(my_set))   # 5
# print(len(my_dict))  # 3

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = "hello"
# my_set =  {1, 2, 3, 4, 5}
# my_dict = {"key1": 1, "key2": 2, "key3": 3}
# print(f"列表转列表：{list(my_list)}")
# print(f"元组转列表：{list(my_tuple)}")
# print(f"字符串转列表：{list(my_str)}")
# print(f"集合转列表：{list(my_set)}")
# print(f"字典转列表：{list(my_dict)}")

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = "hello"
# my_set =  {1, 2, 3, 4, 5}
# my_dict = {"key1": 1, "key2": 2, "key3": 3}
# print(f"列表转元组：{tuple(my_list)}")
# print(f"元组转元组：{tuple(my_tuple)}")
# print(f"字符串转元组：{tuple(my_str)}")
# print(f"集合转元组：{tuple(my_set)}")
# print(f"字典转元组：{tuple(my_dict)}")

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_tuple = (1, 2, 3, 4, 5)
# my_str = "hello"
# my_set =  {1, 2, 3, 4, 5}
# my_dict = {"key1": 1, "key2": 2, "key3": 3}
# print(f"列表转集合：{set(my_list)}")
# print(f"元组转集合：{set(my_tuple)}")
# print(f"字符串转集合：{set(my_str)}")
# print(f"集合转集合：{set(my_set)}")
# print(f"字典转集合：{set(my_dict)}")

# my_list = [7, 5, 9, 4, 2, 6, 1, 10, 3, 8]
# my_tuple = (3, 5, 1, 4, 3)
# my_str = "afedcb"
# my_set =  {5, 3, 2, 4, 1}
# my_dict = {"key3": 1, "key2": 2, "key1": 3}
# print(f"列表排序后：{sorted(my_list)}")
# print(f"元组排序后：{sorted(my_tuple)}")
# print(f"字符串排序后：{sorted(my_str)}")
# print(f"集合排序后：{sorted(my_set)}")
# print(f"字典排序后：{sorted(my_dict)}")
#
# my_list = [7, 5, 9, 4, 2, 6, 1, 10, 3, 8]
# my_tuple = (3, 5, 1, 4, 3)
# my_str = "afedcb"
# my_set =  {5, 3, 2, 4, 1}
# my_dict = {"key3": 1, "key2": 2, "key1": 3}
# print(f"列表反向排序后：{sorted(my_list, reverse = True)}")
# print(f"元组反向排序后：{sorted(my_tuple,reverse = True)}")
# print(f"字符串反向排序后：{sorted(my_str,reverse = True)}")
# print(f"集合反向排序后：{sorted(my_set,reverse = True)}")
# print(f"字典反向排序后：{sorted(my_dict,reverse = True)}")

# def test_return():
#     return 1,"hello", True
#
# x, y, z = test_return()
# print(x) # 1
# print(y) # hello
# print(z) # True

# def Student(name, sex, age):
#     print(f"我的名字是{name},性别是{sex}，今年{age}岁") # 我的名字是小明,性别是男，今年18岁
# Student("小明", "男", 18)

# def Student(name, sex, age):
#     print(f"我的名字是{name},性别是{sex}，今年{age}岁")
# Student(name = "小明", age = 20, sex = "男")
# Student(sex = "女", age = 18, name = "小红")
# Student( "小李", age = 19, sex = "男")

# def Student(name, sex, age = 18):
#     print(f"我的名字是{name},性别是{sex}，今年{age}岁")
# Student("小明", "男", 20) # 我的名字是小明,性别是男，今年20岁
# Student("小红", "女", 19) # 我的名字是小红,性别是女，今年19岁
# Student("小王", "女")          # 我的名字是小王,性别是女，今年18岁

# def Student(*args):
#     print(args)
# Student("小明", "211515", 20) # ('小明', '211515', 20)
# Student("小红",  18)          # ('小红', 18)

# def Student(**kwargs):
#     print(kwargs) # {'name': '小明', 'sex': '男', 'age': 18}
# Student(name="小明", sex="男", age=18)

# # 定义一个函数，接收另一个函数作为传入参数
# def test(calculate):
#     ret = calculate(10, 20)
#     print(ret)
#
# # 定义一个函数，作为参数传入另一个函数
# def calculate(x, y):
#     return x + y;
#
# # 调用并传入参数
# test(calculate) # 30
# 定义一个函数，接收其他函数输入
def test(calculate):
    ret = calculate(10, 20)
    print(ret)

# 通过lambda匿名函数的形式，将匿名函数作为参数传入
test(lambda x, y: x + y) # 30
