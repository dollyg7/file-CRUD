#Project - CRUD Operations

from pathlib import Path
def readfileandfolder():
        try:
            p = Path('')
            items = list(p.rglob('*'))
            for index , file in enumerate(items):
                print(f'{index+1} - {file}')
        except Exception as e:
            print(e)
        pass


def create_file():
    try:
        readfileandfolder()
        # C:\Users\tanis\Desktop\File Handling\hello.txt
        file_name = input('Enter name of your file: ')
        p = Path(file_name)
        if p.exists():
            print('FILE ALREADY EXISTS')
        else:
            with open(file_name,'w') as file:
             content = input('Enter your file content: ')
             file.write(content)
             print('FILE ADDED!')

def read_file():
    readfileandfolder()
    file_name = input('Enter name of your file: ')
    p = Path(file_name)
    if p.exists():
        with open(file_name,'r') as file:
            print(file.read())
    else:
        print('FILE NOT FOUND!')



def update_file():
    try:
        readfileandfolder()
        file_name = input('Enter name of your file:')
        p=Path(file_name)
        if p.exists():
            print('Press 1 to overwrite the content')
            print('Press 2 to append new content')

            option = int(input('Enter your choice for updating a file:'))
            if option == 1:
                with open(file_name,'w')as file:
                     content = input('Enter your content:')
                     file.write(content)
                     print('CONTENT CHANGED...')


            elif option == 2:
                with open(file_name,'a')as file:
                     content = input('Enter your content:')
                     file.write(content)
                     print('CONTENT CHANGED...')
 
            else:
                print("INVALID INPUT")
    
        else:
            print('FILE DOES NOT EXISTS!!')

    except Exception as e:
        print(e)




def delete_file():
    readfileandfolder()
    file_name = input('Enter name of your file:')
    p = Path(file_name)
    if p.exists():
        os.remove(p) #OS is removing path of that file completelt fromthe system.
        print("FILE DELETED")
    else:
        print('FILE DOES NOT EXISTS!!')
    







while True:
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")

    option = int(input("Enter your choice: "))
    if option ==1:
      create_file()
    
    if option ==2:
       read_file() 

    if option ==3:
       update_file()

    if option ==4:
       delete_file()

    if option ==0:
       break