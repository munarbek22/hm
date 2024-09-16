class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        user_input = int(input('Введите сумму для добавление в баланс: '))
        self._balance += user_input
        print( f'На вашем балансе теперь: {self._balance}')

    def _kill(self):
        self._balance = 0
        print(f'Счет {self._name} был обнулен.')

    def __jackpot(self):
        self._balance *= 10
        print( f'Теперь на вашем счете {self._balance}')
    def _add_balances(self,  another_bank):
        self._balance += another_bank
        print(f'баланс объединен, теперь ваш баланс: {self._balance}')


b1=Bank('Muna', 5)
b2=Bank('suli', 9)

b1.moneyX()
b1._kill()
b1._Bank__jackpot()
b1._add_balances(b2._balance)
print(b1)