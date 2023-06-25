from sys import *
import os

def DirectoryWatcher(Dir_Name,Extension):
    print("Name of the input directory : ",Dir_Name)
    print("")

    for foldername, subfolder,filename in os.walk(Dir_Name):
        for file in filename:
            if(file.endswith(Extension)):
                print("File inside folder : "+foldername+" is "+file)
        print("")
        
def main():

    print("---------------Python Automation-------------")
    print("Application name : ",argv[0])

    if(len(argv)!=3):
        print("Invalid number of arguments.")
        print("Use -h for help or -u for usage")
        exit()
    
    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("Help : This application is use to traverse specific directory for searching files with specific extension .")
        exit()
    
    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : python ApplicationName AbsolutePath_of_Directory .txt")
        exit()

    DirectoryWatcher(argv[1],argv[2])

if __name__=="__main__":
    main()