import os

def Delete_File(FileName):
    if(os.path.exists(FileName)):
        FileSize=os.path.getsize(FileName)

        if(FileSize==0):
            os.remove(FileName)
            print("File deleted.")
        else:
            print("Note : File is not empty. Confirm Y/N to delete.")
            Option =input()
            if(Option=="y")or(Option=="Y"):
                os.remove(FileName)
                print("File deleted.")
            else:
                print("Delete operation terminated.")
                return 
    else:
        print("File doesn't exists.")
        return

def main():
    print("Enter the file name to delete :")
    Name=input()

    Delete_File(Name)

if __name__=="__main__":
    main()

