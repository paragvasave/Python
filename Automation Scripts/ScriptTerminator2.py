import schedule
import datetime
import time

Cnt = 0

def Fun():
    print("Inside fun time : ",datetime.datetime.now())
    global Cnt
    Cnt+=1
    if(Cnt==5):
        print("Count = 5, Script terminated : ",datetime.datetime.now())
        exit()

def main():
    print("Inside main : ",datetime.datetime.now())

    schedule.every(5).seconds.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()