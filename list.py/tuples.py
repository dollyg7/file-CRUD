# """
# #Tuples 
# 1.Tuples are ordered(indexing)
# 2.Can have duplicate 
# 3.Are Heterogeneous
# 4.Immutable
# """

# #t = () #Empty Tuple
# t = (1,2,3,4,5)

# Direct Loop
# for i in t:
#     print(i)

# Index Loop
# for i in range(len(t)):
#     print(i,t[i])
# """

# for index , value in enumerate(t):
#     print(index,value)

# """
# t = (1,2,3,4,5)

# print(t[2])
# print(t[1:4])

# """

# Methods in Tuples
# 1.count() -> we can count occurence of a value.
# 2.index()
# """
# t=(1,2,2,2,3,4,5,3,4)
# print(t.count(1))
# print(t.count(3))

# print(t.index(1))
# print(t.index(2))

# t=(1,2,2,2,3,4,5,3,4)
# """
# print(3 in t)
# print(9 in t)
# """

# """#Tuple UNpacking
# t=(1,2,3,4,5)
# a,b,c,d,e=t #Unpacking
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a= 1,2 #Packing"""

# #Star Expression(*)
# t= (1,2,3,4,5)
# a,*b,c = t
# a,*b = t
# print(a)
# print(b) # Middle Value Extraction
# print(c)"""

# t= (1,2,3,4,5)
# a,*_,c = t
# print(a)
# print(*_)
# print(c)

# t1 = (1,2,3)
# t2 = (4,5,6)
# print(t1+t2)

