class BankAccount:
    def __init__(self, account_number: str = "", balance: float = 0):
        self.account_number = account_number
        self.balance = balance
    
    def add(self, summ):
        self.balance += summ
        return self.balance
    
    def withdraw(self, summ):
        if summ > self.balance:
            return f"сумма снятия превышает баланс на {summ - self.balance}"
        else:
            self.balance -= summ
            return self.balance
    
    def transfer_money(self, other_account, summ):
        if summ > self.balance:
            return f"сумма перевода превышает баланс на {summ - self.balance}"
        else:
            self.balance -= summ
            other_account.add(summ)
            return other_account.balance


account_1 = BankAccount("12345", 5000)
print(f"баланс первого счета после пополнения: {account_1.add(750)}\nбаланс первого счета после снятия: {account_1.withdraw(200)}")

account_2 = BankAccount("67890")
print(f"баланс второго счета после перевода: {account_1.transfer_money(account_2, 2000)}")