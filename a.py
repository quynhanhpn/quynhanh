#bài 1
# a = input("nhập: ")
# b = input("nhập: ")
# print("tên đầy đủ là",a,b)
#bài 2
# a = input("nhập: ")
# print(a.upper())
#bài 3
# a = int(input("nhập số: "))
# print(a**2)
#bài 4
# a = int(input("nhập số: "))
# from turtle import*
# penup()
# goto(-100, a)
# pendown() 
# circle(a)
# mainloop()


#bài 1
# for i in range(0,13):
#    if i % 3 ==0:
#     print(i)
#bài 2
# n = int(input("nhập số: "))
# for i in range(0,n + 1):
#     print(i)
#bài 3
# for i in range(0,11):
#    if i % 2 != 0:
#     print(i)
#bài 4
# a = int(input("nhập cạnh: "))
# from turtle import*
# forward(a)
# right(60)
# forward(a)
# right(60)
# forward(a)
# right(60)
# forward(a)
# right(60)
# forward(a)
# right(60)
# forward(a)
# right(60)
# mainloop()


#bài 1
# a = int(input("nhập số: "))
# if a > 13:
#     print("lớn hơn 13")
# else: 
#     print("ko lớn hơn 13")
#bài 2
# a = int(input("nhập số: "))
# if a % 2 == 0 :
#     print("chẵn")
# else: 
#     print("lẻ")
#bài 3
# a = int(input("nhập tháng: "))
# if a ==  1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12 :
#     print("31 ngày")
# elif a ==  4 or a == 6 or a == 9 or a == 11:
#     print("30 ngày ")
# else: 
#     print("28 hoặc 29 ngày")


#bài 1
# a = input("Username: ")
# b = input("Password: ")
# c = input("Email: ")
# if a and b and c != " ":
#     print("đăng nhập thành công")
# else:
#     print("đăng nhập ko thành công")
#bài 2
# a = input("Username: ")
# b = input("Password: ")
# d = input("Repeat password: ")
# c = input("Email: ")
# if a and b and c != " ":
#     if b == d:
#         print("đăng nhập thành công")
#     else: 
#         print("đăng nhập ko thành công")
# else:
#     print("đăng nhập ko thành công")
#bài 3
# a = input("Username: ")
# b = input("Password: ")
# d = input("Repeat password: ")
# c = input("Email: ")
# if a and b and c != " ":
#     if b == d:
#         if "@" in c:
#             if len(c) > 8:
#                 print("đăng nhập thành công")
#             else:
#                 print("đăng nhập ko thành công")
#         else:
#             print("đăng nhập ko thành công")
#     else: 
#         print("đăng nhập ko thành công")
# else:
#     print("đăng nhập ko thành công")


#phần 5
import random
a = random.randint(3 , 9)
b = random.randint(3 , 9)
score = 0
print(int(a))
print(int(b))
ques1 = a + b
ans = int(input("nhập đáp án: "))
if ans == ques1:
    score += 1
    print("đúng, điểm: ",score )
    print(int(a))
    print(int(b))
    ques2 = a - b
    ans = int(input("nhập đáp án: "))
    if ans == ques2:
      score += 1
      print("đúng, điểm: ",score )
      print(int(a))
      print(int(b))
      ques3 = a * b
      ans = int(input("nhập đáp án: "))
      if ans == ques3:
         score += 1
         print("đúng, điểm: ",score )
         print(int(a))
         print(int(b))
         ques4 = a / b
         ans = int(input("nhập đáp án: "))
         if ans == ques4:
           score += 1
           print("đúng, điểm: ",score )
           
         else: 
           print("sai")
      else: 
          print("sai")
    else: 
        print("sai")
else: 
    print("sai")