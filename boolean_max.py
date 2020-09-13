# some conditionals
# 'True' and 'False' are constant boolean values
# if True:
#     print("this will print!")
# if False:
#     print("this will not print...")
# print("this will print regardless, it's separate from the ifs")

# actual comparisons.  remember, these are questions, not statements of truth
# this will print
# if 4 < 5:
#     print("yes, 4 < 5")
# # ... but this will not
# if 4 > 5:
#     print("4 < 5?")

# once we involve variable names, things get more interesting
# chairs_in_room = 60
# # note: input(...) gets a string from the user, we must typecast it to an int
# students_registered = int(input("Enter students registered: "))
# students_auditing = int(input("Enter students auditing: "))
# if (students_registered + students_auditing) > chairs_in_room:
#     print("there's not enough room...")
# else:
#     print("there's enough room for everyone!")

# try to determine if the user has entered a valid color
# first approach: the WRONG WAY

# color = input("(1) Enter a color: ")
# if color == "red":
#     print("i recognize red!")
# if color == "blue":
#     print("i recognize blue!")
# if color == "green":
#     print("i recognize green!")
# else:
#     # note: this else is attached to the if-statement checking for green...
#     #       for example, entering 'red' passes the first if-statement, fails
#     #       the blue-statement, and fails the green-statement
#     print("i don't recognize that color...")

# second approach: correct, but unwieldy
# the problem here is that we have too many indentations, and it's just hard to
# read...
# color = input("(2) Enter a color: ")
# if color == "red":
#     # color is red, recognized
#     print("i recognize red!")
# else:
#     # otherwise it's not red...
#     if color == "blue":
#         # ... but it is blue! recognized.
#         print("i recognize blue!")
#     else:
#         # otherwise it's not red AND not blue...
#         if color == "green":
#             # ... but it is green! recognized.
#             print("i recognize green!")
#         else:
#             # otherwise, it's not red, blue, or green: unknown!
#             print("i don't recognize that color...")

# third approach: separates options into categories.  either red, blue, green,
#                 or unknown
color = input("(3) Enter a color: ")
if color == "red":
    print("i recognize red!")
elif color == "blue":
    print("i recognize blue!")
elif color == "green":
    print("i recognize green!")
else:
    print("i don't recognize that color...")

# any case resumes execution here...
print('regardless of the value of user input, this prints')
