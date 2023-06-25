
class Numbers:
    def __init__(self):
        self.List = []
        self.Size = 0
    
    def Accept(self):
        print("Enter the size of List : ",end=" ")
        self.Size = int(input())

        for i in range(0,self.Size,1):
            print("Enter element : ",i+1," : ",end=" ")
            Value=int(input())
            self.List.append(Value)
    
    def Display(self):
        print("Elements of list are : ",end = " ")
        for i in range(0,self.Size,1):
            print(self.List[i],end=" ")
        print("")

    def Summation(self):
        Sum=0
        for i in range(0,self.Size,1):
            Sum=Sum+self.List[i]
        
        return Sum
        
    def Average(self):
        Sum=0
        for no in self.List:
            Sum = Sum+no
        
        Avg = Sum/self.Size
        return Avg

        
def main():
    obj1= Numbers()
    obj1.Accept()
    obj1.Display()

    Ret = obj1.Summation()
    print("Summation of the elements is : ",Ret)

    Ret = obj1.Average()
    print("Average of the List is : ",Ret)


if __name__=="__main__":
    main()