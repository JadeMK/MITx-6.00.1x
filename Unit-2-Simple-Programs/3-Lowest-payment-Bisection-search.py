"""
Write a program that uses these bounds and bisection search to find the smallest
monthly payment to the cent such that we can pay off the debt within a year.

if you do not use bisection search, your code will not run - your code only has
30 seconds to run on our servers

e.g.,
balance = 320000
annualInterestRate = 0.2
"""

monthly_interest = annualInterestRate / 12
low = balance / 12
high = (balance * (1 + monthly_interest) ** 12) / 12
epsilon = 0.01
balance_checker = balance

while abs(balance_checker) >= epsilon:
    balance_checker = balance
    monthly_payment = (low + high) / 2
    
    # Iterate through 12 months
    for month in range(12):
        monthly_unpaid = balance_checker - monthly_payment
        balance_checker = monthly_unpaid + (monthly_interest * monthly_unpaid)

    # Find the new middle point to continue searching
    if balance_checker > epsilon:
        low = monthly_payment
    else:
        high = monthly_payment
        
print("Lowest Payment:", round(monthly_payment, 2)) 
