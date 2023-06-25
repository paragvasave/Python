import schedule
import datetime
import time

def Fun():
    print("Inside fun time : ",datetime.datetime.now())

def main():
    print("Inside main : ",datetime.datetime.now())

    schedule.every(5).seconds.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()