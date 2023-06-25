def Area(Radius,PI=3.14):
    Result = PI*Radius*Radius
    return Result

def main():
    RValue = 10.5
    PIValue = 3.14

    # Positional argument
    Ans = Area(RValue,PIValue)
    print("Area is : ",Ans)

    # Keyword argument
    Ans =Area(Radius=RValue,PI=PIValue)
    print("Area is : ",Ans)

    # Positional argument & Default argument
    Ans = Area(10.5)
    print("Area is : ",Ans)

    # Keyword argument & Default argument
    Ans = Area(Radius=10.5)
    print("Area is : ",Ans)

    # Keyword argument
    Ans =Area(PI=7.10, Radius=10.5)
    print("Area is : ",Ans)
    

if __name__=="__main__":
    main()