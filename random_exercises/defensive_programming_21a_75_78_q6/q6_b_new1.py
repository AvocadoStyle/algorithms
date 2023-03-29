class BankAccount:
    def __init__(self, name, balance: float):
        self.name = name
        self.balance = balance


class InvestmentAccount(BankAccount):
    def __init__(self, name, balance: float):
        super().__init__(name, balance)
        self.invsts = {}

    def add_investment(self, id, qty: float):
        self.invsts[id] = qty

def read_from_file_to_mem(file_name):
    accounts = []
    with open(file_name, 'r') as f:
        line = f.readline()
        while line:
            words = line.strip().split()
            if len(words) == 2 and 'done' not in words[0]:
                name = words[0].strip()
                balance = words[1].strip()
                try:
                    balance = float(balance)
                except Exception(f'cannot cast to float') as e:
                    print(f'error: {e}')
                    raise e
                acc_obj = BankAccount(name, balance)
            elif len(words) == 3:
                name = words[0].strip()
                balance = words[1].strip()
                try:
                    balance = float(balance)
                except Exception(f'cannot cast to float') as e:
                    print(f'error: {e}')
                    raise e
                acc_obj = InvestmentAccount(name, balance)
                line = f.readline()
                while line and 'done' not in line:
                    words_invest = line.strip().split()
                    id = words_invest[0].strip()
                    qty = words_invest[1].strip()
                    try:
                        qty = float(qty)
                    except Exception(f'cannot cast to float') as e:
                        print(f'error: {e}')
                        raise e
                    acc_obj.add_investment(id, qty)
                    line = f.readline()
            accounts.append(acc_obj)
            line = f.readline()
        return accounts

def print_accs(accs):
    for i, v in enumerate(accs):
        if isinstance(v, InvestmentAccount):
            print(f'investment account: name={v.name} balance={v.balance}')
            for val in v.invsts:
                print(f'{val}: {v.invsts[val]}    ', end="")

            print()
        else:
            print(f'regular account: name={v.name} balance={v.balance}')

fn = 'data.txt'
accs = read_from_file_to_mem(fn)
print_accs(accs)





