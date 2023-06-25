# Instance variable : Name, Address, AccountNo, Amount
# Instance Methods : CreateAccount, DisplayInformation

class Bank_Account:
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


def main():

    Customer1 = Bank_Account()
    Customer2 = Bank_Account()

    print("Creating account for first customer.")
    Customer1.CreateAccount()
    Customer1.DisplayAccountInfo()
    
    print("")

    print("Creating account for second customer.")
    Customer2.CreateAccount()
    Customer2.DisplayAccountInfo()
    
if __name__=="__main__":
    main()