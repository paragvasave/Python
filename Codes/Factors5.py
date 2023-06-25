
#import Numbers
#from Numbers import DisplayFactors
#from Numbers import *

import Numbers as NUM

def main():
    print("Enter a number : ")
    iNo = int(input())

    NUM.DisplayFactors(iNo)

if __name__=="__main__":
    main()