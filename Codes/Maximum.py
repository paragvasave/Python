# Display largest number

def LargestNumber(iValue1,iValue2):
    if(iValue1>iValue2):
        return iValue1
    else:
        return iValue2

def main():
    print("Enter first number : ")
    iNo1 = input()
    print("Enter second number : ")
    iNo2 = input()

    iMax = LargestNumber(int(iNo1),int(iNo2))   
    print("Largest number is : ",iMax)

if __name__=="__main__":
    main()