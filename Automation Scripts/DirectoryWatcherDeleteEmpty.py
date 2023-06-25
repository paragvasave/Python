# Delete the files which are empty

# **************************************************************************************************
# Please take precaution while using this application once the file is removed it cannot be restore*
# **************************************************************************************************

from sys import *
import os

def DirectoryWatcher(Dir_Name):
    print("Name of the input directory : ",Dir_Name)
    print("----------------------------------------------------------")

    Size = 0
    print("")
    print("*** Deleted file list *** ")
    for foldername, subfolder,filename in os.walk(Dir_Name):
        for file in filename:
            Size = os.path.getsize(os.path.join(foldername,file))
            if(Size==0):
                os.remove(os.path.join(foldername,file))
                print(os.path.join(foldername,file)) 
def main():

    print("-----------------------Python Automation------------------")
    print("Application name : ",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments.")
        print("Use -h for help or -u for usage")
        exit()
    
    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("Help : This application is use to traverse specific directory and delete empty files.")
        exit()
    
    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : python ApplicationName AbsolutePath_of_Directory")
        exit()

    DirectoryWatcher(argv[1])

if __name__=="__main__":
    main()