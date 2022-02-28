"""
Write a program to calculate the credit card balance after one year if a
person only pays the minimum monthly payment required by the credit card
company each month.

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
"""

# Iterate through 12 months
for month in range(12):
    interest = (balance - balance * monthlyPaymentRate) * (annualInterestRate / 12)
    balance = balance - (balance * monthlyPaymentRate) + interest

print("Remaining balance:", round(balance, 2))
