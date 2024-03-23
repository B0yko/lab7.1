import math
#Task 1
class BankAccount:
    def __init__(self, account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")


if __name__ == "__main__":
    account_holder_name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")

    account = BankAccount(account_holder_name, account_number)

    deposit_amount = float(input("Enter deposit amount: "))
    account.deposit(deposit_amount)

    withdraw_amount = float(input("Enter withdrawal amount: "))
    account.withdraw(withdraw_amount)

    account.display_balance()

#Task 2
class Vector:
    def __init__(self, components):
        self.components = components

    def magnitude(self):
        return math.sqrt(sum(component ** 2 for component in self.components))

    def add(self, vector):
        if len(self.components) != len(vector.components):
            raise ValueError("Vectors must have the same number of components.")

        result_components = [self.components[i] + vector.components[i] for i in range(len(self.components))]
        return Vector(result_components)

    def dot_product(self, vector):
        if len(self.components) != len(vector.components):
            raise ValueError("Vectors must have the same number of components.")

        return sum(self.components[i] * vector.components[i] for i in range(len(self.components)))

if __name__ == "__main__":
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([4, 5, 6])

    sum_vector = vector1.add(vector2)
    print("Sum of vectors:", sum_vector.components)

    print("Magnitude of vector 1:", vector1.magnitude())
    print("Magnitude of vector 2:", vector2.magnitude())

    dot_product = vector1.dot_product(vector2)
    print("Dot product of vectors:", dot_product)

#Task 3
class Employee:
    def __init__(self, name, id_number, department):
        self.name = name
        self.id_number = id_number
        self.department = department

    def display(self):
        print("Employee Information:")
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")


if __name__ == "__main__":
    name = input("Enter employee's name: ")
    id_number = input("Enter employee's ID number: ")
    department = input("Enter employee's department: ")

    employee = Employee(name, id_number, department)

    employee.display()
