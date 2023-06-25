import os

def Read_File(FileName):
    if(os.path.exists(FileName)):
        fd = open(FileName,"r")

        Data = fd.read()
        print("Data from the file : ")
        print(Data)

        fd.close()
    else:
        return

def main():

    print("Enter file name : ",end=" ")
    Name= input()

    Read_File(Name)

if __name__=="__main__":
    main()