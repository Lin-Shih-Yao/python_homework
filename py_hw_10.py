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

# 17 不會
# def compact(x):
#     i = [i for i in x if i != 0 or i is True or i != "" or i != [] or i !={} or i == "All done"] 
#     return i
# print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))

# 18
# def intersection(x, y):
#     i = [i for i in y if i in x]
#     return i
# print(intersection([1, 2, 3], [2, 3, 4]))
# print(intersection(["a", "b", "z"],["x", "y", "z"]))












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
