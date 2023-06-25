from sys import *
import os

def DirectoryWatcher(Dir_Name):
    print("Inside directory watcher method")
    print("Name of the input directory : ",Dir_Name)

    for foldername, subfolder,filename in os.walk(Dir_Name):
        print("Folder name : "+foldername)

        for subf in subfolder:
            print("Subfolder name of : "+foldername+" is : "+subf)
        
        for file in filename:
            print("File inside folder "+foldername+ " is "+file+" : Size : ",os.path.getsize(os.path.join(foldername,file)))
        
        print("")
        
def main():

    print("---------------Python Automation-------------")
    print("Application name : ",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments.")
        print("Use -h for help or -u for usage")
        exit()
    
    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("Help : This application is use to traverse specific directory to show file with size.")
        exit()
    
    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage : python ApplicationName AbsolutePath_og_Directory.")
        exit()

    DirectoryWatcher(argv[1])

if __name__=="__main__":
    main()