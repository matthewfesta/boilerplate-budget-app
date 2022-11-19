class Category:
    ledger = []

    def __init__(self, name):
        self.name = name

    def deposit(self, amount, description):
        # Validate Amount and Description
        try:
            amount = float(amount)
        except:
            raise ValueError('Amount must be a number');
        else:
            amount = float(amount)
            

        





def create_spend_chart(categories):
