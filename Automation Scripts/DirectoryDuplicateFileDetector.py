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

def Find_Duplicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exists = os.path.isdir(path)
    Result={}

    if exists ==True:
        for foldername,subfolder,filename in os.walk(path):
            for file in filename:
                path=os.path.join(foldername,file)
                hashcode = Hash_File(path)
                if hashcode in Result:
                    Result[hashcode].append(path)
                else:
                    Result[hashcode]=[path]
        return Result
    else:
        print("Invalid path")


def PrintDuplicate(Data):
    results = list(filter(lambda x:len(x)>1,Data.values()))
    if len(results)>0:
        print("Duplicate found : ")
        print("The following files are identical.")

        iCnt = 0
        for result in results:
            for subresult in result:
                iCnt+=1
                if iCnt>=2:
                    print('\t\t%s' % subresult)
    else:
        print("No duplicate files found.")
    
def main():
    print("--------Automation script to find duplicate files--------")
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
    try:    
        Arr = {}
        Arr = Find_Duplicate(argv[1])
        PrintDuplicate(Arr)
    except Exception as e :
        print("Error : ",e)


if __name__=="__main__":
    main()