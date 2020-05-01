a = list(map(float, input().strip().split()))
b = list(map(float, input().strip().split()))

a_amount = a[1]*a[2]
b_amount = b[1]*b[2]

pay = a_amount+b_amount

print('VALOR A PAGAR: R$ %.2f' %pay)
