from decimal import Decimal

# On the first run, input the starting numbers
principle = Decimal(input("Enter the starting balance of your mortgage:"))
rate = (Decimal(input("Enter your yearly interest rate:"))/100)
term = int(input("Enter the length of your mortgage (in years):"))

# Count is so that when calc_mortgage() is called repeatedly (which it is), it won't continually decrease the monthly payment amount.
count = 0

def calc_mortgage():
	global principle,payment,count
	if count == 0:
		payment = principle*((rate/12)*((1+(rate/12))**(term*12)))/(((1+(rate/12))**(term*12))-1)
		payment = round(payment, 2)
		count += 1
	return print('Your monthly payment is: $', payment)
	return payment

def calc_princ_payment():
	global principle,payment,principle_payment,interest_payment
	return calc_mortgage()
	interest_payment = (principle*(rate))/12
	principle_payment = Decimal(payment) - Decimal(interest_payment)
	return principle,principle_payment,interest_payment

def apply_payment(principle):
	global principle_payment
	return calc_princ_payment()
	principle = principle - principle_payment
	return principle,principle_payment
	
amoritization = {}
for year in range(2020,2051,1):
	for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
		if principle > 0:
			apply_payment(principle)
			x = month + str(year)
			amoritization[x] = float(principle)
			print(month + " " + str(year) + " " + str(principle))
		else:
			pass