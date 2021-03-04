#code by miyandi279
from time import strftime
import time

def Prepaid():
    print("(1) Airtime")
    print("(2) Data bundles")
    number = int(input(" "))
    if number == int(1):
        print("Select service provider")
        print("(1) Vodacom")
        print("(2) MTN")
        print("(3) Cell C")
        print("(4) Telkom")
        number2 = int(input(" "))
        cell1 = int(input("Enter cell phone number "))

        amount1 = int(input("Enter amount R "))
        print("Buy R",amount1, " airtime for ", cell1)
        confirm = int(input("(1) Confirm (2) Cancel"))
        if confirm == int(1):
            for i in range(5):
                time.sleep(0.2)
                print("Successful")
                print("Your new balance is ", int(5000) - amount1,)
                print("Transaction was made on: ",strftime("%A %d/%b/%Y %I:%M %p "))
        if confirm == int(2):
            print("Transaction cancelled")
                    
    if number == int(2):
        print("(1) 100MB Weekly R12 \n(2) 200MB Monthly R29 \n(3) 5GB Monthly R250")
        chose = int(input(" "))
        print("Successful")
        print("Your account will be charged for data bundle purchase according to your choice above")
        print("Transaction was made on: ",strftime("%A %d/%b/%Y %I:%M %p "))
            

def Deposite():
    print(" ")
    deposit=int(input("How much you want to Deposite: R"))
    print("You're going to deposite R",deposit," into your account")
    print("Enter 1 to confirm or 2 to cancel")
    conf=int(input(" "))
    
    if conf == int(1):
        new_account =int(5000)+deposit
        for x in range(5):
            time.sleep(0.2)
        print("You have successfully deposited R",deposit,"into your account")
        print(" ")
        print("Your new balance is: R ",new_account)
        print(" ")
        print("Transaction was made on: ",strftime("%A %d/%b/%Y %I:%M %p "))
       
    if conf == int(2):
        print(" ")
        print("Transaction cancelled")
        print(" ")

def Withdraw():
    print(" ")
    withdraw=int(input("How much you want to Withdraw: R "))
    print("You're going to withdraw money R", withdraw," from your account")
    print("Enter 1 to confirm or 2 to cancel")
    confi = int(input(" "))
    
    if confi == int(1):
        if withdraw>=5000:
            print(" ")
            print("You can not withdraw that money")
            print(" ")
        
        if withdraw<5000:
            new_account2 =5000-withdraw
            for t in range(5):
                time.sleep(0.2)
            print("You have successfully withdrawn R",withdraw,"into your account")
            print(" ")
            print("Your new balance is: R ",new_account2)
            print(" ")
            print("Transaction was made on: ",strftime("%A %d/%b/%Y %I:%M %p "))
       
    if confi == int(2):
        print(" ")
        print("Transaction cancelled")
        print(" ")

def Transfer():
    print(" ")
    transfer=int(input("How much you want to Transfer: R "))
    if transfer>=5000:
        print(" ")
        print("You can not transfer that money")
        print(" ")
    if transfer<5000:
        for i in range(3):
            rec=input("Enter account number of the receiver: ")
            print("You're going to transfer money to ", rec, " from your account")
            print("Enter 1 to confirm or 2 to cancel")
            conf3 = int(input(" "))
    
            if conf3 == int(1):
                new_account3 =5000-transfer
                for c in range(5):
                    time.sleep(0.2)
                print("You have successfully transferred R ",transfer," to ",rec)
                print(" ")
                print("Your new balance is: R ",new_account3)
                print("Transaction was made on: ",strftime("%A %d/%b/%Y %I:%M %p"))

            if conf3 == int(3):
                print(" ")
                print("Transaction cancelled")
            break      
                

print("="*60)
print("             Mi279                      ")
print("="*60)
print("pin is 1234")

username=input("Enter your name: ")
pn = int(input("Enter your pin: "))
pin=int(pn)
    
if pin != int(1234):
    print(" ")
    print("Wrong pin ")

    
if pin == int(1234):
    print(" ")
    print("Welcome back ",username)
    print(" ")
    print("Your account is: R 5000 ")
    for i in range(5):
        time.sleep(0.3)
    print(" ")
    print("What do you want to do today?")
    print("(1) Deposite")
    print("(2) Withdraw")
    print("(3) Transfer")
    print("(4) Buy prepaid")
    print(" ")
    what = int(input(" "))
    if what == int(1):
        Deposite()

    if what == int(2):
        Withdraw()

    if what == int(3):
        Transfer()
        
    if what == int(4):
        Prepaid()
                    
print("="*60)
