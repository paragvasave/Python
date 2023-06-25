import psutil
import datetime 

def ProcessDisplay():
    ListProcess=[]

    for process in psutil.process_iter():
        try:    
            ProcessInfo = process.as_dict(attrs= ['pid','name','username'])
            
            ListProcess.append(ProcessInfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
        
    return ListProcess


def main():
   
    print("Process Monitor : ",datetime.datetime.now())
    print("")

    listprocess = ProcessDisplay()
    for element in listprocess:
        print(element)
    

if __name__=="__main__":
    main()