# Instance variable : Name, Address, AccountNo, Amount
# Instance Methods : CreateAccount, DisplayInformation
# Class variable :  Bank_Name, ROI_FD
# Class Method : DisplayBankInformation

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


def main():

    print("Name of Bank : ",Bank_Account.Bank_Name)
    print("Rate of Interest on FD : ",Bank_Account.ROI_FD)
    print("")

    Bank_Account.DisplayBankInformation()
    print("")

    Customer1 = Bank_Account()
    Customer2 = Bank_Account()

    print("Creating account for first customer.")
    Customer1.CreateAccount()

    print("Creating account for second customer.")
    Customer2.CreateAccount()

    Customer1.DisplayAccountInfo()
    Customer2.DisplayAccountInfo()
    
if __name__=="__main__":
    main()