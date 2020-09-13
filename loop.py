# #some examples of loops
#  val = int(input('Enter a Value: '))
 # if val > 0:
 #     print(val,"is greater than zero")

# val = int(input('Enter a Value: '))
# while  val > 0:
#      val = val - 1
#      print(val,"is greater than zero")

#Temperature conversation

# deg_f = 32
# while deg_f < 100:
#     deg_c = (deg_f - 32) * 5/9
#     print (deg_f,'f is', deg_c,'c')
#     deg_f = deg_f + 5

# deg_f = 32
# for deg_f in range(32,100,5):
#     deg_c = (deg_f - 32) * 5/9
#     print (deg_f,'f is', deg_c,'c')

#random numbers chooses a number value 10<= x <= 20
# import random
# x =  random.randint(10,20)
# print(x)
#
# #deliberately bad seeming loop and a way to fix it,python's version of do while loop,with while you don't know how many times the loop will occur
# while True:
#     s = input('Enter the number 5: ')
#     if s == '5':
#         break   #ends the current loop
# print('Hooray you entered 5!')
#

# MAX_ATTEMPTS = 3
# for attempt in range(0,MAX_ATTEMPTS):
#     s = input('Enter the number 5: ')
#     if s == '5':
#         break   #ends the current loop
#     else:
#         print('you have' ,attempt,'attempts')
# print('Hooray you entered 5!')
#
# for i in range(0,0):  #empty range:)
#     pass
# print(i)
#
# for i in range(0,10):  #range is not inclusive
#     pass
# print(i)
r = int(input("Enter max range: "))
for i in range(0,r):
    if i == 4:
        continue
    print(i)
