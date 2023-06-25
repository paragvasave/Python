from sys import *

def Addition(iNo1,iNo2):
    Ans = 0
    Ans = iNo1+iNo2
    return Ans

def main():
    print("Welcome to : ",argv[0])

    if(len(argv)==2):
        if(argv[1] == "--U"):
            print("Use the application as : ")
            print("python Name_of_Application First_Number Second_Number")
            exit()
            
        if(argv[1]== "--H"):
            print("Help : This application is used to perform addition of 2 numbers.")
            exit()

    if(len(argv) != 3):
        print("Invalid number of arguments.")
        print("Please use --U flag to get the usage.")
        print("Please use --H flag for help")
        exit()
    
    Ret = Addition(int(argv[1]),int(argv[2]))
    print("Addition is : ",Ret)

    print("Thank you for using the application.")

if __name__=="__main__":
    main()