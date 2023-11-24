import time

class ATM:
    def __init__(self, balance, pin):
        self.balance = 2000
        self.pin = 1234

    def check_balance(self):
        y=int(input("Enter your pin: "))
        if y== 1234:
            print("Your account balance is: " , self.balance )
        else:
            print(f"invalid pin")



    def deposit(self, amount):
        y = int(input("Enter your pin: "))
        if y == 1234:
            amount = int(input("Enter your amount: "))
            self.balance += amount
            print(f"Deposit successful. Your new balance is: {self.balance}")

        else:
             print(f"invalid pin")




    def withdraw(self, amount):
        y = int(input("Enter your pin: "))
        if y == 1234:
            if amount > self.balance:
                print("Insufficient funds.")

            else:
                 self.balance -= amount
                 print(f"Withdrawal successful. Your new balance is: {self.balance}")
        else:
            print(f"invalid pin")

    def change_pin(self, new_pin):
        y = int(input("Enter your pin: "))
        if y == 1234:
           pin = int(input("Enter your pin"))
           self.pin = new_pin
           print("PIN changed successfully.")
        else:
             print(f"invalid pin")

def main():
    atm = ATM(0000, 1234)

    while True:
        print("Welcome to the ATM!")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            amount = int(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif choice == 3:
            amount = int(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == 4:
            new_pin = int(input("Enter your new PIN: "))
            atm.change_pin(new_pin)
        elif choice == 5:
            break

        time.sleep(2)

if __name__ == "__main__":
    main()