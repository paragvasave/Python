
def CreateFile(FileName):
    fd = open(FileName,"w")

def main():
    print("Enter file name : ",end=" ")
    Name = input()

    CreateFile(Name)

if __name__=="__main__":
    main()