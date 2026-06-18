#Main class - BankAccount , loan account
#Sub - Saving account - cnnot withdraw more 30k, interest
# rate - 6%
#current account - can withdraw any amount
#CA - interest rate 2% , cannot deposit more 3ook
#Loare account - cnnot withdraw

"""
main class - bankaccount
sub class - saving acount, current account, loan account
saving account - cannot withdrwan more then 30% interest 
rate 6%
current account - can withdrawn any amount
ca - interest rate 2% and , cannot deposit more theen 300k
loan account - cannot withdrawn

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.06

    def withdraw(self, amount):
        if amount > self.balance * 0.3:
            print("Cannot withdraw more than 30% of the balance")
        else:
            super().withdraw(amount)
        
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.02

    def deposit(self, amount):
        if amount > 300000:
            print("Cannot deposit more than 300k")
        else:
            super().deposit(amount)

class LoanAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self, amount):
        print("Cannot withdraw from a loan account")


saving_acc = SavingAccount("SA123", 10000)  
saving_acc.withdraw(4000)
current_acc = CurrentAccount("CA123", 5000)
current_acc.deposit(350000)
loan_acc = LoanAccount("LA123", 20000)
loan_acc.withdraw(5000)


class BankAccount:
    interest_rate = 4

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        print("Balance:", self.balance)


class SavingAccount(BankAccount):
    interest_rate = 6
    def withdraw(self, amount):
        if amount > 30000:
            print("Cannot withdraw more than 30,000")
        else:
            BankAccount.withdraw(self, amount)


class CurrentAccount(BankAccount):
    interest_rate = 2
    def deposit(self, amount):
        if amount > 300000:
            balance -= amount
            return(self.balance)
        else:
            return("can only withdraw")


class LoanAccount(BankAccount):
    def __init__(self, name, account_number, balance):
        BankAccount.__init__(self, name, account_number, balance)

    def withdraw(self, amount):
        print("Withdrawal not allowed in Loan Account")


sa = SavingAccount("Rahul", "SA101", 50000)
sa.withdraw(35000)
sa.withdraw(20000)
sa.show_balance()

ca = CurrentAccount("Amit", "CA101", 100000)
ca.deposit(350000)
ca.deposit(50000)
ca.show_balance()

la = LoanAccount("Neha", "LA101", 200000)
la.withdraw(10000)

"""

# __str__ human readable output 
# __super__ 
# runtime_errors

def show(label ,func):
    try:
        func()
    except Exception as e:
        print(f"({type(e).__name__}:{e})")

print("NameError",lambda:print(undefined_variable))
print("TypeError",lambda:"3"+5)
print("ValueError",lambda:int("abc"))
print("IndexError",lambda:[1,2,3][10]) #IndexError <function <lambda> at 0x000002370E6B35E0>
print("KeyError",lambda:{"a":1}["b"]) #KeyError <function <lambda> at 0x000002370E6B35E0>
print("ZeroDivisionError",lambda: 1/0)
print("AttributeError",lambda:"hello".push("!"))
print("FileNotFoundError",lambda:open("Does_not_exist_12345.txt"))

"""
1. NameError : Jab kisi variable ko use karo jo define hi nahi hua. 

 print(name)

Output: NameError: name 'name' is not defined

2. TypeError: Jab incompatible data types par operation karo.

num = 10
text = "20"

print(num + text)

Output: TypeError

3. ValueError:Data type sahi hai, lekin value galat hai.

age = int("hello")
print(age)

Output:ValueError

4. IndexError: List ke bahar ka index access karna.

numbers = [10, 20, 30]

print(numbers[5])

Output: IndexError

5. KeyError: Dictionary mein jo key exist nahi karti usko access karna.

student = {
    "name": "Rahul",
    "age": 20
}

print(student["city"])

Output: KeyError

6. ZeroDivisionError : Kisi number ko 0 se divide karna.
a = 10
b = 0
print(a / b)

Output: ZeroDivisionError


7. AttributeError Object mein jo attribute/method nahi hai usko call karna.

name = "Rahul"
name.append("Kumar")

Output: AttributeError
Kyuki string mein append() method nahi hota.

8. TypeError (Function Arguments)
Function ko galat number of arguments dena.

def add(a, b):
    return a + b
print(add(10))

Output:
TypeError
Kyuki function ko 2 arguments chahiye the.
Bonus: Exception Handling
In sab errors ko handle karna bhi seekho.

try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")


"""
#Value Error
def to_int(test):
    try:
        return int(test)
    except ValueError:
        return None

print(to_int(42))
print(to_int("ABC"))

#try/except/else/finally

def safe_divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print(f"{a}/{b} : cannot divide by zero")
    else:
        print(f"{a}/{b} = {result}") #true only if no exception
    finally:
        print("its Done") #finally always run
    
safe_divide(1,4)
safe_divide(1,0)
safe_divide(50,2)
    