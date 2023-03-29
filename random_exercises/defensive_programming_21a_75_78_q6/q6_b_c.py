class BankAccount:
    def __init__(self, name: str, balance: float):
        """
        Bank Account class of a person with balance of the person account
        Parameters
        ----------
        name
        balance
        """
        self.name = name
        self.balance = balance

class InvestmentAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.investments = {}

    def add_investment(self, id, qty:float):
        self.investments[id] = qty



def read_file_to_mem(file_name: str):
    """
    read the data from the file and load to to the memory as BankAccount/Investment
    Parameters
    ----------
    file_name

    Returns
    -------

    """
    accounts = []
    with open(file_name, 'r') as file:
        line = file.readline()
        while line:
            words_li = line.split()
            inv_obj = None
            if len(words_li) == 2:
                inv_obj = BankAccount(words_li[0], float(words_li[1]))
            elif len(words_li) == 3 and \
                words_li[2].strip() == "investments:":
                inv_obj = InvestmentAccount(words_li[0], float(words_li[1]))
                line = file.readline()
                while line and line.strip() != 'done investments':
                    inv_li = line.split()
                    inv_obj.add_investment(inv_li[0], float(inv_li[1]))
                    line = file.readline()
            accounts.append(inv_obj)
            line = file.readline()

    return accounts




accs = read_file_to_mem("data.txt")

for v in accs:
    print(f'name: {v.name} balance: {v.balance}', end=" ")
    if isinstance(v, InvestmentAccount):
        print(f'investments: {v.investments}', end=" ")
    print()