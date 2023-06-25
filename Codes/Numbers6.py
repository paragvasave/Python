class Numbers:
    def __init__(self):
        self.List=list()
        self.Size=0
        self.Accept()
    
    def Accept(self):
        print("Enter the size of list : ",end=" ")
        self.Size=int(input())
        for i in range(0,self.Size,1):
            print("Enter element : ",i+1," : ",end=" ")
            Value=int(input())
            self.List.append(Value)
    
    def Display(self):
        print("Elements of list are : ",end=" ")
        for i in range(0,self.Size,1):
            print(self.List[i],end=" ")
        print("")
    
    def Summation(self):
        Sum = 0
        for i in self.List:
            Sum = Sum+i
        return Sum
    
    def Average(self):
        Sum=0
        for i in range(0,self.Size,1):
            Sum = Sum+self.List[i]
        
        return Sum/self.Size
    
    def Maximum(self):
        iMax=self.List[0]
        for i in range(0,self.Size,1):
            if(iMax<self.List[i]):
                iMax = self.List[i]

        return iMax
    
    def Minimum(self):
        iMin=self.List[0]
        for i in range(0,self.Size,1):
            if(iMin>self.List[i]):
                iMin = self.List[i]

        return iMin


def main():
    obj1 = Numbers()
    obj1.Display()

    Ret = obj1.Summation()
    print("Summation of all the elements is : ",Ret)
    Ret = obj1.Average()
    print("Average of all the elements is : ",Ret)

    Ret = obj1.Maximum()
    print("Largest element is : ",Ret)

    Ret = obj1.Minimum()
    print("Smallest element is : ",Ret)
    

if __name__=="__main__":
    main()