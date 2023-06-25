def DisplayFactors(iNo):
    i=1
    while(i<=int(iNo/2)):
        if(iNo%i==0):
            print(i)
        i=i+1