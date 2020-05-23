salary = float(input())

if salary >= 0.00 and salary <= 2000.00:
	print("Isento")
elif salary >= 2000.01 and salary <= 3000.00:
	taxes_count1 = salary - 2000.00
	taxes = taxes_count1*0.08
	print("R$ %.2f" %taxes)
elif salary >= 3000.01 and salary <= 4500.00:
	taxes_count1 = 1000*0.08
	taxes_count2 = (salary - 3000.00)*0.18
	taxes = taxes_count1 + taxes_count2
	print("R$ %.2f"% (taxes))
elif salary > 4500.00:
	 taxes_count1 = 1000.00*0.08
	 taxes_count2 = 1500.00*0.18
	 taxes_count3 = (salary - 4500.00)*0.28
	 taxes = taxes_count1 + taxes_count2 + taxes_count3
	 print("R$ %.2f"%(taxes))
