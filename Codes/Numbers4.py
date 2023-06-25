class Numbers:
    def __init__(self):
        self.List = list()
        self.Size =0
	
    def Accept(self):
        print("Enter the size of list",end=" ")
        self.Size=int(input())
        
        for i in range(0,self.Size,1):
            print("Enter element : ",i+1,":",end=" ")
            value=int(input())
            self.List.append(value)
	
    def Display(self):
        print("Elements of list are : ",end=" ")
        for no in self.List:
            print(no,end=" ")
        print("")
    
    def Summation(self):
        Sum =0
        for no in self.List:
            Sum=Sum+no
            
        return Sum
    
    def Average(self):
        Sum=0
        for no in self.List:
            Sum = Sum+no
            
        Avg = Sum/self.Size
        return Avg
        
    def Maximum(self):
        iMax = self.List[0]
        for no in self.List:
            if(no>iMax):
                iMax= no
                
        return iMax
            
def main():
    obj1=Numbers()
    obj1.Accept()
    obj1.Display()
    
    Ret = obj1.Summation()
    print("Summation of all the elements is : ",Ret)

    Ret = obj1.Average()
    print("Average of all the elements is : ",Ret)
    
    Ret = obj1.Maximum()
    print("Largest number is : ",Ret)
    
    
if __name__=="__main__":
    main()