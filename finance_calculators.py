# Description of available options supported by the calculator
# Investment/bond options within loop so program repeat asks if incorrect input received
# Checks for bond or investment and calculates accordingly
# Prints results within full sentence

import math  

print("This is a calculator designed to help calculate investments and bonds")
print("\ninvestment - to calculate the amount of interest you'll earn on your investment ")
print("\nbond - to calculate the amount you'll have to pay on a home loan")

while True:
    answer = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ")
    answer = answer.lower()

    if answer == "bond":
        house_value = int(input("\nEnter the present value of the house numerically: "))
        interest_rate = int(input("\nEnter the interest rate as a number: "))
        months = int(input("\nEnter the number of months over which you will repay the bond: "))
        interest_rate = (interest_rate / 100) / 12                                          
        repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (- months)) 
        print("\nYou will have to repay {} per month to pay back the loan".format(repayment))
        break

    elif answer == "investment":
        deposit = int(input("\nEnter the amount of money you are depositing: "))
        interest_rate = int(input("\nEnter the interest rate as a number: "))
        years_invested = int(input("\nEnter the amount of years you plan to invest: "))
        while True:

            interest_type = input(
            "\nPlease enter the type of interest you would like to use: 'simple' or 'compound': ")
            interest_type = interest_type.lower()
            if interest_type == "simple":
                interest_rate = interest_rate / 100
                new_total = deposit * (1 + interest_rate * years_invested)
                print("\nYou will get back {} after {} years of investment" \
                      .format(new_total, years_invested))
                break
            elif interest_type == "compound":
                interest_rate = interest_rate / 100
                new_total = deposit * math.pow((1 + interest_rate), years_invested)
                print("\nYou will get back {} after {} years of investment" \
                      .format(new_total, years_invested))
                break
            else:
                print("\nYou have not entered a valid answer. Please try again")
        break
    else: 
        print("\nYou have not entered a valid answer. Please try again")
