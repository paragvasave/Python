from sys import *
import os
import time
import psutil
import datetime

def ProcessDisplay(Log_Dir = "Process"):
    ListProcess=[]

    if not os.path.exists(Log_Dir):
        try:
            os.mkdir(Log_Dir)
        except:
            pass
    
    separator = "-" * 80
    Log_Path = os.path.join(Log_Dir,"Process %s.log"%(datetime.datetime.now().strftime("%d-%m-%Y~%H_%M_%S")))
    f= open(Log_Path,'w')
    f.write(separator + "\n")
    f.write("Process Logger : "+time.ctime() + "\n")
    f.write(separator + "\n")

    for process in psutil.process_iter():
        try:
            ProcessInfo = process.as_dict(attrs = ['pid','name','username'])
            vms = process.memory_info().vms/(1024*1024)
            ProcessInfo['vms'] = vms
            ListProcess.append(ProcessInfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    for element in ListProcess:
        f.write("%s\n" % element)
            

def main():
    print("-------------- Python automation-------------")
    print("Application name : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        print("Use -h for help or -u for usage")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help : This script is use to save log record of running process in a file")
        exit()

    if((argv[1]=="-u") or (argv[1]=="-U")):
        print("Usage : Application_Name AbsolutePath_of_Directory")
        exit()
    
    ProcessDisplay(argv[1])
    
if __name__=="__main__":
    main()