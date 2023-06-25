def CheckEven(no):
    return(no%2==0)

def Increment(no):
    return (no+2)

def FilterX(List,Function_Name):
    Result=[]
    for no in List:
        if Function_Name(no):
            Result.append(no)
    return Result

def MapX(List,Function_Name):
    Result=[]
    for no in List:
        Value=Function_Name(no)
        Result.append(Value)
    return Result

def ReduceX(List):
    Sum=0
    for no in List:
        Sum=Sum+no
    return Sum

def main():
    print("Enter the size of list : ",end=" ")
    iSize = int(input())
    Data = list()

    for i in range(0,iSize,1):
        print("Enter element : ",i+1," : ",end=" ")
        iNo = int(input())
        Data.append(iNo)
    print("Elements of the list are : ",Data)

    Data_Filter=list(FilterX(Data,CheckEven))
    print("Data after filter : ",Data_Filter)

    Data_Map =list(MapX(Data_Filter,Increment))
    print("Data after map : ",Data_Map)

    Data_Reduce=ReduceX(Data_Map)
    print("Data after reduce : ",Data_Reduce)

if __name__=="__main__":
    main()