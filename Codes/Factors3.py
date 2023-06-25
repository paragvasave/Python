
def main():
    print("Enter a number : ")
    iNo = int(input())
    i=1
    print("Factors are : ")

    while(i<=int(iNo/2)):
        if(iNo%i==0):
            print(i)
        i=i+1

if __name__=="__main__":
    main()