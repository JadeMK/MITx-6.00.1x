"""
write a program that calculates the minimum fixed monthly payment needed in
order pay off a credit card balance within 12 months. By a fixed monthly
payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.

e.g.,
balance = 3926
annualInterestRate = 0.2
"""

monthly_interest = annualInterestRate / 12
monthly_payment = 0

while balance > 0:
    # Reset the balance and iterate through 12 months
    balance_checker = balance
    for month in range(12):
        monthly_unpaid = balance_checker - monthly_payment
        balance_checker = monthly_unpaid + (monthly_interest * monthly_unpaid)
        
    # increase the value on each iteration
    if balance_checker > 0:
        monthly_payment += 10
    else:
        break

print("Lowest Payment:", monthly_payment) 
