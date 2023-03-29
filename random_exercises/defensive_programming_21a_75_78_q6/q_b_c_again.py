class BankAccount:
    def __init__(self, name, balance: float):
        self.name = name
        self.balance = balance

class InvestmentAccount(BankAccount):
    def __init__(self, name, balance: float):
        super().__init__(name, balance)
        self.invsts = {}

    def add_investments(self, id, qty: float):
        self.invsts[id] = qty


def add_to_mem_from_file(file_name):
    accounts = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line.strip()
        while line:
            words = line.split()
            name = words[0].strip()
            balance = float(words[1].strip())
            acc_obj = None
            if len(words) == 2:
                acc_obj = BankAccount(name, balance)
            elif len(words) == 3 and words[2].strip() == 'investments:':
                acc_obj = InvestmentAccount(name, balance)
                line = f.readline()
                line.strip()
                while line and 'done investments' not in line:
                    words_invsts = line.split()
                    acc_obj.add_investments(words_invsts[0], float(words_invsts[1]))
                    line = f.readline()
                    line.strip()
            line = f.readline()
            line.strip()
            accounts.append(acc_obj)
    return accounts





def print_accs(accounts):
    for i, v in enumerate(accounts):
        if isinstance(v, InvestmentAccount):
            print(f'InvestmentsAccount: {v.name} {v.balance} and investments: {v.invsts}')
        else:
            print(f'BankAccount: {v.name} {v.balance}')

f = 'data.txt'
accs = add_to_mem_from_file(f)
print_accs(accs)