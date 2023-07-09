def factorial(x):
    y=1
    for i in range(1,x+1):
        y=y*i
    print('factorial',x,'=' , y)

again='k'
while again=='k':   
    n=int(input('enter number for factorial :'))

    factorial(n)
    again=input('do you want to calculate another factorial (enter k for yes): ')


