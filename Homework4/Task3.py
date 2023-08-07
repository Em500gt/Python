# Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

class Bankomat:
    def __init__(self):
        self.balance = 0
        self.operations_count = 0
        self.total_operations = 0

    def deposit(self, amount):
        if self.check_tax():
            amount -= amount * 0.1
        self.balance += amount
        self.operations_count += 1
        self.total_operations += 1
        self.calculate_interest()

    def withdraw(self, amount):
        if self.check_tax():
            amount -= amount * 0.1
        if amount > self.balance:
            print("Недостаточно средств на счете")
        else:
            if amount % 50 == 0:
                commission = min(max(amount * 0.015, 30), 600)
                amount -= commission
                self.balance -= amount
                self.operations_count += 1
                self.total_operations += 1
                self.calculate_interest()
            else:
                print("Сумма должна быть кратна 50")

    def exit(self):
        print("Сумма на счете:", self.balance)

    def check_tax(self):
        return self.total_operations % 5 == 0 and self.balance >= 5000000

    def calculate_interest(self):
        if self.operations_count == 3:
            interest = self.balance * 0.03
            self.balance += interest
            self.operations_count = 0


atm = Bankomat()
atm.deposit(2000)
atm.withdraw(500)
atm.deposit(1000)
atm.exit()