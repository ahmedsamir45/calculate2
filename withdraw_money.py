
def withdraw_money(current_balance,amount):
    if current_balance >= amount :
        current_balance = current_balance - amount
        return current_balance


current_balance =int(input('enter current_balance : '))
amount = int(input('enter amount : '))

balance = withdraw_money(current_balance,amount)

if balance <= current_balance/2  :

    print("we need to make a deposit  ")

else:
    print('your curren_balance now = ',balance)
