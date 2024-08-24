class My_Account:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance = self.balance-amount 
            self.transaction_history.append(f"Withdrawn: {amount}")
            return f"Successfully withdrawn: {amount}"

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transaction_history.append(f"Deposited: {amount}")
        return f"Successfully deposited: {amount}"

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            self.transaction_history.append("PIN changed successfully.")
            return "PIN changed successfully."
        else:
            return "Incorrect old PIN."

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self, account):
        self.account = account

    def main(self):
        while True:
            print("\nWelcome to the ATM Machine")
            print("1. Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("\nChoose an option: ")
            if choice == '1':
                self.balance_inquiry()
            elif choice == '2':
                self.cash_withdrawal()
            elif choice == '3':
                self.cash_deposit()
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                self.transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM. Have a Nice Day!")
                break
            else:
                print("Invalid option. Please try again.")

    def balance_inquiry(self):
        print(f"Your current balance is: {self.account.check_balance()}")

    def cash_withdrawal(self):
        amount = float(input("Enter amount to withdraw: "))
        print(self.account.withdraw(amount))

    def cash_deposit(self):
        amount = float(input("Enter amount to deposit: "))
        print(self.account.deposit(amount))

    def change_pin(self):
        old_pin = input("Enter old PIN: ")
        new_pin = input("Enter new PIN: ")
        print(self.account.change_pin(old_pin, new_pin))

    def transaction_history(self):
        history = self.account.get_transaction_history()
        if not history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in history:
                print(transaction)

if __name__ == "__main__":
    user_account = My_Account(pin="1234", balance=1000) 
    atm = ATM(account=user_account)  
    atm.main()  
