# TODO: Import Budget and Transaction classes

from budget import Budget
from transaction import Transaction

def main():
    budget = Budget()
    budget.load_from_file("budget_data.txt")

    while True:
        print("\n1. Add Transaction\n2. View Summary\n3. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # TODO: Get input and create Transaction
            # TODO: Add transaction to budget

            desc_ = input("Enter description: ")
            cash_amount = float(input("Enter amount: "))
            categoery = input("Enter category: ")
            income_or_expense = input("Is this an income? (yes/no): ")

            transaction = Transaction(desc_, cash_amount, categoery, income_or_expense)

            # transaction  = Transaction(
            #     input("Enter description: "),
            #     float(input("Enter amount: ")),
            #     input("Enter category: "),
            #     input("Is this an income? (yes/no): ")
            #     )

            budget.add_transaction(transaction)

        elif choice == "2":
            # TODO: Print each transaction
            # TODO: Print current balance

            for list in budget.transaction:
                if list.is_income.lower() == "yes":
                    print(list)

                else:
                    expense = str(list).replace("Income", "Expense")
                    # expense = f"Expense: {transaction.description} | £{transaction.amount} | Category: {transaction.category}"
                    print(expense)


            balance = budget.get_balance()
            print(f"Balance: £{balance}")

            pass

        elif choice == "3":
            budget.save_to_file("budget_data.txt")
            print("Saved! Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
