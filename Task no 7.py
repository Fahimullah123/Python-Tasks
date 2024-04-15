 #Calculate the compound interest for a given principal 
# amount, interest rate, and time period


def compound_interest(principal, rate, time, compound_frequency):

    amount = principal * (1 + rate/compound_frequency) ** (compound_frequency * time)
    return amount

# Example usage
principal_amount = 1000  # in dollars
annual_interest_rate = 0.05  # 5% annual interest rate
investment_time = 5  # 5 years
compounding_frequency = 12  # compounded monthly

# Calculate compound interest
result = compound_interest(principal_amount, annual_interest_rate, investment_time, compounding_frequency)
print("The amount of money accumulated after 5 years with monthly compounding:", round(result, 2))
