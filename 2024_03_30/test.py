# class Student:
#     name = None
#     age =  None
#     __id = None  # 私有成员变量
#
#     def __stu_info(self):
#         print("-----------") # 私有成员方法
#
# stu = Student()  # 创建对象
# stu.__stu_info() # 使用私有方法

# class Student:
#     name = None
#     age =  None
#     __id__stu = None  # 私有成员变量
#
#     def __stu_info(self):
#         print("-----------") # 私有成员方法
#
# stu = Student()  # 创建对象
# stu.__id__stu = 20    # 私有变量赋值  不报错，但无效
# print(stu.__id__stu)  # 获取私有变量值 报错，无法使用


# class Phone:
#     __is_5g_enable = False
#
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print("5G开启")
#         else:
#             print("5G关闭,开启4G网络")
#
#     def call_by_5g(self):
#         self.__check_5g()
#         print("正在通话中")
#
# phone = Phone()
# phone.call_by_5g()

# class Phone:
#     cpu = 'A13'
#     screen = 'LG'
#
#     def call_by_4g(self):
#         print("4G通话")
#
# class newPhone(Phone):
#     battery = None
#
#     def call_by_5g(self):
#         print("5G通话")
#
# Phone = newPhone()
# print(Phone.cpu)
# print(Phone.screen)
# Phone.call_by_4g()
# Phone.call_by_5g()

# class Phone:
#     producer = 'iP'
#     cpu = 'A13'
#
#     def call_by_5g(self):
#         print("5G通话")
#
# class NFCReader:
#     nfs_type = "第六代"
#     producer = "iP"
#
#     def read_card(self):
#         print("读卡")
#     def write_card(self):
#         print("写卡")
#
# class RemoteControl:
#     rc_type = "红外遥控"
#
#     def control(self):
#         print("开启红外遥控")
#
# class MyPhone(Phone, NFCReader, RemoteControl):
#     pass
#
# Phone = MyPhone()
# print(Phone.producer)
# print(Phone.cpu)
# print(Phone.rc_type)
# print(Phone.nfs_type)
# Phone.call_by_5g()
# Phone.read_card()
# Phone.write_card()
# Phone.control()

# class Phone:
#     producer = "iP"
#     cpu = "A13"
#
#     def call_by_5g(self):
#         print("父类 - 5G通话")
#
# class newPhone(Phone):
#     cpu = "A14"
#
#     def call_by_5g(self):
#         print("子类 - 5G通话")
#
# phone = newPhone()
# print(phone.cpu) # A14
# print(phone.producer) # iP
# phone.call_by_5g() # 子类 - 5G通话

# class Phone:
#     producer = "iP"
#     cpu = "A13"
#
#     def call_by_5g(self):
#         print("父类 - 5G通话")
#
# class newPhone(Phone):
#     cpu = "A14"
#
#     def call_by_5g(self):
#         # 方式1
#         print(f"父类中的处理器是：{Phone.cpu}")
#         Phone.call_by_5g(self)
#
#         # 方式2
#         print(f"父类中的处理器是：{super().cpu}")
#         super().call_by_5g()
#
#         print("子类 - 5G通话")
#
# phone = newPhone()
# phone.call_by_5g()

# # 基础数据类型注解
# num_1: int = 10
# num_2: float = 3.14
# num_3: bool = True
# num_4: str = "Hello"
#
# # 类对象类型注解
# class Student:
#     pass
# stu: Student = Student()
#
# # 基础容器类型注解
# my_list: list = [11, 12, 13, 14, 15]
# my_tuple: tuple = (6, 7, 8, 9, 10)
# my_set: set = {1, 2, 3, 4, 5}
# my_dict: dict = {"py": 10}
# my_str: str = "python"
#
# # 容器类型详细注解
# my_list: list[int] = [11, 12, 13, 14, 15]
# my_tuple: tuple[int, str, bool] = (6, "th", True)
# my_set: set[int] = {1, 2, 3, 4, 5}
# my_dict: dict[str, int] = {"py": 10}

# # 注释外进行类型注解
# import random
# num_1 = random.randint(1, 10) # type: int
# num_2 = {"gate": "road"}      # type: dict[str, str]
# def func():
#     return 1
# num_3 = func()                # type: int

# num_1: int = "python" # 不会报错
# num_2: str = 3.14     # 不会报错

# def add(x:int, y: int):
#     return x + y
# add()

# def sub(x:int, y: int) -> int:
#     z = x - y
#     return z
# print(sub(20, 10))

# from typing import Union
#
# my_list: list[Union[int, str]] = [10, 20, "hello", "python"]
# def func(data: Union[int, str]) -> Union[int, str]:
#     pass
# func()

# class Drinking:
#     def drink(self):
#         pass
# class Coffee(Drinking):
#     def drink(self):
#         print("咖啡")
# class Tea(Drinking):
#     def drink(self):
#         print("茶")
# def doWork(drinking: Drinking):
#     drinking.drink()
#
# coffee = Coffee()
# tea = Tea()
#
# doWork(coffee) # 咖啡
# doWork(tea) # 茶

class Drinking:
    def ice(self):
        pass
    def milk(self):
        pass
    def feeding(self):
        pass

class Coffee(Drinking):
    def ice(self):
        print("加冰")
    def milk(self):
        print("加燕麦牛奶")
    def feeding(self):
        print("加少糖")

class Tea(Drinking):
    def ice(self):
        print("加冰")
    def milk(self):
        print("加鲜牛奶")
    def feeding(self):
        print("加七分糖")

def doWork(drinking: Drinking):
    drinking.ice()
    drinking.milk()
    drinking.feeding()

coffee = Coffee()
tea  = Tea()
doWork(coffee)
print("--------")
doWork(tea)