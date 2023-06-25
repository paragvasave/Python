
class Bank_Account:
    Bank_Name = "HDFC Bank Pvt.Ltd"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name=""
        self.Address=""
        self.AccountNo=0
        self.Amount=0

    def CreateAccount(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your intial amount : ")
        self.Amount = int(input())

        print("Enter your Address : ")
        self.Address = input()

        print("Enter your Account Number : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("-------- Your Account informartion is as below --------")
        print("Name of Account Holder : ",self.Name)
        print("Account Number : ",self.AccountNo)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in account : ",self.Amount)

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is : ",cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposite is : ",cls.ROI_On_FD)
   
    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information")
        print("According to the rules of Goverment of India you have to submit below documnets")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of aadhar card")
        print("3 : Photo of PAN card")
       
    def Deposit(self,value):
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value

def main():
    print("----------------------------------------------------------------------------")
    print("---------------------------- Banking Application -----------------------------")
    print("----------------------------------------------------------------------------")
    print("-------------- Calling Static method to display KYC info ---------------------")
    Bank_Account.DisplayKYCInfo()

    print("----------------------------------------------------------------------------")
    print("---------------------------- Accessing Class variables -----------------------")
    print("----------------------------------------------------------------------------")
    print("Bank Name : ",Bank_Account.Bank_Name)
    print("Rate of Interest on FD : ",Bank_Account.ROI_On_FD)

    print("----------------------------------------------------------------------------")
    print("-------------- Calling class method to display banking info ------------------")
    print("----------------------------------------------------------------------------")
    Bank_Account.DisplayBankInformation()

    print("----------------------------------------------------------------------------")
    print("-------------------------Creating object of class---------------------------")
    print("----------------------------------------------------------------------------")
    User1=Bank_Account()
    User2=Bank_Account()

    print("----------------------------------------------------------------------------")
    print("-------------------------Creating the first account-------------------------")
    print("----------------------------------------------------------------------------")

    print("----------------------------------------------------------------------------")
    print("--------------------- Enter details for first account holder ---------------")
    print("----------------------------------------------------------------------------")
    User1.CreateAccount()

    print("----------------------------------------------------------------------------")
    print("-------------------------Creating the second account------------------------")
    print("----------------------------------------------------------------------------")

    print("----------------------------------------------------------------------------")
    print("--------------------- Enter details for second account holder --------------")
    print("----------------------------------------------------------------------------")
    User2.CreateAccount()

    print("--------- Calling Instance method to show information of first account -----")
    print("----------------------------------------------------------------------------")
    User1.DisplayAccountInfo()
    print("----------------------------------------------------------------------------")

    print("-------- Calling Instance method to show information of second account -----")
    print("----------------------------------------------------------------------------")
    User2.DisplayAccountInfo()
    print("----------------------------------------------------------------------------")

    print("-------------------------- Depositing 500 in User1 account -----------------")
    User1.Deposit(500)
    print("----------------------------------------------------------------------------")

    print("-------------------------- Depositing 1200 in User2 account -----------------")
    User2.Deposit(1200)
    print("----------------------------------------------------------------------------")
    
    print("Amount of {} after deposit : {}".format(User1.Name,User1.Amount))
    print("Amount of {} after deposit : {}".format(User2.Name,User2.Amount))
    
    print("-------------------------- Withdraw 1000 in User1 account -----------------")
    User1.Withdraw(1000)
    print("----------------------------------------------------------------------------")

    print("-------------------------- Depositing 15000 in User2 account -----------------")
    User2.Withdraw(3000)
    print("----------------------------------------------------------------------------")

    print("Amount of {} after witdraw : {}".format(User1.Name,User1.Amount))
    print("Amount of {} after witdraw : {}".format(User2.Name,User2.Amount))

    print("----------------------------------------------------------------------------")
    print("---------------------- End of banking appplication --------------------------")
    print("----------------------------------------------------------------------------")


if __name__=="__main__":
    main()