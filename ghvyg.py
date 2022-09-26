#ism = input("ismingizni kiriting:")
#familya = input("familyangizni kiriting:")
#yosh = input("yoshingizni kiriting:")
#print(f"sizning ismingiz: {ism}, sizning fmilyangiz: {familya}, sizning yoshingiz: {yosh} ")


# n1 = input("birinchi son")
# n2 = input("ikkinchi son")
# n3 = input("uchinchi son")
# print(int(n1) + int(n2) + int(n3))


#bogcha_yosh = int(input("bolangizning yoshini kiriting"))
#if bogcha_yosh >= 3:
#    print("kirishingiz mumkin")
#else:
#    print("kirish mumkin emas")


#name = input("iltimos ismingizni kiriting:")
#anvar_pass = 7777
#if name == "anvar" and anvar_pass == 7777:
#    print("salom")
#    password = int(input("parol kiriting"))
#    print("kirish mumkin")

#else:
#    print("kirish mumkin emas")
                        
#name = input("kirit")
#password = int(input("parol"))
#
#if name == "anvar" and password == 777:
#    print("kirish mumkin")
#else:
#    print("error")  


# fruits = ["nok", "olma", "tarvuz", "kivi", "banan", "qovun"]
# print(fruits[3::])


#rain = int(input("iltimos kodni kiriting: "))
#if rain == 1:
#    print("kochada yomgir yogyapti iltimos soyabonni oling")
#elif rain == 0:
#    print("kochada yomgir yogmiyapti")
#
#else:
#    print("error")


#russian_l = int(input("rus tilidan to'plagan balingizni kiritng\n>>> "))
#math = int(input("matematikadan to'plagan blingizni kiriting\n>>> "))
#it = int(input("informatikadan toplagan balingizni kiriting\n>>> "))
#score = russian_l + math + it
#
#if score >= 270:
#    print("siz grandga o'qishga qabul qilindingiz !")
#else:
#    print("afsuski siz grandga o'qishga qabul qilinmadingiz !")

#pop (ocirish)
#remove (predmetni ocirdi)

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [2]

for n in l1:
   print(n*2)
   if n == 3:
       pass
   else:
       l2.append(n*2)


#print(l2)


# l1 = [1, 2, 3, 4, 5, 6, 7]
# toq_sonlar = []

# for i in l1:
#     if toq_sonlar != 0:
#         print(i)


# n = 100
# while n > 0:
#     n /= 2
#     print(n)




# n = int(input("Raqamni kiriting: "))
# i = 0
# for son in range(1, n + 1):
#     i += son
# print("Natija: ", i)


# n = int(input("Raqamni kiriting: "))
# s = 0

# for i in range(n + 1):
#     s += i

# print("Natija: ", s)
    

# while True:
#     try:
#         age = int(input("Please enter your age: "))
#     except ValueError:
#         print("Sorry, I didn't understand that.")
#         continue

#     if age < 0:
#         print("Sorry, your response must not be negative.")
#         continue
#     else:
#         break
# if age >= 18:
#     print("You are able to vote!")
# else:
#     print("You are not able to vote.")

