
def main():
    print("Enter a number : ")
    iNo = int(input())

    for i in range(1,iNo,1):
        if(iNo%i ==0):
            print(i)

if __name__=="__main__":
    main()