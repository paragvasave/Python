import AdditionModule

def main():
    print("Value of __name__ from main is : ",__name__)
    
    print("Enter first number : ")
    iNo1 = int(input())

    print("Enter second number : ")
    iNo2 = int(input())

    Sum = AdditionModule.Addition(iNo1,iNo2)
    print("Addition is : ",Sum)

if __name__=="__main__":
    main()
    