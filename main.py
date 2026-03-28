import pywhatkit as kit
import math
import pyautogui
import time
import matplotlib.pyplot as plt
print("=======================================================")
print("Welcome to the bank loan management system")
print("=======================================================")

print("\n--- USER REGISTRATION ---")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
phone = input("Please enter your phone number: ")
monthly_income = int(input("Please enter your monthly income: "))

print("\n--- AGE & INCOME VERIFICATION ---")
if age < 21:
    print("Loan Rejected: Age must be at least 21")
    exit()

if monthly_income < 20000:
    print("Loan Rejected: Monthly Income must be at least 20000")
    exit()

print("Eligibility Verification Sucessfully")

print("\n--- Loan Details Input---")
loan_amount = int(input("Please enter your loan amount: "))
annual_interest_rate = float(input("Please enter your annual interest rate (%): "))
loan_years = int(input("Please enter your loan years: "))

monthly_interest_rate = annual_interest_rate / (12*100)
total_months = loan_years * 12

emi = (loan_amount * monthly_interest_rate * math.pow(1+monthly_interest_rate, total_months))/(math.pow(1+monthly_interest_rate, total_months)-1)
total_payment = emi * total_months
total_interest = total_payment - loan_amount

print("\n--- Loan Summary ---")
print("Customer name: ", name)
print("Total loan amount: ", loan_amount)
print("Interest rate: ", annual_interest_rate, "%")
print("Total years: ", loan_years, "years")
print("Monthly EMI: ", round(emi,2))
print("Total Interest: ", round(total_interest,2))
print("Total Final Payment: ", round(total_payment,2))

remaining_balance = loan_amount
balance_list = []
month_list = []

for month in range(1, total_months + 1):
    interest_component = remaining_balance * monthly_interest_rate
    principal_component = emi - interest_component
    remaining_balance -= principal_component

    if remaining_balance < 0:
        remaining_balance = 0

    balance_list.append(remaining_balance)
    month_list.append(month)

plt.figure()
plt.plot(month_list, balance_list)
plt.xlabel("Months")
plt.ylabel("Remaining Loan Balance")
plt.title("Loan EMI Repayment Chart")
plt.grid(True)
plt.show()

message = f"""
Hello {name},

Your Loan is APPROVED!!!

Loan Amount: ₹{loan_amount}
Interest Rate: {annual_interest_rate}%
Tenure: {loan_years} years

Monthly EMI: ₹{round(emi, 2)}
Total Interest: ₹{round(total_interest, 2)}
Total Payable Amount: ₹{round(total_payment, 2)}

Thank you for choosing our bank.
"""

print("\n Sending WhatsApp notification")
time.sleep(2)
kit.sendwhatmsg_instantly(phone,message, wait_time=15)
pyautogui.press('enter')
print("\n WhatsApp notification sent successfully")
print("Thank you for chossing our bank.")
