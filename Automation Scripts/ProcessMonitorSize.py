import psutil

def ProcessDisplay():
    ListProcess=[]

    try:
        for process in psutil.process_iter():
            processinfo = process.as_dict(['pid','username' ,'name'])

            processinfo['vms']=process.memory_info().vms/(1024*1024)
            ListProcess.append(processinfo)

    except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
        pass

    return ListProcess

def main():

    ListProcess = ProcessDisplay()
    for process in ListProcess:
        print(process)

if __name__=="__main__":
    main()