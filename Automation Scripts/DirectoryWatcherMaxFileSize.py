from sys import *
import os

def DirectoryWatcher(Dir_Name):
    print("Name of the input directory : ",Dir_Name)
    print("")

    MaxSize = 0
    MaxFilePath = ""

    for foldername, subfolder,filename in os.walk(Dir_Name):
        for file in filename:
            Size = os.path.getsize(os.path.join(foldername,file))
            if(MaxSize<Size):
                MaxSize=Size
                MaxFilePath=os.path.join(foldername,file)
    
    print("Largest File : "+MaxFilePath)
    print("File size : "+str(MaxSize)+" bytes.")
        
def main():

    print("---------------Python Automation-------------")
    print("Application name : ",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments.")
        print("Use -h for help or -u for usage")
        exit()
    
    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("Help : This application is use to traverse specific directory and search for file having largest size.")
        exit()
    
    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : python ApplicationName AbsolutePath_og_Directory.")
        exit()

    DirectoryWatcher(argv[1])

if __name__=="__main__":
    main()