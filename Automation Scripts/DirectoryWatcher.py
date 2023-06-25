#Command to run :python DirectoryWatcher.py "C:\Users\Rose\Desktop\Work\Drive programs\Python\Automation\A"

from sys import *
import os

def DirectoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    is_Dir = os.path.isdir(path)

    if is_Dir:
        for Folder_Name, Sub_Folder,File_Name in os.walk(path):
            print("[ Current folder ] : "+Folder_Name)
            for subfolder in Sub_Folder:
                print("[ Sub folder ] of "+Folder_Name+" is : "+subfolder)
            for filename in File_Name:
                print("File inside "+Folder_Name+" is : "+filename)
            print(' ')
    else:
        print("Invalid path")

def main():
    print("---------------Python Automation-------------")
    print("Application name : ",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments.")
        print("Use -h for help or -u for usage")
        exit()
    
    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("Help : This application is use to traverse specific directory.")
        exit()
    
    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : python ApplicationName AbsolutePath_og_Directory.")
        exit()

    try:
        DirectoryWatcher(argv[1])
    
    except ValueError:
        print("Error : Invalid datatype of inpt")
    
    except Exception as e:
        print("Error : ",e)

if __name__=="__main__":
    main()