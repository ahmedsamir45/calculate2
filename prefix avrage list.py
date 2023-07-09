# big oh of the prefix_avrage2 is n square
def prefix_avrage2(s):
    n = len(s)
    a = [0]*n
    for j in range(n):
        a[j] = sum(s[0:j+1])/(j+1)
    return a

s =[]
t='y'
while t=='y':
    x = int(input('enter number to append : '))
    s.append(x)
    t = input('if you want to append again enter y else enter any buttom : ')


print("list : ",s)
print("prefix_avrage : ",prefix_avrage2(s))
