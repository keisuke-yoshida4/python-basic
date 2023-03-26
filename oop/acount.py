import time


class Account:

    count = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.account_number = Account.count
        self.transaction_history = []
        Account.count += 1

    def withdraw(self, price):
        if price <= self.balance:
            self.balance -= price
            self.show_balance()
            self._add_transaction(-price)
        else:
            print(f"残高({self.balance})円が足りません")

    def deposit(self, price):
        self.balance += price
        self.show_balance()
        self._add_transaction(price)

    def show_balance(self):
        print("{0.name}(口座番号:{0.account_number})の残高は{0.balance}円です".format(self))

    def _add_transaction(self, price):
        transaction = {
            "withdraw/deposit": price,
            "new_balance": self.balance,
            "time": Account._get_time_str()

        }
        self.transaction_history.append(transaction)

    @staticmethod
    def _get_time_str():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)

    def show_transaction_history(self):
        for transaction in self.transaction_history:
            transaction_str_list = []
            for k, v in transaction.items():
                transaction_str_list.append(f"{k}: {v}")
            print(",".join(transaction_str_list))


my_account = Account(balance=1000, name="my account")
print(my_account.name)
print(my_account.balance)
my_account.withdraw(200)
my_account.deposit(500)
my_account.withdraw(600)
# your_account = Account(balance=10000, name="your account")
# your_account.withdraw(700)
print(my_account.transaction_history)
print(Account._get_time_str())
my_account.show_transaction_history()
