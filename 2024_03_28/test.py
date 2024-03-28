# class Student:
#     name = None
#     age = None
#     def print_Info(self):
#         print(f"我的名字{self.name},年龄{self.age}")
# stu_1 = Student()
# stu_1.name = "小明"
# stu_1.age = 18
# stu_1.print_Info()

# class Student:
#     name  = None
#     age = None
#     def print_info(self):
#         print(f"我叫{self.name}")
#     def print2_info(self, msg):
#         print(f"我的年龄是{msg}")
# stu = Student()
# stu.name = "小明"
# stu.print_info()    # 调用时无需传参
# stu.print2_info(18) # 调用时需要传msg参数

# class Clock:
#     id = None     # 闹钟编号
#     price = None  # 闹钟价格
#     def ring(self): # 闹钟响铃
#         import winsound
#         winsound.Beep(1000, 3000) # (频率， 时间)
# clock1 = Clock()
# clock1.id = "000001"
# clock1.price = 12.9
# print(f"闹钟编号{clock1.id}, 价格为{clock1.price}")
# clock1.ring()
#
# clock2 = Clock()
# clock2.id = "000002"
# clock2.price = 15.9
# print(f"闹钟编号{clock2.id}, 价格为{clock2.price}")
# clock2.ring()
#
# clock3 = Clock()
# clock3.id = "000003"
# clock3.price = 18.9
# print(f"闹钟编号{clock3.id}, 价格为{clock3.price}")
# clock3.ring()

# class Student:
#     name = None
#     age = None
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#         print("Student创建了一个对象")
# stu = Student("小明",18)
# print(stu.name)
# print(stu.age)

# class Student:
#     id = None
#     name = None
#     sex = None
#     age = None
#     def __init__(self, id, name, sex, age):
#         self.id = id
#         self.name = name
#         self.sex = sex
#         self.age = age
# for i in range(1,11):
#     print(f"当前录入第{i}位学生信息，总共录入10位学生信息")
#     print(f"请输入学生学号:",end=" ")
#     id = int(input())
#     print(f"请输入学生姓名:",end=" ")
#     name = input()
#     print(f"请输入学生性别:",end=" ")
#     sex = input()
#     print(f"请输入学生年龄:",end=" ")
#     age = int(input())
#     stu = Student(id, name, sex, age)
#     print(f"学生{i}信息录入完成，信息为：学生学号：{stu.id},学生姓名：{stu.name},学生性别：{stu.sex}, 学生年龄：{stu.age}")

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Student： name = {self.name}, age = {self.age}"
# stu = Student("小明", 18)
# print(stu)
# print(str(stu))

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __lt__(self, other):
#        return self.age < other.age
#
# s1 = Student("小明", 20) # False
# s2 = Student("小红", 18) # True
# print(s1 < s2)
# print(s1 > s2)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __le__(self, other):
#        return self.age <= other.age
#
# s1 = Student("小明", 20) # False
# s2 = Student("小红", 18) # True
# s3 = Student("小王", 18) # True
#
# print(s1 <= s2)
# print(s1 >= s2)
# print(s2 >= s3)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
       return self.age == other.age

s1 = Student("小明", 18)
s2 = Student("小红", 18)

print(s1 == s2) # True
