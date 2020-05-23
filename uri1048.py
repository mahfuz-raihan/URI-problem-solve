salary = float(input())

if(salary >= 0 and salary <= 400.00):
    percentage = "15 %"
    earned_amount = salary*0.15
    new_salary = salary + earned_amount
elif(salary >= 400.01 and salary <= 800.00):
    percentage = "12 %"
    earned_amount = salary*0.12
    new_salary = salary + earned_amount
elif(salary >= 800.01 and salary <= 1200.00):
    percentage = "10 %"
    earned_amount = salary*0.1
    new_salary = salary + earned_amount
elif(salary >= 1200.01 and salary <= 2000.00):
    percentage = "7 %"
    earned_amount = salary*0.07
    new_salary = salary + earned_amount
elif(salary > 2000.00):
    percentage = "4 %"
    earned_amount = salary*0.04
    new_salary = salary + earned_amount

print("Novo salario: %.2f" %new_salary)
print("Reajuste ganho: %.2f"%(earned_amount))
print("Em percentual: {}".format(percentage))
