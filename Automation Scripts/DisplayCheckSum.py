from sys import *
import os
import hashlib

def Hash_File(path,blocksize=1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buffer = fd.read(blocksize)

    while(len(buffer)>0):
        hasher.update(buffer)
        buffer = fd.read(blocksize)
    fd.close()
    return hasher.hexdigest()

def Display_CheckSum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)

    if exists ==True:
        for foldername,subfolder,filename in os.walk(path):
            for file in filename:
                path=os.path.join(foldername,file)
                hashcode = Hash_File(path)
                print("File name : "+file+" CheckSum : ",hashcode)
                
def main():
    print("--------Automation script to find checksum--------")
    print("Application name : ",argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if((argv[1]=="-u") or (argv[1]=="-U")):
        print("Usage: ApplicationName AbsolutePath_of_DirectoryExtension")
        exit()
    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help:This script is used to traverse specific directory and display checksum of file")
        exit()
    
    Display_CheckSum(argv[1])

if __name__=="__main__":
    main()