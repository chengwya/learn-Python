# # 定义集合字面量
# {元素1, 元素2, ....元素n}
# # 定义集合变量
# 变量名 = {元素1, 元素2, ....元素n}
# # 定义空集合
# 变量名 = set()

# my_set = {"ha", "he", "he"}
# my_set_empty = set()
# print(f"my_set的内容是{my_set}, 类型是{type(my_set)}")
# print(f"my_set_empty的内容是{my_set_empty}, 类型是{type(my_set_empty)}")

# my_set = {"hello", "world"}
# my_set.add("hahe")
# print(f"my_set添加元素后的结果是{my_set}") # my_set添加元素后的结果是{'hahe', 'hello', 'world'}
#
# my_set = {"hello", "world"}
# my_set.remove("hello")
# print(f"my_set移除元素后的结果是{my_set}") # my_set移除元素后的结果是{'world'}

# my_set = {"hello", "world"}
# element = my_set.pop()
# print(f"my_set被随机移除{element}后结果是{my_set}") # my_set被随机移除world后结果是{'hello'}
#
# my_set = {"hello", "world"}
# my_set.clear()
# print(f"my_set被清空后的结果是{my_set}") # my_set移除元素后的结果是{'world'} # my_set被清空后的结果是set()

# set1 = {1, 3, 4}
# set2 = {1, 2, 3}
# set3 = set1.difference(set2)
# print(set1) # {1, 3, 4}
# print(set2) # {1, 2, 3}
# print(set3) # {4}

# set1 = {1, 3, 4}
# set2 = {1, 2, 3}
# set1.difference_update(set2)
# print(set1) # {4}
# print(set2) # {1, 2, 3}

# set1 = {1, 3, 4}
# set2 = {1, 2, 3}
# set3 = set1.union((set2))
# print(set1) # {1, 3, 4}
# print(set2) # {1, 2, 3}
# print(set3) # {1, 2, 3, 4}

# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# num = len(set1)
# print(f"set1统计集合元素数量是{num}") # set1统计集合元素数量是10
# 集合不支持下标索引，所以不能使用while循环
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for element in set1:
    print(f"set1中的元素有{element}")
