#how to declare a function
# def min1(a,b):
#
# val1 = min1(5,10)
# print (val1)

# def collatz_function(n):
#     if (n % 2 == 0): #checks for even/odd
#         return n//2
#     else:
#         return 3*n + 1
#
# def collatz_sequence(n):
#     while n != 1:
#         print(n,end='-->')
#         n = collatz_function(n)

# def function(a=5):
#     '''this is the documentation of my function'''
#     return a
# PI = 3.1415926
# def volume_sphere(radius):
#     return 4/3*PI*radius**3
# import random
# def roll_dice(faces):
#     return random.randint(1,faces)
#
# def sum_of_rolls(trials,faces = 6):
#     total = 0
#     for roll in range(trials):
#         total += roll_dice(faces)
#
# count = 0
# def counter():
#     global count #<--when you want to modify global variable
#     count += 1
#
# #single ,double and triple quote
# # s1 ='said "something
# '''you can write multiline
#     comments'''
# #escape chars
# tab ='\t'
# newline = '\n'
# single_quotes = '\''
# double_quotes = "\""
# slash = '\\'

## format strings allow us to print nicer

# guesses_left = 5
# prompt1 = "Guesses left: " + str(guesses_left)
# ##format method(...)
# prompt2 = "you have {} Guesses left: ".format(guesses_left)
# name = 'max'
# prompt3 = "{0} has {1} Guesses left: ".format(name,guesses_left)
# prompt4 = "{1} has {0} Guesses left: ".format(guesses_left,name)
# print(prompt3)
# print(prompt4)
# ##f-strings
# prompt = f"{name} has {guesses_left} guesses_left: "
# prompt11 = f"{{ }}{name} has {guesses_left} guesses_left: "
# print(prompt11)

# score = 700
# score_string1 = f"{score:06d}" #<--zero leading padding
# score_string2 = f"{score:6d}" #<--space leading padding
# score_string3 = f"{score:_d}" #<--space leading padding
# print(score_string3)
#
# #floating point numbers
# value = 100000000000000.32423141
# value = f"{value:,.2f}"
# print(value)
string ='title'
string1 =f"{string:#<10s}"
print(string1)
