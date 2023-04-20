# Programme allowing user to access two financial calculators
# Investment calculator to calculate interest earnt from an investment
# Bond calculator to calculate interest to pay on a home loan
import math

# Functions
# check_float() requires a float to be entered by user to continue
def check_float(num=0):
    while True:
            try:
                num = float(num)
            # Requests time as a float as we can only process a number for this calculation
            except: 
            # If a float is not input the except triggers and loops back to try
                num = input("I did not understand that, please enter a number only: ")
            else: 
            # The input was successfully parsed. We're ready to exit the loop.
                return num

# investment() takes inputs from the user and sends them to simple or compound to calculate the interest depending on selection
def investment():
    print("\nInvestment Calculator")
    print("We need some information from you to calculate your investment return.")
    print("Please enter numbers only. E.g. enter 16.99 not £16.99 or enter 10 not 10%")
        # Request numerical variables and use check_float() to ensure user enters correct data type  
    deposit_request = input("Input the amount of money you are depositing: ")
    deposit_amount = check_float(deposit_request)
    rate_request = input("Please enter the interest rate percentage (exclude % sign): ")
    interest_rate  = check_float(rate_request)
    time_request = input("Enter the whole number of years you will invest: ")
    invest_time  = check_float(time_request)
    interest_type = input("Enter 'simple' for simple interest or 'compound' for compound interest: ")
    
    # Validate interest_type choice and run function based on selection
    while True:
        if interest_type.lower() == "simple":
            print("Simple selected")
            simple(deposit_amount, interest_rate, invest_time)
            break
        if interest_type.lower() == "compound":
            print("Compound selected")
            compound(deposit_amount, interest_rate, invest_time)
            break
        else:
            interest_type = input("Enter 'simple' for simple interest or 'compound' for compound interest: ")
 
# simple() calculates the simple interest based on input from investment()
def simple(amount, rate, time):
    # Round time to a whole year
    time = round(time) 
    # Calculate simple interest using formula A = P*(1 +r*t)
    simple_interest = amount * (1 + ((rate/100) * time)) 
    # Round simple interest to two decimal places
    simple_interest = round(simple_interest, 2)

    print("")
    print("Simple interest")
    print(f"Initial deposit: \t{amount}")
    print(f"Years saved: \t\t{time}")
    print(f"Interest rate: \t\t{rate}%")
    print(f"New balance: \t\t{simple_interest}")

# compound() calculates the compound interest based on input from investment()
def compound(amount, rate, time):
    # Round time to a whole year
    time = round(time)  
    # Calculate simple interest using formula A = P*(1 +r)^t
    compound_interest = amount * math.pow((1 + rate/100), time) 
    # Round simple interest to two decimal places
    compound_interest = round(compound_interest, 2)

    print("")
    print("Compound interest")
    print(f"Initial deposit: \t{amount}")
    print(f"Years saved: \t\t{time}")
    print(f"Interest rate: \t\t{rate}%")
    print(f"New balance: \t\t{compound_interest}")

# bond() calculates the amount you will have to pay on a home loan.
def bond():
    print("\nBond Interest Calculator")
    print("We need some information from you to calculate the interest on your loan.")
    print("Please enter numbers only. E.g. enter 16.99 not £16.99 or enter 10 not 10%")
    
    # Request numerical variables and use check_float ensure user enters correct data type  
    value_request = input("Input current balance of loan: ")
    value_amount = check_float(value_request)
 
    rate_request = input("Please enter the annual interest rate (exclude % sign): ")
    annual_interest  = check_float(rate_request)
    
    time_request = input("Enter the number of months you will take to repay: ")
    repay_time  = check_float(time_request)
    
    # Calculate monthly interest
    monthly_interest = (annual_interest/100)/12
    # Calculate monthly repayment
    repayment = (monthly_interest * value_amount)/(1- (1 + monthly_interest)**(-repay_time))
    repayment = round(repayment, 2)
    # Calculate the total amount that will be repaid
    total_repaid = round(repayment*repay_time,2)
 
    print("")
    print("Bond Interest Calculator")
    print(f"Loan balance: \t\t{value_amount}")
    print(f"Interest rate: \t\t{annual_interest}%")
    print(f"Repayment period: \t{repay_time} months")
    print(f"Montly repayment: \t{repayment}")
    print(f"Total amount repaid: \t{total_repaid}")
    return

 
# Programme 
print("Finance Calculators")
print("investment - to calculate the amount of interest you will earn on your investment.") 
print("bond       - to calculate the amount you will have to pay on a home loan.") 
# User instructions to access the required calculator
calculator_option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Validate choice 
while True:
    if calculator_option.lower() == "investment":
        print("Investment selected")
        investment()

        # User given option to calculate again or exit programme
        restart = input("Would you like to calculate again? Yes or No: ")
        while restart.lower() == "yes":
            investment()
            restart = input("Would you like to calculate again? Yes or No: ")
        else: 
            break
        
    if calculator_option.lower() == "bond":
        print("bond selected")
        bond()

        # User given option to calculate again or exit programme
        restart = input("Would you like to calculate again? Yes or No: ")
        while restart.lower() == "yes":
            bond()
            restart = input("Would you like to calculate again? Yes or No: ")
        else: 
            break
    else:
        # If 'bond' or 'investment' not input request again and loop
        calculator_option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

print("\nThank you for using Finance Calculators")