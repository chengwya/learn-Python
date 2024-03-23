# def add(x , y):
#     """
#     该函数进行两个整型数据进行相加，并返回相加后的值
#     """
#     return x + y
#
# result = add(10, 20)
# print(result) # 30

# def Mul(x, y ):   # 形式参数：意义上的一种参数，在定义时不占内存地址
#     sum = x*y
#     print(sum)
# # 在调用函数时必选参数是必须要赋值
# Mul(10, 5) # 实际参数：意义上的一种参数，在定义时不占内存地址
# # Mul(20)          # 报错

# def Mul(x, y=5): # 默认参数始终存在于参数列表中的尾部
#     print(f"默认参数使用={x*y}") # 100
# # 默认参数调用，在调用时如果没赋值，就会使用定义函数时给定的默认值
# Mul(20)

# def PrintInfo(*args):
#     print(args) # ('Hello',)
# str = "Hello"
# PrintInfo(str)

