
CheckEven = lambda No : No%2

Doubles = lambda No : No*2

Sum = lambda a,b : a+b


def FilterX(Helper_Function,List):
    Result=[]
    for No in List:
        if(Helper_Function(No)==True):
            Result.append(No)
    return Result

def MapX(Helper_Function,List):
    Result=[]
    for No in List:
        Value = Helper_Function(No)
        Result.append(Value)
    return Result

def ReduceX(Helper_Function,List):
    Ans = 0
    for No in List:
        Ans = Helper_Function(Ans,No)
    return Ans


def main():
    print("Enter number of elements you want to enter : ")
    iSize = int(input())

    Data_Input = []
    print("Please enter the data ")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is : ",Data_Input)

    Data_Filter=FilterX(CheckEven,Data_Input)
    print("Data after filter : ",Data_Filter)

    Data_Map = MapX(Doubles, Data_Filter)
    print("Data after map is : ",Data_Map)

    Output = ReduceX(Sum,Data_Map)
    print("Result after reduce is : ",Output)
    

if __name__ == "__main__":
    main()