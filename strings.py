# some_string = "abcdefghijkl"
# '''
# >>> some_string ='abcdef'
# >>> some_string[0]
# 'a'
# >>> len(some_string)
# 6
# >>> for i in range(len(some_string)):
# ...     print(some_string[]
#   File "<stdin>", line 2
#     print(some_string[]
#                       ^
# SyntaxError: invalid syntax
# >>> for i in range(len(some_string)):
# ...     print(some_string[])
#   File "<stdin>", line 2
#     print(some_string[])
#                       ^
# SyntaxError: invalid syntax
# >>> for i in range(len(some_string)):
# ...     print(some_string[i]
# ...
# ...
# ... )
# ...
# a
# b
# c
# d
# e
# f
# >>> some_string[2:6]
# 'cdef'
# >>> some_string[2:len(some_string):2]
# 'ce'
# >>> some_string[::2]
# 'ace'
# >>> some_string[:]
# 'abcdef'
# >>>
# >>> some_string[2:6]
# 'cdef'
# >>> some_string[2:len(some_string):2]
# 'ce'
# >>> some_string[::2]
# 'ace'
# >>> some_string[:]
# 'abcdef'
# >>> some_string[::-1]
# 'fedcba'
# >>> some_string[-1]
# 'f'
# >>> some_string
# 'abcdef'
# >>> some_string[:4]
# 'abcd'
# >>> some_string[-1:]
# 'f'
# >>> some_string ='A' + some_string[1:]
# >>> some_string
# 'Abcdef'
# >>> 'cdef' in some_string
# True
# >>> 'cef' in some_string
# False
# >>> 'cef' not in some_string
# True
# >>> import string
# >>> string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# >>> string.ascii_uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# >>> string.ascii_uppercase[13]
# 'N'
# >>>
# '''
# for c in some_string[2:6]:
#     print(c)
#
# for i in range(len(some_string)-1,-1,-1):
#     print(some_string[i])
#
# some_string[::-1]
#
# #string are immutable
#
# some_string ='A' + some_string[1:]

# s = "This string contains relatively long words."
# first_word = s[0:4] #diff is number of characters 4-0 =4 chars
# second_word = s[5:11]
# third_word = s[12:20]

# def spaces(s):
# #find all spaces in a string
# '''print indices of spaces in string.'''
# for i in range(len(s)): #i was chosen bcoz we wanted the indexes
#     if s[i] == ' ':
#         print(i)
#
# for c in s:
#     if c =='':
#         ##what do we do here?

def mix(a,b):
    '''return the mix of a and b'''
    a_idx = 0
    b_idx = 0
    output = ''
    while a_idx < len(a) and b_idx < len(b):
        output += a[a_idx]
        output += b[b_idx]
        a_idx += 1
        b_idx += 1

    return(output)

#
# mix('abcd','ABCDEF')

def shuffle(a):
    ##split a string in half
    print(mix(a[:len(a)//2] , a[len(a)//2:]))

shuffle('abcdefg')

def unshuffle(a):
    return a[a::2] + a[1::2]

def remove(a,to_remove):
    output = ''
    for c in a:
        if c not in to_remove:
            output += c
    return c

remove('I am Sayak', 'a')

def keep(a,to_keep):
    output = ''
    for c in a:
        if c in to_keep:
            ouput += c
    return output
