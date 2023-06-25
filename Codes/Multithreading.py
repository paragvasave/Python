import time
import threading

def DisplayEven(No):
    for i in range(1,No,1):
        if(i%2==0):
            print("Even number : ",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i%2!=0):
            print("Odd number : ",i)

def Addition(No):
    global X                        # for returning the value you have to use global variable
    Sum=0
    for i in range(0,No,1):
        Sum = Sum+No
    
    X = Sum
    

def main():
    print("Demonstration of parallel programming using multiple threads.")
    Number = 20
    
    p1 = threading.Thread(target=DisplayEven,args= (Number,))
    p2 = threading.Thread(target=DisplayOdd,args= (Number,)) 
    p3 = threading.Thread(target=Addition,args= (Number,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Addition of all the numbers : ",X)

    print("End of main")

if __name__=="__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()

    print("Execution time of a process : ",end_time-start_time , " sec." )
    # time given by the os to the process