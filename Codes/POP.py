
def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def main():
    print("Enter first number : ")
    iNo1 = int(input()) 

    print("Enter second number : ")
    iNo2 = int(input())

    Ans = Add(iNo1,iNo2)
    print("Addition of the numbers is : ",Ans)

    Ans = Sub(iNo1,iNo2)
    print("Subtraction of the numbers is : ",Ans)

if __name__=="__main__":
    main()