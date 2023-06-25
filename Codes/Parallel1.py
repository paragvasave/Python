import os 
import multiprocessing

def Square(No):
    return No*No

def main():
    print("Process ID of our application : ",os.getpid())

    Data = [1,2,3,4,5]
    Result = list()

    pobj = multiprocessing.Pool()
    Result = pobj.map(Square, Data)

    print("Result after square operation is : ",Result)

if __name__=="__main__":
    main()