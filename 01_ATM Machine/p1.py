class Account:
    '''
        Attributes:
            account_holder: Name of the account holder (string).
            account_number: Unique number for the account (integer).
            balance: Current balance in the account (float).
            pin: A private attribute for the user's PIN (string; use encapsulation).
    '''

    def __init__(self , account_holder: str , account_number: int , balance: float , pin: str):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance
        self.__pin = pin

    '''
    Methods:
        verify_pin(self, entered_pin): Check if the entered PIN matches the stored PIN.
        deposit(self, amount): Add money to the account balance.
        withdraw(self, amount): Deduct money from the balance if sufficient funds are available.
        get_balance(self): Return the current balance (read-only for security). 
    '''

    def verify_pin(self, entered_pin: str) -> bool:
        return entered_pin == self.__pin

    def deposit(self, amount: float) -> str:
        if amount > 0:
            self.__balance += amount
            return "Deposit successful."
        return "Deposit amount must be positive."

    def withdraw(self, amount: float) -> str:
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount <= self.__balance:
            self.__balance -= amount
            return "Withdrawal successful."
        if amount > self.__balance:
            return f'You Account balance is {self.__balance}'
        return "Insufficient funds."

    def get_balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: {self.__balance}"


class ATM:

    accounts : dict = {}
    '''
    Attributes:
        accounts: A list or dictionary to store all account objects (e.g., {account_number: account_object}).
    '''

    '''
    Methods:
    __init__(self): Initialize the ATM with an empty dictionary for accounts.
    add_account(self, account): Add an account to the system.
    authenticate_user(self, account_number, pin): Verify account existence and PIN.
    perform_transaction(self, account_number): Handle user actions (deposit, withdraw, check balance).
    display_menu(self): Display transaction options to the user.
        '''
    def add_account(self, account: Account):
            self.accounts[account.account_number] = account

    def authenticate_user(self, account_number: int, pin: str) -> bool:
        account = self.accounts.get(account_number)
        if account and account.verify_pin(pin):
            return True
        print("Authentication failed. Check account number or PIN.")
        return False

    def perform_transaction(self, account_number: int):
        account = self.accounts.get(account_number)
        if not account:
            print("Invalid account number.")
            return

        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                print(account.deposit(amount))

            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                print(account.withdraw(amount))

            elif choice == "3":
                print(f"Balance: {account.get_balance()}")

            elif choice == "4":
                print("Thank you for using the ATM.")
                break

            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("\nTransaction Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")



account1 = Account("Abdullah", 1234, 1000, "1111")
atm = ATM()
atm.add_account(account1)

# Authenticate and perform transactions
account_number = int(input("Enter your account number: "))
pin = input("Enter your PIN: ")

if atm.authenticate_user(account_number, pin):
    atm.perform_transaction(account_number)
else:
    print("Access denied.")

