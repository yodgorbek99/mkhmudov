# kinolar = []
# print("5 ta sevimli kinoingiz qaysilar?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar)    




# a = 23
# b = 43
# c = int(input("a=43\nb=23"))
# print(c)


# non = 2400
# soni = int(input("nechta non olasiz ?"))
# result = non * soni
# print(result)
# my_name is uygur
# whats your name


# misol = {"Ten":[10], "twenty": [20], "thirty": [30]}
# for i in range(keys)

#TASK-1
# lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
# upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
# print ("The Prime Numbers in the range are: ")  
# for number in range (lower_value, upper_value + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number) (number)



# import pprint
# n = 10
# m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
# pprint.pprint(m)




# for x in range(1, 11):
#         for y in range(1, 11):
#             z = x * y
#             print(z, end="\t")
#         print()


# yosh = int(input("yilingizni kiriting"))
# import datetime as dt
# natija = dt.date(1999, 6, 23)
# natija2 = dt.date(1999, 8, 22)
# javob = natija - natija2
# print(javob)

# from datetime import datetime, timedelta
# x_vaqt = datetime.now()
# print(x_vaqt)

# oldingi = x_vaqt - timedelta(days=5)
# print(oldingi)

# import datetime
# today = datetime.date.today()
# yesterday = today - datetime.timedelta(days = 1)
# tomorrow = today + datetime.timedelta(days = 1) 
# print(yesterday)
# print(today)
# print(tomorrow)

# import datetime
# today = datetime.date.today()
# oldingi1 = today + datetime.timedelta(days=5)
# print(oldingi1)

#RECURSION FUNCTION
# def display(n):
#     if n < 100:
#         print(n)
#         return display(n+1)
#     else:
#         return n

# print(display(1)) 



# l2 = ["olamgir", "bekzod", "muslima", "azamjon"]
# def display(l, n):
#     lent = len(l)
#     if n <= lent:
#         return display(l, n+1)
#     else:
#         return "done"

# display(l2, 0)            
 



# name = input("iltimos login kiriting:")
# anvar_pass = 7777
# if name == "anvar" and anvar_pass == 7777:
#    print("salom")
#    password = int(input("parol kiriting"))
#    print("kirish mumkin")



# username = 'polly1220'

# password = 'bob'

# userInput = input("What is your username?\n")

# if userInput == username:
#     a=input("Password?\n")   
#     if a == password:
#         print("Welcome!")
#     else:
#         print("That is the wrong password.")
# else:
#     print("That is the wrong username.") 



# def factorial(n):
      
#     if n == 0:
#         return 1
     
#     return n * factorial(n-1)
  
# num = int(input("nomer kiriting"))
# print("Factorial of", num, "is",
# factorial(num))      



# l1 = ["muslima", "bekzod", "khamza", 12,45,67]
# i = 0
# while i < len(l1):
#     print(l1[i])
#     i = i + 1



L1 = [12, 23, 45, 43]
L2 = [L1**"2"]
print(L2)

