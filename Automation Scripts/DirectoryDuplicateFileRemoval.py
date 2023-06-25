from sys import * 
import os
import hashlib
import time

def Delete_Files(dict1):
    results = list(filter(lambda x : len(x)>1,dict1.values()))

    iCnt = 0
    if len(results)>0:
        for result  in results:
            for subresult in result:
                iCnt+=1
                if iCnt>=2:
                    os.remove(subresult)
                    print("Duplicate file removed : ",subresult)
            iCnt = 0
    else:
        print("No duplicate files found.")
    
def Hash_File(path,blocksize=1024):
    fd = open(path,"rb")
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

    dups = {}

    if exists:
        for foldername, subfolder, filename in os.walk(path):
            for file in filename:
                path = os.path.join(foldername,file)
                Hash_Code = Hash_File(path)

                if Hash_Code in dups:
                    dups[Hash_Code].append(path)
                else:
                    dups[Hash_Code]=[path]
        return dups
    else:
        print("Invalid path")
    

def Print_Results(dict2):
    results = list(filter(lambda x : len(x)>1,dict2.values()))

    if len(results)>0:
        print("Duplicate found : ")
        print("The following files are duplicate : ")
        for result in results:
            for subresult in result:
                print("\t\t %s" % subresult)
    else:
        print("No duplicate files found")


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
        print("Help:This script is used to traverse specific directory and deleteduplicate file comparing checksum.")
        exit()

    try:
        Arr = {}
        startTime = time.time()
        Arr = Find_Duplicate(argv[1])
        Print_Results(Arr)
        Delete_Files(Arr)
        endTime = time.time()

        print("Took %s second to evaluate." %(endTime - startTime))
    
    except Exception as E:
        print("Error : Invalid input : ",E )
    
if __name__=="__main__":
    main()