#Exception
'''
devision by zero

'''

#try block

# try:
#     number =int(input("Enter number"))
#     result = 100/number
# except ZeroDivisionError:
#     print("cannot devide by zero")

# except ValueError:
#     print("invalid number entered.")

# try:
#     file =open("student.json")
#     print("file missing")

# except FileNotFoundError:
#     print("file found")

# finally:
#     print("finished opening")


#ATM Withdraw

class InsufficientBalance(Exception):
    pass
balance =2000000
withdraw = int(input("Amount: "))

try:
    if withdraw>balance:
        print