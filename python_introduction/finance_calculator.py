#Monthly savings
#Assign value to variable

rate = 5

#Prompting for user input

monthly_income = float(input("Enter your monthly income: "))

total_monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = total_monthly_expenses - monthly_income


#annual savings with 5% rate of interest
yearly_savings = monthly_savings * 12 
projected_savings = yearly_savings + (yearly_savings * 0.05)


#Display results

print(f"Your monthly savings are  ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")




