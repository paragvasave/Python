# Instance variable : Name, Address, AccountNo, Amount
# Instance Methods : CreateAccount, DisplayInformation
# Class variable :  Bank_Name, ROI_FD
# Class Method : DisplayBankInformation
# Static Method : DisplayKYCInformation

class Bank_Account:
    Bank_Name = "HDFC Bank Pvt Ltd."
    ROI_FD=6.7

    def __init__(self):
        self.Name = ""
        self.Address = ""
        self.AccountNo = 0
        self.Amount = 0
    
    def CreateAccount(self):
        print("Enter the name of account holder : ",end=" ")
        self.Name=input()

        print("Enter address : ",end=" ")
        self.Address = input()

        print("Enter account number  : ",end=" ")
        self.AccountNo = int(input())

        print("Enter initial amount : ",end = " ")
        self.Amount= int(input())

    def DisplayAccountInfo(self):
        print("---------------Your account details---------------")
        print("Name of account holder : ",self.Name)
        print("Address : ",self.Address)
        print("Account No : ",self.AccountNo)
        print("Balance : ",self.Amount)
    
    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking console.")
        print("Bank Name : ",cls.Bank_Name)
        print("Rate of Interest on FD : ",cls.ROI_FD)

    @staticmethod
    def DisplayKYCInformation():
        print("Please find below the KYC rules.")
        print("As per Govt. of India below documents are mandatory to open an account.")
        print("1. Passport size photo")
        print("2. Aadhar card")
        print("3. PAN card")


    def Deposit(self,Value):
        self.Amount= Value+self.Amount


    def Withdrawl(self,Value):
        self.Amount=self.Amount-Value

def main():
    Bank_Account.DisplayBankInformation()
    print("")

    print("Name of Bank : ",Bank_Account.Bank_Name)
    print("Rate of Interest on FD : ",Bank_Account.ROI_FD)
    print("")

    Bank_Account.DisplayKYCInformation()
    print("")

    Customer1 = Bank_Account()
    Customer2 = Bank_Account()

    print("Creating account for first customer.")
    Customer1.CreateAccount()
    print("")

    print("Creating account for second customer.")
    Customer2.CreateAccount()

    Customer1.DisplayAccountInfo()
    print("")
    Customer2.DisplayAccountInfo()

    Customer1.Deposit(500)
    Customer2.Deposit(1200)

    print("Balance of {} after deposit is : {}".format(Customer1.Name,Customer1.Amount))
    
    print("Balance of {} after deposit is : {}".format(Customer2.Name,Customer2.Amount))

    Customer1.Withdrawl(5000)
    Customer2.Withdrawl(3200)

    print("Balance of {} after Withdrawl is : {}".format(Customer1.Name,Customer1.Amount))
    print("")
    print("Balance of {} after Withdrawl is : {}".format(Customer2.Name,Customer2.Amount))

    
if __name__=="__main__":
    main()