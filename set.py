#set is a collection of objects
s = set() #mutable
s = frozenset() #immutable
##with stuff in them
s = {1,2,3,4,5}
s = frozenset({1,2,3,4,5})

#set comprehension produces a set ,three ways to declare set below
s = {abs(i) for i in range(-10,10)}
s = set(abs(i) for i in range(-10,10))
s = frozenset(abs(i) for i in range(-10,10))

#membership is tested in 'in'
if 10 in s:
    print(10,'is in',s)

if -1 not in s
    print(-1,'is not in',s)

## sets have union
A = {1,2,3}
B = {2,3,4}
##the ones that don't change A
print(A.union(B)) ## returns a new value containing union
print(A|B) # same as above
print(A |=B) # changes A

#intersection
print(A.intersection(B))
print(A&B)
print(A &= B)

#symmetric difference
##things in A or B but not BOTH
print(A^B)
A^=B #augumented forms

A<=B #a subset of b
A < B #All is a strict subset of B
A>= B #A is superset of B.
A>B #strict super set of B

for c in s:
    print(c)
