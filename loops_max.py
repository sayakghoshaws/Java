# some examples of loops
# val = int(input("Enter a value: "))
# while val > 0:
#       # remember, we have to change 'val' in order for the loop to stop
#       # you can always stop code in an infinite loop by typing ctrl-c
#     val = val - 1
#     print(val, "is greater than zero")

# temperature conversion
# deg_f = 40
# while deg_f < 100:
#     deg_c = (deg_f - 32) * (5/9)
#     print(deg_f, 'f is', deg_c, 'c')
#     deg_f = deg_f + 5
#     # deg_f += 5 # <-- this is the same as above: it increments deg_f by 5

# range(stop)
# range(start, stop)
# range(start, stop, step)
# for deg_f in range(40, 101, 5):
#     deg_c = (deg_f - 32) * (5/9)
#     print(deg_f, 'f is', deg_c, 'c')

# random numbers!
# this chooses a random value 10 <= x <= 20
# import random
# x = random.randint(10, 20)
# print(x)

# a deliberately bad seeming loop, and a way to fix it!
# this seems like an infinite loop, until you consider the break statement
# break statements end a loop immediately
# the real reason we do this is because we want the code in the loop to run
# at least once
# while True:
#     s = input('Enter the number 5: ')
#     if s == '5':
#         break
#     else:
#         print("That's not 5.")
# print('hooray!  you entered 5. good job.')

# a while-true loop is better than the following attempt, which does the same
# thing.  the problem is that the variable 's' must be defined before we use
# it in the while-loop's conditional statement.  this involves repeating code,
# which is bad practice.
# s = input('Enter the number 6: ')
# while s != '6':
#     s = input('Enter the number 6: ')

# using a for-loop
# MAX_ATTEMPTS = 6
# for attempt in range(1, MAX_ATTEMPTS+1):
#     s = input('Enter the number 5: ')
#     if s == '5':
#         print('hooray!  you entered 5. good job.')
#         break
#     else:
#         print("That's not 5.")
# else: # this means the loop ended without a break statement
#     print("i give up.  you're useless.")
# print('attempts: ', attempt)

# last notes:
# this causes a NameError because there are no values for i; the range is empty
# for i in range(0, 0):
#     pass
# print(i)

# after the for-loop, i contains the last value it was assigned.  in this case,
# the last value was 9.
# for i in range(0, 10):
#     pass
# print(i)

# the continue statement skips to the next iteration.  for example, this skips
# printing 4, since the continue ends that iteration early.
# for i in range(0, 10):
#     if i == 4:
#         continue
#     print(i)
