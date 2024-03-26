# f = open("test.txt", "r", encoding="ETF-8")

# try:
#     f = open("test.txt", "r", encoding="UTF-8")
# except:
#     f = open("test.txt", "w", encoding="UTF-8")

# try:
#     print(age)
# except NameError as e:
#     print("出现了变量未定义的异常")
#     print(e)

# try:
#     # print(age)
#     1 / 0
# except (NameError,ZeroDivisionError ):
#     print("出现了变量未定义的异常或除0的异常")

# try:
#     f = open("Python.txt", "r", encoding="UTF=8")
# except Exception as e:
#     print("出现异常")
# else:
#     print("没有出现异常")
# finally:
#     f.close()

def func01(): # 异常在func01中没有被捕获
    print("func01 - start!")
    num = 1 / 0
    print("func01 - end!")

def func02(): # 异常在func02中没有被捕获
    print("func02 - start!")
    func01()
    print("func02 - end!")

def main(): # 异常再main函数中捕获
    try:
        func02()
    except Exception as e:
        print(e)