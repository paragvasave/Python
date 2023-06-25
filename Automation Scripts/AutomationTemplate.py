
from sys import *

def CheckEven(No):
    if(No%2==0):
        print("{} is even number.".format(No))
    else:
        print("{} is odd number.".format(No))


def main():
    print("------------------ Automation script ------------")

    print("Name of the script : ",argv[0])

    if(len(argv)!=2):
        print("Error : Insufficient arguments.")
        print("Use -h for help or -u for usage")
        exit()
    
    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help : This script is use for _______")
        exit()
    
    if((argv[1]=="-") or (argv[1]=="-U")):
        print("Usage : File_Name.py argument")
        exit()
    
    else:
        CheckEven(int(argv[1]))

if __name__=="__main__":
    main()