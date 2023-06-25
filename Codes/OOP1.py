
class Maths:
    def __init__(self,A,B):
        self.iNo1 = A
        self.iNo2 = B

    def Add(self):
        return self.iNo1+self.iNo2
    
    def Sub(self):
        return self.iNo1-self.iNo2
        

def main():
    print("Enter first number :",end=" ")
    Value1 = int(input())

    print("Enter second number :",end=" ")
    Value2 = int(input())

    obj1 = Maths(Value1,Value2)
    Ret=obj1.Add()
    print("Addition is :",Ret)
    Ret = obj1.Sub()
    print("Subtraction is : ",Ret)


if __name__=="__main__":
    main()