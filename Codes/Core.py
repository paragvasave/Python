import multiprocessing

def main():
    print("Number of logical CPU cores : ",multiprocessing.cpu_count())

if __name__=="__main__":
    main()