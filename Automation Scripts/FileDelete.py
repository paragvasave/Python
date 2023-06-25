import os

def Delete_File(FileName):
    if(os.path.exists(FileName)):
        os.remove(FileName)
        print("File deleted.")
    else:
        print("File doesn't exists.")
        return

def main():
    print("Enter the file name to delete :")
    Name=input()

    Delete_File(Name)

if __name__=="__main__":
    main()

