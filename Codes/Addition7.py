
def Addition(Value1, Value2):
    Ans = Value1+Value2
    return Ans
    
def main():
    print("Enter first number : ")
    iNo1 = int(input())

    print("Enter second number : ")
    iNo2 = int(input())

    Sum = Addition(iNo1,iNo2)
    print("Addition is : ",Sum)

if __name__ =="__main__":
    main()