# function
# 1
# def make_noise():
#     print("THE CROWD GOES WILD")
# make_noise()

# 4
# def yell(x):
#     print(x.upper() + "!")
#     return x
# yell("go away")
# yell("leave me alone")

# 5
# def count_dollar_signs(word):
#     count = 0
#     for char in word:
#         if char == "$":
#             count += 1
#     return count
# print(count_dollar_signs("$uper$ize"))

# 6
# def product(x, y):
#     return x * y
# print(product(2, 2))
# print(product(2, -2))

# 7
# def return_day(x):
#     if x == 1:
#         return "Sunday"
#     elif x == 2:
#         return "Monday"
#     elif x == 3:
#         return "Tuesday"
#     elif x == 4:
#         return "Wednsday"
#     elif x == 5:
#         return "Thursday"
#     elif x == 6:
#         return "Saturday"
# print(return_day(1))
# print(return_day(2))
# print(return_day(3))
# print(return_day(4))
# print(return_day(5))
# print(return_day(6))
# print(return_day(41))

# 8
# def element(x):
#     for i in x[-1:]:
#         return i
# print(element([1, 2, 3]))
# print(element([]))

# 9
# def number_compare(x, y):
#     if x == y:
#         return "Numbers are equal"
#     elif x > y:
#         return "First is greater"
#     elif x < y:
#         return "Second is grearer"
# print(number_compare(1, 1))
# print(number_compare(1, 0))
# print(number_compare(2, 4))

# 10
# def single_letter_count(x, y):
#     if not y in x.lower():
#         return 0
#     else:
#         return list(x.lower()).index(y) + 1
# print(single_letter_count("Hello world", "h"))
# print(single_letter_count("Hello world", "z"))
# print(single_letter_count("Hello world", "l"))

# # 11
# def multiple_letter_count(x):
#     return {a:x.count(a) for a in sorted(x)}
# print(multiple_letter_count("awesome"))

# 12
# def list_manipulation(w, x, y, z):
#     if x == "remove":
#         if y == "begining":
#             return w[0]
#         elif y == "end":
#             return w[-1]
#     elif x in "add":
#         if y == "begining":
#             w.insert(0, z)
#             return w
#         elif y == "end":
#             w.append(z)
#             return w
# print(list_manipulation([1, 2, 3], "remove", "end", 0))
# print(list_manipulation([1, 2, 3], "remove", "begining", 0))
# print(list_manipulation([1, 2, 3], "add", "begining", "20"))
# print(list_manipulation([1, 2, 3], "add", "end", "30"))

# 13
# def is_palindrome(x):
#     i = [i for i in list(x) if i != " "]
#     return i == i[-1::-1]
# print(is_palindrome("testing"))
# print(is_palindrome("tacocat"))
# print(is_palindrome("hannah"))
# print(is_palindrome("amanaplanacanalpanama"))
# print(is_palindrome("a man a plan a canal panama"))

# 14
# def frequency(x, y):
#     return x.count(y)
# print(frequency([1, 2, 3, 4, 4, 4], 4))
# print(frequency([True, False, True, True], False))

# 15
# def muliple_even_number(numbers):
#     i = 1
#     for x in numbers:
#         if x % 2 ==0:
#             i *= x
#         else :
#             pass
#     return i 
# print(muliple_even_number([2, 3, 4, 5, 6]))

# 16
# def capitalize(x):
#     return (x[0].upper()) + x[1:]
# print(capitalize("jamaika"))
# print(capitalize("chicken"))
# print(capitalize("tim"))
# print(capitalize("matt"))

# 17 
# def compact(x):
#     a = [i for i in x if i]
#     return a
# print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))

# 18
# def intersection(x, y):
#     i = [i for i in y if i in x]
#     return i
# print(intersection([1, 2, 3], [2, 3, 4]))
# print(intersection(["a", "b", "z"],["x", "y", "z"]))

# 19
# def partition(x, y):
#     if y == "isEven":
#         e = []
#         o = []
#         for i in x:
#             if i % 2 == 0:
#                 e.append(i)
#             elif i % 2 != 0:
#                 o.append(i)
#         return [e, o]        
#     elif y == "isOdd":
#         e = []
#         o = []
#         for i in x:
#             if i % 2 == 0:
#                 e.append(i)
#             elif i % 2 != 0:
#                 o.append(i)
#         return [o, e]
# print(partition([1, 2, 3, 4], 'isEven'))

# function advance
# 1
# def contain_purple(x):
#     if "purple" in x:
#         return True
#     else:
#         return False
# print(contain_purple([25, "purple"]))
# print(contain_purple(["green", False, "blue", "hello world"]))
# print(contain_purple("purple"))
# print(contain_purple(["a", 99, "blah blah blah", 1, True, False, "purple"]))
# print(contain_purple([1, 2, 3]))

# 2
# def combine_world(x, **kwargs):
#     if not kwargs:
#         return x
#     elif "prefix" in kwargs:
#         return kwargs["prefix"] + x
#     elif "suffix" in kwargs:
#         return x + kwargs["suffix"]
# print(combine_world("child"))
# print(combine_world("child", prefix="man"))
# print(combine_world("child", suffix="ish"))
# print(combine_world("work", suffix="er"))
# print(combine_world("work", prefix="home"))

# 3 不會
# def count_sevens(*args):
#     return args.count(7)
# num = [90, 1, 35, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, 46, 57, 68, 79, 12, 23, 34, 55, 1, 90, 454, 34, 76, 8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,77,345,23,54,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,7]
# result1 = count_sevens(1, 4, 7)
# result2 = count_sevens(tuple(num))
# print(result1)
# print(result2)

# 4
# def calculate(**kwargs):
#     if kwargs["make_float"] == True:
#         if kwargs["operation"] == "add":
#              return float(kwargs["first"] + kwargs["second"])
#         elif kwargs["operation"] == "divide":
#              return  float(kwargs["first"]/kwargs["second"])
#     elif kwargs["make_float"] == False:
#         if kwargs["operation"] == "add":
#              return int(kwargs["first"] + kwargs["second"])
#         elif kwargs["operation"] == "divide":
#              return int(kwargs["first"]/kwargs["second"])
# print(calculate(make_float=False, operation="add", messege="You just added", first=2, second=4))
# print(calculate(make_float=True, operation="divide", first=3.5, second=5))



















# Module_hw
# 1
# import math #solution 1
# answer = math.sqrt(15129)
# print(answer)
# from math import sqrt #solution 2
# answer = sqrt(15129)
# print(answer)

# 2
# import keyword
# def contain_keyword(*args):
#     answer = ""
#     for x in args:
#         answer += str(keyword.iskeyword(x))
#     if "False" in answer:
#         i = False
#     else:
#         i = True
#     return i
# print(contain_keyword("hello", "gooebye"))
# print(contain_keyword("def", "haha", "lol", "chicken", "alaska"))
# print(contain_keyword("four", "for", "if"))
# print(contain_keyword("grizzly", "ignore", "return", "False"))

# # 3
# import helpers
# result = helpers.lucky_number()
# print(result)
