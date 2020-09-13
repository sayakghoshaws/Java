#for i in [1, 2, 1]:
#   for j in {1, 2, 1}:
#        print('A', end='')
#   print('B', end='')

################################
def f(x):
    if x <= 1:
        return 0
    else:
        return 1 + f(f(x - 1))
#print(f(6))
#ans 1
####################################
#dict
#################################
A = [- 2, -1, 0, 1, 2]
#print(A.pop(-1))
#print(A)
#Ans=[-2, -1, 0, 1]
################################
A = [3, 6, 9,  12]
A.insert(1,(4,5))
#print(A)
#ans [3, (4, 5), 6, 9, 12]

###########################
#print([n**2 for n in range(6) if n%2==0])
#ans [0, 4, 16]
#############################
fun = [list.pop, list.sort]
A = [3, 4, 5, 1, 2]
for f in fun: f(A)
#print(A)
############################
A = []
for i in range(2):
    B = []
    for j in range(2):
        B.append((i+j)%2 == 0)
    A.append(B)
#print(A)
# ans [[True, False], [False, True]]

############################
    def f(x):
        xs = str(x)
        if len(xs) == 1:
            return int(xs)
        n = int(xs[0])
        return n + f(xs[1:])
#print(f(1234))
# ans 10
###########################
A=[1,2,3,4,5]
B=A
B[1]=3
#print(A)
###########################
#print(list(range(8))[1:-1])
###########################
t = 3
#t[1] = 2
##########################
#set([1,2,3,4])
#set([[1,2],[3,4]]) #error
#set([(1,2),(3,4)])
#########################3
#t = 3, 4
#if t == 3:
#    print(3)
#elif t == 4:
#    print(4)
#elif t == (3, 4):
#    print(3, 4)
#else:
#    print('None')
#ans 3 4
#########################
#A = [1,2,3]
#B = A
#A.append(4)
#print(A)
#print(B)
##
#A = [1,2,3]
#B = A[:]
#A.append(4)
#print(A)
#print(B)
###########

def cmp(x, y, z):
    return x < y < z or z < y < x
#print(cmp(7,5,2))

#############
t=('abcd', 365 , 2.22 , 'pat' , 3.14)
#print(t[1:3])
#############

class adt:
    def __init__(self, s="i am an adt"):
        self.s = s

    def __str__(self):
        if len(self.s) > 0:
            return self.s
        else:
            return 'nothing yet'
obj = adt()
#print(obj)

#######################
n = 5
def f(x):
    n = n + x
    return n
#print(f(4))

class group:
    def __init__(self, x=0, y=0, z=0):
        self.a = x + y + z

x = group(3,2,3)
y = getattr(x, 'a')
setattr(x, 'a', y+1)
#print(x.a)

################
class myclass(object):
    def __init__(self,a):
        self.a=a
    def display(self):
        print(self.a)
obj=myclass(5)
#obj.display()
################
class myclass(object):
    def __init__(self,a):
        self.a=a

    def __str__(self):
        return self.a
x = myclass('x')
y = x
del x
#print(y)

############
num = '12'
den = '12'
val = 6
try:
    val = num // len(den)
except:
    val = 0
#print(val)
##########################
num = 6
den = 2
val = 1
try:
  val = num // den
except:
  val = 0
else:
 val = 2
#print(val)
##################
print(3 < '3')




