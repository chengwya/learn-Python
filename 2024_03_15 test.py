# a = 10   # 定义一个名称为a的变量
# a = 20   # 变量可多次赋值
# print(a) # 变量需先定义再使用

# a = 10
# print(type(a))
# b = 3.14
# print(type(b))
# c = 'he'
# print(type(c))
# d = True
# print(type(d))
# e = []
# print(type(e))
# f = ()
# print(type(f))
# g = {}
# print(type(g))

# Name_1 = "小明"
# 2_Name = "小红" # 报错
# _Name3 = "小王"
# False = 3.14 # 报错
# class Name4 = "小张" # 报错

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ret1 = num_list[1:5]   # 步长可省略不写，默认为1
# print(f"结果1为{ret1}")
#
# num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# ret2 = num_list[:]
# print(f"结果2为{ret2}")
#
# num_str = "12345678910"
# ret3 = num_list[::2]
# print(f"结果3为{ret3}")
#
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ret4 = num_list[::-1]   # 步长可省略不写，默认为1
# print(f"结果4为{ret4}")
#
# num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# ret5 = num_list[3:1:-1]
# print(f"结果5为{ret5}")
#
# num_str = "12345678910"
# ret6 = num_str[::-2]
# print(f"结果6为{ret6}")

name = "你好，明小叫字名的我，我今年18岁"
str = name[9:2:-1]
print(str)