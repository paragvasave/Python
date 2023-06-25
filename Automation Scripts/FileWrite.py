import os

def Write_File(FileName):
    if(os.path.exists(FileName)):
        print("Enter the data that you want to write in the file : ")
        Data = input()

        fd = open(FileName,"a")     #open the file in append mode to write at theend of the file

        fd.write(Data)          # write the Data in file, fd = handle(file descriptor)
    
    else:
        print("File doesn't exist.")
        return

def main():
    print("Enter file name : ",end=" ")
    Name = input()

    Write_File(Name)
    

if __name__=="__main__":
    main()
