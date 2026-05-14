#List 

# List = [] (Square Brackets)
# 1.Can have multiple data types(int,float,str,bool).
# 2.Can have duplicate values.
# 3.List have a unique thing that is known as indexing.
# 4.You can change the values of list as it is mutable.


#Indexing starts with 0 and goes to len = 1

# age = [] #Empty List
# #   0 1 2
# age = [21,22,23] #List of integers
# print(age[2])


# l = [1,2,3,4,5,6,7]
# l[3] = 18
# print(l)

# Slicing 
# Start_index:S_index:Step_skip:Step_skip
# Step(by_default=+1)
# Start(by_default=0)



# 0 1 2 3 4
#l = [1,2,3,4,5]
#print(l[1:4:])



# Iterating on List
# 1. Direct Loop -> Items ko print krte ho
# 2. Index Loop -> Values ke index ko print krte ho



#Direct Loop
#l = [1,2,3,4,5]
#for i in l:
#    print(i)

#Index Loop
#for i in range(len(l)):
 #   print(i,l[i]) #index , values




# METHODS IN list
# 1. append()
# 2. extend()
# 3. insert()
# 4. pop()
# 5. remove()
# 6. clear

# l.append(6)
# print(l)


# l = [1,2,3,4,5]
# l1 = [6,7,8]
# #print(l+l1)
# l.extend(l1)
# print(l)

# l=[1,2,3,4,5]
# l.insert(2,100)
# print(l)


# l=[1,2,3,4,5]
# l.pop(2)
# print(l)

# l=[1,2,3,4,5]
# l.remove(5)
# print(l)

# l=[1,2,3,4,5]
# l.clear()
# print(l)




#Rotate a list by k elements.

# l=[10,20,30,40,50]
# k = 2
def rotate_elements(l,k):
#   for i in range(k):
#       last = l[len(l)-1]

#       for j in range(len(l)-1,0,-1):

#           l[j] =  l[j-1]
#       l[0] = last 
    return l
    print('hello')

l=[10,20,30,40,50]
k = 2    
print(rotate_elements(l,k))

# print(l)


#def (define)
def greet(gender): #Parameter -> Gender
    print(f"HELLO {gender}")

greet('female') # Arguments    


