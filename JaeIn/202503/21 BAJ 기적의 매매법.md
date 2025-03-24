```python
N = int(input())

sp = list(map(int , input().split()))

j_cash = N
j_stock = 0

for price in sp:
    if j_cash >= price:
        j_stock += j_cash // price
        j_cash %= price


j_total = j_cash + (j_stock * sp[-1])


s_cash = N
s_stock = 0

plus_check = 0
minus_check = 0


for i in range(1 , 14):
    if sp[i] > sp[i - 1]:
        plus_check += 1
        minus_check = 0
    elif sp[i] < sp[i - 1]:
        minus_check += 1
        plus_check = 0
    else:
        plus_check = 0
        minus_check = 0


    if plus_check == 3 and s_stock > 0:
        s_cash += s_stock * sp[i]
        s_stock = 0

    elif minus_check == 3 and s_cash >= sp[i]:
        s_stock += s_cash // sp[i]
        s_cash %= sp[i]

s_total = s_cash + (s_stock * sp[-1])


if j_total > s_total:
    print('BNP')
elif j_total < s_total:
    print('TIMING')
else:
    print("SAMESAME")




```
