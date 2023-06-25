from sys import *

def Addition(iNo1,iNo2):
    Ans = iNo1+iNo2
    return Ans

def main():
    if(len(argv)!=3):
        print("Invalid number of arguments.")
        exit()

    Sum=Addition(int(argv[1]),int(argv[2]))
    print("Addition is : ",Sum)

if __name__=="__main__":
    main()