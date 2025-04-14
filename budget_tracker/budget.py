# TODO: Import Transaction class from transaction.py

from transaction import Transaction

class Budget:
    def __init__(self):
        # TODO: Create a list to store transactions

        self.transaction = []
        

    def add_transaction(self, transaction):
        # TODO: Append the transaction to the list

        self.transaction.append(transaction)


    def get_balance(self):
        # TODO: Loop through transactions and calculate the balance
        result_balance = 0

        for transaction in self.transaction:
            if transaction.is_income.lower() == "yes":
                result_balance += transaction.amount
       
            if transaction.is_income.lower() == "no":
                result_balance -= transaction.amount

        return result_balance

        

    def save_to_file(self, filename):
        # TODO: Write transactions to a file

        with open(filename, "w") as file:
            for items in self.transaction:
                if items.is_income.lower() == "yes":
                    file.write(f"{items}\n")
                    # file.write(f"Income: {items.description} | £{items.amount} | Category: {items.category}\n")
                if items.is_income.lower() == "no":
                    file.write(f"Expense: {items.description} | £{items.amount} | Category: {items.category}\n")

        pass

    def load_from_file(self, filename):
        # TODO: Read file and load transactions using Transaction class

        try:
        
            with open(filename, "r") as file:
                for existing_transactions in file:
                    # self.transaction.append(existing_transactions)
        #             print(existing_transactions)
                    existing_transactions = existing_transactions.strip()
                    parts = existing_transactions.split('|')

                    if len(parts) == 3:

                        description_part = parts[0]
                        amount_part = parts[1]
                        category_part = parts[2]
                        # # is_income = parts[3]
                        # amount = float(amount_part.replace("£:", ""))
                        # category = category_part.replace("Category: ", "")
                        
                        if description_part.startswith("Income: "):
                            is_income = "yes"
                            replaced_description = description_part.replace("Income: ", "").strip()
                        elif description_part.startswith("Expense: "):
                            is_income = "no"
                            replaced_description = description_part.replace("Expense: ", "").strip()

                        amount = float(amount_part.replace("£", ""))
                        category = category_part.replace("Category: ", "").strip()

                        transactions = Transaction(replaced_description, amount, category, is_income)
                        self.transaction.append(transactions)
                    
                    # else:
                        # print(f"Skipping invalid transaction: {existing_transactions}")

        except FileNotFoundError:
            print(f'No previous transaction list found at {filename}. Starting with an empty list')
        except Exception as e:
            print(f'An error occured while loading transactions: {e}')

