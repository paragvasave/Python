
def Square(No):
    return No*No

def main():
    Data = [1,2,3,4,5]
    Result=[]

    for i in Data:
        Result.append(Square(i))
    
    print(Result)


if __name__=="__main__":
    main()