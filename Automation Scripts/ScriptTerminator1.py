import schedule
import datetime
import time

def Script_Terminator():
    print("Script terminated : ",datetime.datetime.now())
    exit()

def Fun():
    print("Inside fun time : ",datetime.datetime.now())

def main():
    print("Inside main : ",datetime.datetime.now())

    schedule.every(5).seconds.do(Fun)
    schedule.every().tuesday.at("17:45:00").do(Script_Terminator)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()