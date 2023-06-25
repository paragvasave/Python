import schedule
import datetime
import time

def Task_Minute():
    print("Task based on minutes gets schedule at : ",datetime.datetime.now())

def Task_Hour():
    print("Task based on hour gets schedule at : ",datetime.datetime.now())

def Task_Day():
    print("Task based on day gets schedule at : ",datetime.datetime.now())


def main():
    print("Inside taks schedular. Current time : ",datetime.datetime.now())

    schedule.every(1).minutes.do(Task_Minute)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().day.do(Task_Day)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()