# #sequences of characters
#
# a="abcdef"
#
# ##similarly we can have sequence of integers,Note its the sequence that matters!!!
# #in python we can extend lists at will
#
# numbers = [1,2,3,4,5]
# strings = ['this','is','a','list',
# 'of','words',[1,2],False]
#
# #nested list
# nested=[[1,2],[3,4]]
# print(nested[0][0]) #prints 1 multi dimentional list
#
# ##iterate over a list and print out each
#
# for i in range(0,len(nested)):
#     print(nested[i])
#
# for element in nested:
#     print(element)
#
# number = 12345  #any string variable is lists
#
# first_elements =[]
# for element in nested:
#     first_elements +=[element[0]]
# print("the first elements are:",first_elements)
#
# #list comprehension,a shorter way to do the previous!
# #[EXPRESSION for variable in collection]
# second_elements =[element[1] for element in  nested]
#
# ##squares of numbers
# squares =[i**2 for i in range(1,11)]
#
# ##split on strings,delimiter as spaces
# s ="abc,def".split(',')
# join(s)
#
# a = [1,2,3,4]
# b =a ##aliases a,b pointing to same values
#
# #when you call functions it only modifies the existing pointer values,lists are immutable
# ## a += [1] extends the existing set
# ##a = a + [1] creates a new copy
# # b = a[:] absolute seperate copy
#
# a = [1, 2]  ## 'a' points to [1, 2]
# b = [a, a]  ## 'b' contains two elements: each pointing at the value of 'a'
# a += [3]    ## 3 is added to the end of 'a', which also updates BOTH elements of 'b'
# print(b)    ## prints [[1, 2, 3], [1, 2, 3]]
#
#
# ##tuples are immutable
# ##empty tuple
# empty_tuples =()
# ## several elements
# larger_tuples =(1,2,3,4,5)
# larger_tuples =1,2,3,4,5
# single_tuple = 1,
# len(larger_tuples)
# larger_tuples[0]
# larger_tuples[1:4]
# #multiple assignments
# a,b,c = 1,2,3
#
# return =1,2
# val1,val2 = return_two_values()
#
#
# ##new for loop
# string =["hello",1,1.0]
# for index,value in enumerate(string):
#     print(index,value)
# #     0 h
# #     1 e
# #     2 l
# #     3 l

# a = (i for i in range(0,10))
# #print(a)
# print(next(a))
# print(next(a))
#
def words_of(s):
    print(s.split())
    return s.split()

# words_of("this is sentence")

# for word in words_of("this is a sentence"):
#     print(word)
#
# for word in "this,is,a,sentence".split(','):
#     print(word)

# def words_and_lengths_of(s):
#     return[((word),len(word)) for word in s.split()]  #list comprehension
#
# for p in words_and_lengths_of("this is a sentence"):
#     print(p)
#
# for word,length in words_and_lengths_of("this is a sentence"):
#     print(word,length)

for a,b,c in ((1,2,3),(2,3,5)):
    print(a,b,c)
