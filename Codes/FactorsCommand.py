from sys import * 

def DisplayFactors(iNo):
    for i in range(1,int(iNo/2)+1,1):
        if((iNo%i)==0):
            print(i)

def main():
    print("Welcome to the application")
    print("Name of the application : ",argv[0])

    if(len(argv)==2):
        if(argv[1]=="--U"):
            print("Usage : python File_Name Any_Number")
            exit()
        if(argv[1]=="--H"):
            print("Help : This applcation is use to show factors of provided number. ")
            exit()
        
    if(len(argv)!=2):
        print("Invalid argument.")
        print("Use --U flag for Usages, --H for Help.")
        exit()
    
    DisplayFactors(int(argv[1]))

if __name__ == "__main__":
    main()