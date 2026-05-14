# Sets
# """

# 1. Unorderd (no indexing)
# 2. semi mutable (can add or remove but not change)
# 3. unique elements (no duplicate values)
# 4. Heterogeneous (can store different types of data)
# """

# a=[]
# b={}
# c= () #type conversion

# s=set() #empty set
# s={1,2,3,4,5}
# print(s)
# """

# Methods in set 
# """

# 1. add() 
# 2. update() 
# 3. remove() 
# 4. discard()  
# 5. pop() 
# 6. clear() 
# """

# 1.add() #For adding a single element in set.
# s={1,2,3,4,4,5,2,3,5}
# s.add(6)

# 2.update() #For adding multiple elements in set.
# s.update([7,8,9])
# print(s)

# 3.remove() #If valure is not present in set then it will give error.
# s.remove(10)
# print(s)

# 4.discard() #If value is not present in set then it will not give error.
# s.discard(10)
# print(s)

# 5.pop() #It will remove a random element from set.
# print(s.pop()) #It will remove a random element from set.

# 6.clear() #It will remove all elements and give empty set.
# s.clear()
# print(s)


# """
# 1. Intersection- It will give common elements in both sets.
# 2. Union- It will give all unique elements in both sets.
# 3. Difference - It will give elements which are present in one set but not in other set.
# 4. Symmetric Difference- It will give elements which are present in one set but not in other set. (It will give all unique elements in both sets except common elements.)
# """

# s1={1,2,3,4,}
# s2={2,3,4,,6}
# print(s1.intersection(s2)) #It will give common elements in both sets.
# print(f"Intersection: {s1.intersection(s2)}"
# print(f"Union: {s1.union(s2)}")
# print(f"Difference s1: {s1.difference(s2)}")
# print(f"Difference s2: {s2.difference(s1)}")
# print(f"Symmetric Difference: {s1.symmetric_difference(s2)}")

# fs= {10,20,30,40,50}
# fs= frozenset(fs) #frozenset is a function
# fs.add(60)
# fs.remove(10) #It will give error because frozenset is immutable.
# print(fs)
# """
