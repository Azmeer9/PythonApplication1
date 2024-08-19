print(""" 
***********
Welcome To The 'Banking System'
***********
""")

class BankAccount(object):
    def __init__(self, name, accno, balance):
        self.name = name
        self.acccno = accno
        self.balance = balance

    def balanceCheck(self):
        print(f'Balance is : {self.balance}')

    def withdraw(self, am):
        self.balance -= am
        print(f"Balance After Withdraw: {self.balance}")
    
    def deposit(self, am):
        self.balance += am
        print(f"Balance After Deposit: {self.balance}")

class savingAcc(BankAccount):
    def addInterest(self):
        interest = self.balance / 50
        print(f"Interest on your Amount is : {interest}")
        self.balance += interest

class Checking(savingAcc):
    pass

# MAIN _ WORK
char = ""
while char.lower() != "q":
    print(""" 
    Press 'S' to *START* || Press 'Q' to Quit   
    >ENTER : 
    """)
    char = input().lower()

    if char == 's':
        n = input("Enter your name: ")
        a = int(input("Enter Your Account #: "))
        b = int(input("Enter Your Initial Balance: "))
        s = savingAcc(n, a, b)

        s.balanceCheck()

        #s.deposit(5000)
        #s.withdraw(1000)
        #s.addInterest()

    elif char == 'q':
        print("Exiting the system...")
    else:
        print("Invalid input. Please enter 'S' to start or 'Q' to quit.")
