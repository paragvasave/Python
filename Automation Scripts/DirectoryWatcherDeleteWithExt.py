# Directory name , extenstion name, delete

# **************************************************************************************************
# Please take precaution while using this application once the file is removed it cannot be restore*
# **************************************************************************************************

from sys import *
import os  

def DirectoryWatcher(path,Extension):
    print("")
    print("Deleted file list : ") 

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername,subfolder,filename in os.walk(path):
            for file in filename:
                if(file.endswith(Extension)):
                    os.remove(os.path.join(foldername,file))
                    print("File deleted : ",os.path.join(foldername,file))

    else:
        print("Invalid path.")

def main():
    print("--------------------Python Automation----------------------")
    print("Application name : ",argv[0])
    print("-----------------------------------------------------------")

    if(len(argv)!=3):
        print("Insufficicent arguments")
        print("Use -h for help or -u for usage.")
        exit()
    
    if((argv[1]=="-h")or(argv[1]=="-H")):
        print("This application is use to delete files with sepecific extension in specific directory.")
        exit()
    
    if((argv[1]=="-u")or(argv[1]=="-U")):
        print("Usage command : python Application_Name AbsolutePath_of_Directory Extension_Name")
        exit()
    
    try:
        DirectoryWatcher(argv[1],argv[2])
    
    except Exception as e:
        print("Error : ",e)

if __name__=="__main__":
    main()