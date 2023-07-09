keep_going='y'
while keep_going=='y':
    sales=float(input('Enter the amount of sales:'))
    comm_rate=float(input('Enter the amount of sales'))
    commission=sales*comm_rate
    print('the commission is $ ',commission)
    keep_going=input('do you want to calculate another commission(enter y for yes):')
