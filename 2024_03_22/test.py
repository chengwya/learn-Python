# row = 1
# while row <= 5:
#     j=1
#     while j <= 5 - row:
#         print(" ", end=' ')
#         j += 1
#     k = 1
#     while k <= 2*row-1:
#         print("*", end=' ')
#         k+=1
#     print()
#     row+=1
# my_str = "Hello"
# for i in my_str:
#     print(i)

# break
# for i in range(0, 10):
#     if i % 2 == 0:
#         break
#     print(i, end=' ') #
#
# # continue
# for i in range(0, 10):
#     if i % 2 == 0:
#         continue
#     print(i, end=' ') # 1 3 5 7 9

# i=1
# while i < 10:
#     j=1
#     while j <= i:
#         print(f"{j}*{i}={i*j}\t", end=' ')
#         j+=1
#     print()
#     i+=1
# i = 0
# while i <= 3:
#     age = 18
#     guess = int(input("请输入你要猜的年龄："))
#     if guess > age:
#          print("猜大了")
#     elif guess < age:
#          print("猜小了")
#     else:
#         print("恭喜猜对了")
#         break
#     i += 1
#     if i == 3:
#         again = input("继续Y 停止N:")
#         if again == "Y" or again == "y":
#             i = 1
#         else:
#             break
#

height = 1.80
weight = 75.5
bmi = weight / (height**2)
if(bmi < 18.5):
    print("过轻")
elif 18.5<=bmi<25:
    print("正常")
elif 25 <=bmi<28:
    print("过重")
elif 28<=bmi<32:
    print("肥胖")
else:
    print("严重肥胖")