def DisplayFactors(iNo):
    i=1
    while(i<=int(iNo/2)):
        if(iNo%i==0):
            print(i)
        i=i+1


def main():
    print("Enter a number : ")
    iNo = int(input())
    DisplayFactors(iNo)
    

if __name__=="__main__":
    main()