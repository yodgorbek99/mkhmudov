# from lesson import malumot







# def baxosi():
#     print("student id: ")
#     id=int(input())
#     mark1 = int(input())
#     mark2 = int(input())
#     mark3 = int(input())
#     mark4 = int(input())
#     sum = (mark1+mark2+mark3+mark4)
#     result = sum/4
#     print("test rezultat" +str(result))
#     return result




# def natija(scores):
#    baxo = dict()
#    for name in scores:
#       baxo[name] = sum(scores[name])/len(scores[name])

#    return list(baxo.values())

# scores = {"muslima": [34, 56, 89, 87], "abdugaffor": [70, 32, 78], "husain": [23, 56, 78], "ayub": [43, 67, 89, 96]}
# print(natija(scores))


#students = {'Yodgorbek' : [25,36,47,45],'Munisa' : [85,74,69,47],'Ahmad' : [65,35,87,14],'Xamza' : [74,12,36,75]}

# students = dict() #students funksiya yaratdik va uni ichidegi malumotlni dictionary qvolamiza
# n = int(input("Enter number of students :")) #studentlar sonini soridi va shunga qarab bzaga rezultat cqazb beradi
# for i in range(n):
#         sname = input("Enter names of student :") #bu ozgaruvchi student ismini soridi
#         marks= []
#         for j in range(3):
#            mark = (input("Enter marks :"))
#            marks.append(mark)
#         students[sname] = marks
# print("Dictionary of student created :")
# print(students)


#TASK_1
# def swap_case(text):
#    text_list = list(text)
#    text_list_converted = []

#    for i in text_list:
#       if i.isupper():
#          text_list_converted.append(i.lower())
#       elif i.islower():
#          text_list_converted.append(i.upper())

#    return "".join (text_list_converted)

# print(swap_case("Python"))      













#TASK_2
# def count_substring(string, sub_string):
#     c = 0
#     for i in range(len(string)):
#        if string[i:].startswith(sub_string):
#           c = c + 1
#     return c

# if __name__ == '__main__':
#    string = input().strip()
#    sub_string = input().strip()

#    count = count_substring(string, sub_string)
#    print(count)





#TASK_1
# lst1 = [44,54,64,74,104]
# lst2 = [i * 6 for i in lst1]
# print(lst2)



#TASK_2
# bolinma = [n for n in range(1,1000) if n % 7 == 0] 
# print(bolinma)





# my_list = [1,2,3,4,5,6,7,8,9,10]

# my_list.sort()

# print("mid value is ",my_list[int((len(my_list)-1)/2)])



# array = [1,2,3,4,5,6,7,8,9,10]
# x = 4
# def binarySearch(array, x, low, high):
#     while low <= high:

#         mid = low + (high - low)//2

#         if array[mid] == x:
#             return mid

#         elif array[mid] < x:
#             low = mid + 1

#         else:
#             high = mid - 1

#     return -1

# result = binarySearch(array, x, 0, len(array)-1)

# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")




# l1 = [1,2,3,4,5,6,7,8,9,10]
# n = 3
# while low <= high:

#         mid = low + (high - low)//2

#         if l1[mid] == n:
#             print(mid)

#         elif l1[mid] < n:
#             low = mid + 1

#         else:
#             high = mid - 1





# list01 = [1, 2, 3, 4, 5]
# list02 = [10, 20]

# for (i,j) in zip(list01, list02):
#     print (i,j)


# leetcode


# s = "123sdfsd4353432vdf"
# for string in s:
#     if string in dict.keys():
        
#         count = int[string]
#         dict[string] = count + 1
#     else:
       
#         dict[string] = 1




# def mysplit(s):
# ...     head = s.rstrip('0123456789')
# ...     tail = s[len(head):]
# ...     return head, tail
# ... 
# >>> [mysplit(s) for s in ['foofo21', 'bar432', 'foobar12345']]
# [('foofo', '21'), ('bar', '432'), ('foobar', '12345')]






# import re
# r = re.compile("([a-zA-Z]+)([0-9]+)")
# strings = ['foofo21', 'bar432', 'foobar12345']
# print [r.match(string).groups() for string in strings]




# l1 = [1,2,3,4,5]
# target = 5

# if l1 == target:
#     print("mum")
# else:
#     print("xato") 


# a_list = [1, 2, 3]
# integers_to_append = 4.
# a_list. append(integers_to_append)
# print(a_list)



# def filter_by_type(list_to_test, type_of):
#     return [n for n in list_to_test if isinstance(n, type_of)]

# myList = [ 4,'a', 'b', 'c', 1, 'd', 3]
# nums = filter_by_type(myList,int)
# strs = filter_by_type(myList,str)
# print(nums, strs)



# my_str = '246810hjnu'

# list_of_ints = [int(x) for x in my_str]
# print(list_of_ints)  # 👉️ [2, 4, 6, 8, 1, 0]

# mus = {"name": "john", "surname": "makhmudov"}
# def n(momo):
#     for key, value in mus:
#         return momo



text = input("enter your name")


def reversed_string(text):
    return text[::-1]