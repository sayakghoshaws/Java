#recursion bad idea
# def f():
#     f()

#
def countdown(n):
    if n<=0:
        pass
    else:
        print(n)
        countdown(n-1)
lst=[1,2,'a','b']
def number_of_ints(lst):
    '''returns number of ints in a given list'''
    count =0
    for idx in range(lst):
        if type(lst[idx]) == int:
            count +=1
    return count

def number_of_ints_r(lst):
    #base case
    if len(lst) ==0
        return 0
    else:
        #recursive case tries to solve a problem by taking smaller version of same problem
        element = lst[0]
        number_of_ints_in_rest_of_list = number_of_ints_r(lst[1:])
        if type(element) == int:
            return number_of_ints_in_rest_of_list + 1
        else
            return number_of_ints_in_rest_of_list

#trickier problem
##count the number of int in all nested lists of a list
    lst =[1,2,3,[4,5,6,[7,8,9]]]

countdown(10)
