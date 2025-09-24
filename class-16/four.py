class Account:
    def open_account(self):
        print("Account opened")
    def deposit_amount(self,amount):
        print(amount,": Amount deposited")
    def get_balance(self):
        return 0
a1=Account()
a1.open_account()
a1.deposit_amount(5000)
a1.deposit_amount(1500)