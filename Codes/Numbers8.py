class Numbers:
    def __init__(self):
        self.List=list()
        self.iSize = 0
        self.Accept()

    def Accept(self):
        print("Enter the size of List : ",end=" ")
        self.iSize = int(input())
        
        for i in range(0,self.iSize,1):
            print("Enter element : ",i+1," : ",end=" ")
            iValue=int(input())
            self.List.append(iValue)
    
    def Display(self):
        print("Elements of the list are : ",end=" ")
        for i in range(0,self.iSize,1):
            print(self.List[i],end=" ")
        print("")
    
    def Summation(self):
        Sum=0
        for i in self.List:
            Sum=Sum+i
        return Sum

    def Average(self):
        Sum=0
        for i in range(0,self.iSize,1):
            Sum = Sum+self.List[i]

        Ans = Sum/self.iSize
        return Ans
    
    def Maximum(self):
        Max=self.List[0]
        for i in range(0,self.iSize,1):
            if(self.List[i]>Max):
                Max=self.List[i]
        return Max

    def Minimum(self):
        Min=self.List[0]
        for i in range(0,self.iSize,1):
            if(self.List[i]<Min):
                Min=self.List[i]
        return Min
    
    def __CheckPrime(self,No):
        Flag = True
        for i in range(2,int(No/2)+1):
            if(No%i==0):
                Flag=False
                break
        return Flag

    def DisplayFactors(self):
        for i in range(0,self.iSize,1):
            if(self.__CheckPrime(self.List[i])==True):
                print("{} is a prime number".format(self.List[i]))
            else:
                print("{} is not a prime number".format(self.List[i]))


def main():
    obj1 = Numbers()
    obj1.Display()

    Ret = obj1.Summation()
    print("Summation of all the elements is : ",Ret)

    Ret = obj1.Average()
    print("Average of all the elements is : ",Ret)

    Ret = obj1.Maximum()
    print("Largest number of all the elements is : ",Ret)

    Ret = obj1.Minimum()
    print("Smallest number of all the elements is : ",Ret)

    obj1.DisplayFactors()

if __name__=="__main__":
    main()