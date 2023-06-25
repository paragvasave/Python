from sys import *
import os

def DirectoryWatcher(Dir_Name,File_Name):
    print("Name of the input directory : ",Dir_Name)
    print("")

    FilePath = ""

    for foldername, subfolder,filename in os.walk(Dir_Name):
        for file in filename:
            if(file==File_Name):
                FilePath=os.path.join(foldername,file)
                break
    if(FilePath==""):
        print("No such file found in the directory.")
    else:
        print("File inside folder : "+FilePath)


def main():

    print("---------------Python Automation-------------")
    print("Application name : ",argv[0])

    if(len(argv)!=3):
        print("Invalid number of arguments.")
        print("Use -h for help or -u for usage")
        exit()
    
    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("Help : This application is use to traverse specific directory for searching specific file.")
        exit()
    
    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : python ApplicationName AbsolutePath_of_Directory File_Name.ext")
        exit()

    DirectoryWatcher(argv[1],argv[2])

if __name__=="__main__":
    main()