#TASK_1

# n = int(input("Raqamni kiriting: "))
# s = 0

# for i in range(n + 1):
#     s += i

# print("Natija: ", s)



#TASK_2

# numbers = [12, 75, 150, 180, 145, 525, 50]
# numbers_2 = []

# for i in numbers:
#     if i > 500:
#         break
#     if i > 150:
#         continue
#     if i % 5 == 0:
#         numbers_2.append(i)

# print(numbers_2) 




# numbers = [12, 75, 150, 180, 145, 525, 50]
# # iterate each item of a list
# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     # check if number is divisible by 5
#     elif item % 5 == 0:
#         print(item) 
      




# Mutable is a fancy way of saying that the internal state of the object is changed/mutated. So, the simplest definition is: An object whose internal state can be changed is mutable. On the other hand, immutable doesn't allow any change in the object once it has been created.      



# name = "yodgorbek"
# age = 23
# year = 1999


# info = {"name": "yodgorbek", "age": 23, "year": 1999, "hobbies": ["games", "tennis"]}
# print(info["hobbies"][1])


# info = {"name": "yodgorbek", "age": 23, "year": 1999, "hobbies": {"hob_1": "dota", "hob_2": "tennis"}}
# info_2 = info["hobbies"]
# for i in info.values():
#     print(i)
# if info_2 == i:
#         print(info_2["hobbies"][1])


# sonlar_1 = int(input("iltimos sonni kiriting"))
# if sonlar_1 == 4 or 7 or 22 or 40:
#     print("siz togri topdingiz")
# else:
#     print("afsuski xato") 


# son_1 = int(input("sizda 10 ta urinish bor biror raqam kiriting: "))
# son_2 = int(input("sizda 8 ta urinish bor biror raqam kiriting: "))
# son_3 = int(input("sizda 7 ta urinish bor biror raqam kiriting: "))
# son_4 = int(input("sizda 6 ta urinish bor biror raqam kiriting: "))
# sonlar = son_1 + son_2 + son_3 + son_4
# if sonlar == 4:
#     print("togri")
# else:
#     print("xato")


#TASK_1
# sonlar = [2, 33, 45, 13, 150]
# print("Eng katta son: ", max(sonlar))


#TASK_2
# ball = int(input("nechchi ball to'plaganingizni kiriting: "))
# spiska = int(input("nechanchi o'rinda turganingizni kiriting: "))

# if ball > 300 and spiska <= 10:
#     print("Tabriklaymiz siz o'qishga 'GRANT' asosida qabul qilindingiz")

# else:
#     print("Tabriklaymiz siz o'qishga 'KONTRAKT' asosida qabul qilindingiz")  



#TASK_3
# qarzdor = input("Ismingizni kiriting: ") 
# qarz = int(input("Nech pul qarzingiz bor ? KIRITING: ")) 
# print(f"{qarzdor} sizning to'laydigan qarzingiz: {qarz}")

# summa = int(input("Nech pul kiritasiz: "))
# while qarz != summa:
#     print(f"Yetarli emas, {qarzdor}. Keling, yana qilaylik.")
#     summa = int(input("Nech pul kiritasiz: "))

 
# print(f"Ajoyib, {qarzdor}! Siz qarzingizni to'ladingiz. Rahmat!")


    
    



# def malumot(model, rangi, narxi, **kwargs):
#     print(
#     f"moshinani modeli {model}, rangi {rangi}, narxi {narxi}, qolgan malumotlar {kwargs}")

# malumot(model="toyota", rangi="oq", narxi="13000", kms=210, yurgani=23000) 


#TASK_1
# s1 = 12
# s2 = 23
# s3 = 56


# def katta_son(s1, s2, s3):

#     if s1 >= s2 and s1 >= s3:
#         katta_bolsa = s1

#     elif s2 >= s1 and s2 >= s3:
#         katta_bolsa = s2

#     else:
#         katta_bolsa = s3

#         return katta_bolsa


# print(katta_son(s1, s2, s3))

#TASK_2

# def sum_numbers(numbers):
#      if len(numbers) == 0:
#          return 0
#      return numbers[0] + sum_numbers(numbers[1:])

# print(sum_numbers([1, 2, 3]))


# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
# print(sum_list([1, 2,-8]))        

#TASK_3
# def sum_list(items):
#     sum_numbers = 1
#     for x in items:
#         sum_numbers *= x
#     return sum_numbers
# print(sum_list([1, 2, 8]))


# def mul_list(list) :
     
#     # Multiply elements one by one
#     product = 1
#     for i in list:
#          product = product * i
#     return product
     
# list = [2, 3, 4]
# print(mul_list(list))

#TASK_4

# def reversed_string(text):
#      result = ""
#      for char in text:
#          result = char + result
#      return result

# print(reversed_string("Hello, World!"))




import requests

domain = input("enter domain name: ")
url = f"https://api.domainsdb.info/v1/domains/search?domain={domain}"
r = requests.get(url)

print(r.json())