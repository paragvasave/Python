import os

def main():
    print("application process PID : ",os.getpid())
    print("Parent PID : ",os.getppid())

if __name__=="__main__":
    main()