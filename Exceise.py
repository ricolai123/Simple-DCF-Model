def calculate_DCF(cashflows, discount_rate):
    """
    cashflows = List of cash inflows for future periods
    discount_rate = The rate used to discount future cash flows to present value
    """
    DCF = 0
    for i in range(len(cashflows)):
        DCF += cashflows[i] / ((1 + discount_rate) ** (i + 1))
    return DCF

# Get user input for cash flows
num_of_cashflows = int(input("Enter the number of cashflows: "))
growth_rate = float(input("Enter the growth rate (as a decimal): "))
cashflows = []
discount_rate = float(input("Enter the WACC (as a decimal): "))
total_shares = float(input("Enter the total number of shares: "))
Debt = float(input("Enter the Debt: "))
Cash = float(input("Enter the Cash: "))
current_price = float(input("Enter the current price of stock: "))


first_year_cashflow = float(input("Enter cashflow for year 1: "))

for i in range(num_of_cashflows):
    cashflow = first_year_cashflow * (1 + growth_rate) ** i
    discounted_cashflow = cashflow / ((1 + discount_rate) ** (i + 1))
    print(f"Discounted cashflow for year {i+1}: {discounted_cashflow}")
    cashflows.append(discounted_cashflow)

FCFn = cashflows[-1]

Vn = (1+ growth_rate) * FCFn /(discount_rate - growth_rate)


DCF = sum(cashflows) + Vn /( 1 + discount_rate ) ** num_of_cashflows
Fair_Value_per_Share = ((DCF - Debt + Cash) / total_shares)
potencial_upside = ((Fair_Value_per_Share - current_price)/current_price)*100

print("Value for the first 10 years: {:.2f} in million".format(Vn))
print("Number of shares{:.2f}".format(total_shares))
print("The Discounted Cash Flow (DCF) value is: ", DCF)
print("Fair value per share = {:.2f}".format(Fair_Value_per_Share))
print("Potencial upside:{:2f} % ".format(potencial_upside))
