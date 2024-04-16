# import socket # 导包
# socket_client = socket.socket() # 创建socket对象
# socket_client.connect(("localhost", 8888)) # 连接到服务器
# socket_client.send("你好".encode("UTF-8")) # 发送消息
# data = socket_client.recv(1024) # 接收信息并返回
# print(f"服务端返回的信息为：{data}") #
# socket_client.close() # 关闭连接
# import re
#
# str = "hello python"
# ret = re.match("hello", str)
# print(ret) # <re.Match object; span=(0, 5), match='hello'>
# print(ret.span()) # (0, 5)
# print(ret.group()) # hello
#
# str2 = "1hello python"
# ret2 = re.match("hello", str2)
# print(ret2) # None
# print(ret2.span())
# print(ret2.group())

# import re
#
# str = "hello python"
# ret = re.search("python", str)
# print(ret) # <re.Match object; span=(6, 12), match='python'>
# print(ret.span()) # (6, 12)
# print(ret.group()) # python
#
# str2 = "hello 1python"
# ret2 = re.search("python", str2)
# print(ret2) # None # <re.Match object; span=(7, 13), match='python'>
# print(ret2.span()) # (7, 13)
# print(ret2.group()) # python

# import re
#
# str = "hello python"
# ret = re.findall("python", str)
# print(ret) # ['python']
#
#
# str2 = "hello 1python"
# ret2 = re.search("world", str2)
# print(ret2) # None
# import re
#
# str = "hello 2python"
# ret = re.findall(r'[e-h]', str) # 字符串前加上r标记，表示字符串中转义字符无效,为普通字符
# print(ret) # ['h', 'e', 'h']

# import re
# # 1
# r = '^[0-9a-zA-Z]{6,10}$' # 只能由字母和数字组成，长度范围6-10位
# str = '123456abc'
# print(re.findall(r, str)) # ['123456abc']
#
# # 2 纯数字，长度5-10位，第一位不可为0
# r = '^[1-9][0-9]{5,9}$'
# str = '12345678'
# print(re.findall(r, str)) # ['12345678']
#
# # 3 匹配邮箱地址，只允许168、qq邮箱地址
# r = r'(^[\w-]+(\.[\w-]+)*@(163|qq)(\.[\w-]+)+$)'
# str = 'ziqi@163.com'
# print(re.findall(r, str)) # [('ziqi@163.com', '', '163', '.com')]

import os

def test_os():
    print(os.listdir("D:/test"))       # 列出路径下的内容
    print(os.path.isdir("D:/test/a"))  # 判断指定路径是不是文件夹
    print(os.path.exists("D:/test"))   # 判断指定路径是否存在

def get_files(path):
    """
    从指定的文件中用递归的方式，获取全部的文件列表
    :param path: 被判断的文件夹
    :return: 包含全部文件，若目录不存在或无文件则返回一个空list[]
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                get_files(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定目录{path}不存在")
        return []

print(get_files("D:/test"))