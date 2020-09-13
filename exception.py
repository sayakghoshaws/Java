#exception handling
# lo=1
# # hi=100
# valid_int =[i for i in range(1,101)]
# while True:
#     try:
#         val =int(input(f"Enter an Integer between 0 and 100: "))
#         if val in valid_int:
#             break
#         else:
#             print("invalid range")
#     except ValueError:
#         print("that wasn't an integer")

###multiple except
# lst=[1,2,3,4,5]
# while True:
#     try:
#         idx =int(input(f"Enter an Integer idx "))
#         # if -len(lst) <= idx <= len(lst) - 1:
#         val =lst[idx]
#         print(val)
#         break
#     except ValueError:
#         print("that wasn't an integer")
#     except IndexError:
#         print("that wasn't a valid index")
#
# def print_integer_lines(filename):
#     with open (filename,mode='r') as f:
#         for line in f:
#             try:
#                 print(int(line))
#             except ValueError:
#                 pass

# 2
# 3
# 4
# try:
#     print_integer_lines(exception.py)
# except:
#     print('something not right check arg')

##raising errors instead of catching
# raise ValueError
# raise TypeError
# raise Exception

#can specify more information


# try:
#     raise ValueError('5 not valid')
# except ValueError as ve:
#     msg =str(ve)
#     print('error ',ve)

# #lets write our minimum function
# def min(lst):
#   if len(lst) == 0
#     raise ValueError('an empty list has no minimum')
#   m = lst[0]
#   for element in lst:
#       if element < m:
#           m = element
#     return m
#
# #way to create your own exceptions
# class MyCustomError (Exception):
#     pass

def add_lists(l1,l2):
    if len(l1) != len(l2):
        raise ValueError("Can't add list of different lengths")
    else:
        return [l1[i]+l2[i] for i in range(len(l1))]

def smallest_nn(s):
    nn= None   #None is python's version to null
    for element in s:
        if element >=0:
            if nn== None or element < nn:
                nn = element
    if nn == None:
        raise ValueError('no non-negetive elements in this set')
    else:
        return nn


# print(add_lists([1,2,3],[4,5,6]))
# print(smallest_nn([2,3]))


def sum(lst):
    s = 0
    try:
        for idx,element in enumerate(lst):
            s += element

    except:
            raise TypeError(f'improper type at index {idx}')

    return s

print(sum([1,'s']))
