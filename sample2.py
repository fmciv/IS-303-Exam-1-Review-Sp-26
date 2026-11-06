def get_category():
    return input("Expense category: ")


def get_description():
    return input("Describe the expense: ")


def get_cost():
    return float(input("Amount: "))


# Collect all expenses.
def get_expenses():
    expenses = []

    while True:
        category = get_category()

        # A blank category ends expense entry.
        if category == "":
            break

        description = get_description()
        cost = get_cost()

        # Group one expense's information together.
        expense = [category, description, cost]
        expenses.append(expense)

    # Return all expenses after the loop finishes.
    return expenses


def secret_category_function():
    return input("What category do you want to report on? ")


def print_list(expenses, secret_category):
    print(f"Summary of expenses for {secret_category}")

    total = 0

    # Read the three values stored in each expense.
    for category, description, cost in expenses:
        if category == secret_category:
            print(f"${cost} - {description}")
            total += cost

    print(f"Total: ${round(total, 2)}")


def main():
    expenses = get_expenses()
    secret_category = secret_category_function()
    print_list(expenses, secret_category)


if __name__ == "__main__":
    main()