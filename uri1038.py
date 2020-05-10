# URI 1038
"""
Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.
"""



print("CODE     SPECIFICATION       PRICE")
print("1        Cachorro Quente     R$ 4.00")
print("2        X-Salada            R$ 4.50")
print("3        X-Bacon             R$ 5.00")
print("4        Torrado simples     R$ 2.00")
print("5        Refrigerante        R$ 1.50")

x,y = input().split()

product_code = int(x)
quantity = int(y)

if product_code == 1:
    price = 4.00*quantity
    print("Total: R$ %.2f" %price)
elif product_code == 2:
    price = 4.50*quantity
    print("Total: R$ %.2f" %price)
elif product_code == 3:
    price = 5.00*quantity
    print("Total: R$ %.2f" %price)
elif product_code == 4:
    price = 2.00*quantity
    print("Total: R$ %.2f" %price)
elif product_code == 5:
    price = 1.50*quantity
    print("Total: R$ %.2f" %price)
else:
    exit()
