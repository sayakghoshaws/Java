import math, random
a = 1
b = 2
c = 3
d = 4

print(a-b*9%d)

print(c%b)

sum = 10
sum *= 10

print(sum)

A = 3 > 5
B = 5 < 3
C = (not A or B) and (not B or A)

print(C)

L = [4,5,6]

print(L[-2])

s = "No More"
print(s.ljust(9))

print(len(str(5 * 2) + "10"))

a = 1
b = 2
c = 3
a = b = c
print(c-a+b)

X = {}

print(type(X))

a = chr(60)
b = str(60)
c = int(True)
d = int("21")

print(d)

s = "TaUbVcWdXeYfZ"
p = ""
for i in range(0, len(s), 2):
    p += s[i]
print(p)


s = 0
for i in range(2,8):
    if i%3 == 0:
        print(i,end=" ")
    else:
        s += i
print(s)

x = "bitter"
y = "sweet"
print(x + (" " + y) * 2)

x= 2
n = 5
z = [2**x for x in range(1,n+1)]

print(z)


print(math.sqrt(2.0)*math.sqrt(2.0) == 2.0)

print((math.sqrt(2.0))**2)

A = set([1, 1, 2, 3, 3, 3, 4])
print(len(A))

def g(x):
    if x == 1:
        return 1
    else:
        return 2*g(x//2)

print(g(8))

x= 3.0

if x<=3:
   print("option 1")
elif x>3:
   print("option 2")
else:
   print("option 3")

x = int(47.6)

print(x)

for i in range(6):
        if i == 4:
            break
        if i in {1,2,1}:
            print("A",end="")
        print("B",end="")

print("sayak")
s = "ABCDEFG"
s = s[3:] + s[:3]

print(s)

a = {"dog": 10, "cat": 8, "bird": 1}

a[10] = "pig"

print(a)

r = random.random()
print(r)

A = [1, 2, 3]
B = A
print(A)
print(B)
B[0] = 4
print(A)
print(B)
print(A == B)

d = 1
e = 2
d = e
e = 3
print(d)