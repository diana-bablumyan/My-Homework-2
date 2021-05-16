import os

path = os.getcwd()
if not 'New dir' in os.listdir():
    os.makedirs("New dir/Dir1/Dir2")
    os.makedirs("New dir/Dir1/Dir3/Dir4")
    os.chdir("New dir")
    with open('File.txt', 'w') as fp:
        pass
elif 'New dir' in os.listdir():
    os.chdir("New dir")
    if not "Dir1" in os.listdir():
        os.makedirs("Dir1/Dir2")
        os.makedirs("Dir1/Dir3/Dir4")
    if not 'File.txt' in os.listdir():
        with open('File.txt', 'w') as fp:
            pass
    else:
        os.chdir("Dir1")
        if not "Dir2" in os.listdir():
            os.mkdir('Dir2')
        if not 'Dir3' in os.listdir():
            os.makedirs('Dir3/Dir4')
        if 'Dir3' in os.listdir():
            os.chdir('Dir3')
            os.listdir()
            if not 'Dir4' in os.listdir():
                os.mkdir('Dir4')

print("Creation of folders are done!!!")

os.chdir(path)
os.chdir('New dir/Dir1')

answer = input("All folders and file are created already!Do you want to delete any of them? (yes/no) ")
if answer.lower() == 'yes':
    answer = input("Please, input the name of file or folders, which you want to delete. If you choose not empty folder, it will be delete anyway! And if you choose nothing, will be deleted New dir folder! ")
    if answer.lower() == 'dir2':
        os.rmdir('Dir2')
        print("Dir2 is deleted")
    elif answer.lower() == 'dir3':
        os.chdir('Dir3')
        os.rmdir('Dir4')
        os.chdir('..')
        os.rmdir('Dir3')
        print("Dir3 is deleted")
    elif answer.lower() == 'dir4':
        os.chdir('Dir3')
        os.rmdir('Dir4')
        print("Dir4 is deleted")
    elif answer.lower() == "dir1":
        os.chdir('Dir3')
        os.rmdir('Dir4')
        os.chdir('..')
        os.rmdir('Dir3')
        os.rmdir('Dir2')
        os.chdir('..')
        os.rmdir('Dir1')
        print("Dir1 is deleted")
    else:
        os.chdir('Dir3')
        os.rmdir('Dir4')
        os.chdir('..')
        os.rmdir('Dir3')
        os.rmdir('Dir2')
        os.chdir('..')
        os.rmdir('Dir1')
        os.remove("File.txt")
        os.chdir('..')
        os.rmdir("New dir")
        print("New dir is deleted")

