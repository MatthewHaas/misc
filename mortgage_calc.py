from decimal import Decimal

# On the first run, input the starting numbers
principle = Decimal(input("Enter the starting balance of your mortgage:"))
rate = (Decimal(input("Enter your yearly interest rate:"))/100)
term = int(input("Enter the length of your mortgage (in years):"))

# Count is so that when calc_mortgage() is called repeatedly (which it is), it won't continually decrease the monthly payment amount.
#count = 0

def calc_mortgage():
	payment = principle*((rate/12)*((1+(rate/12))**(term*12)))/(((1+(rate/12))**(term*12))-1)
	payment = round(payment, 2)
	return payment
	

def calc_princ_payment():
	global payment,principle
	interest_payment = (principle*(rate))/12
	principle_payment = Decimal(payment) - Decimal(interest_payment)
	return principle_payment

def apply_payment():
	global principle,principle_payment
	principle_payment = calc_princ_payment()
	principle = principle - principle_payment
	return principle
	
amoritization = {}
#count = 0
payment = calc_mortgage()
while principle > 0:
	for year in range(2020,2050,1):
		for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
			if principle > payment:
				principle_payment = calc_princ_payment()
				principle = apply_payment()
				x = month + str(year)
				amoritization[x] = round(float(principle),2)
				print(month + " " + str(year) + " " + str(round(principle,2)))
			elif principle < payment:
				principle = 0
				x = month + str(year)
				amoritization[x] = round(float(principle),2)
				print(month + " " + str(year) + " " + str(principle))
				break
print(amoritization)