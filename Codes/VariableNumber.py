
def Add(*Values):
    Sum=0
    for no in Values:
        Sum=Sum+no
    return Sum


def AddX(*Values):
    Sum=0
    for i in range(0,len(Values),1):
        Sum=Sum+Values[i]
    return Sum

def main():

    Ans = Add(10,20,30,40,50)
    print("Addition of all parameters is : ",Ans)

    Ans = AddX(10,20,30,40,50)
    print("Addition of all parameters is : ",Ans)


if __name__=="__main__":
    main()