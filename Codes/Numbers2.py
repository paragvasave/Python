
class Numbers:
    def __init__(self):
        self.Arr = list()
        self.Size = 0

    def Accept(self):
        print("Enter the size of List :",end=" ")
        self.Size = int(input())

        for iCnt in range(0,self.Size,1):
            print("Enter element : ",iCnt+1," : ",end=" ")
            Value=int(input())
            self.Arr.append(Value)
    
    def Display(self):
        print("Elements of the list are : ",end=" ")
        for no in self.Arr:
            print(no,"\t",end=" ")
        print("")

    def Summation(self):
        Sum = 0
        for no in self.Arr:
            Sum = Sum+no
        
        return Sum

def main():

    obj1=Numbers()
    obj1.Accept()
    obj1.Display()

    Ret = obj1.Summation()
    print("Summation of all the elements is : ",Ret)

if __name__=="__main__":
    main()