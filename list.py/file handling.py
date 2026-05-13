# File Handling 
# file = open('list.py')
# print(file.read())
# file.choose()

# """
# Modes 
# """
# w - write mode (Arar file created nahi hai toh create ho jayegi, agar purna data hai toh overwrite ho jayega.)
# a - append mode
# r - read mode
# x - create mode
# """

# file = open('Gangadhar.txt','w')
# file.write('This is Gangadhar file')
# file.close()

# file = open('Gangadhar.txt','w')
# file.write('This content is now overwritten')
# file.close()

# file = open('Gangadhar.txt','w')
# file.write('the content is added using a (append) mode')
# file.close()

# file = open('Gangadhar.txt','r')
# for i in file:
#     print(i)
# file.close()

#With statement
# with open('Gangadhar.txt','r')as file:
#      print(file.read())

# with open('Gangadhar.txt','w')as file:
#     file.write('content overwritten')
#     print('Done')

#Paths
# C:\Users\tanis\Desktop\New Folder\Saktiman.txt
# from pathlib import Path
# p = Path('Saktiman.txt') 
# if p.exists():
#      print('file exists')
# else:
#      print('file does not exist')