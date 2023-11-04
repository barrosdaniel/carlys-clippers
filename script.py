hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1) Calculate the average price of a cut.
total_price = 0
for price in prices:
    total_price += price
number_of_prices = len(prices)

average_price = total_price / number_of_prices

print(f"Avergage Haircut Price: $ {average_price:.2f}")

# 2) Calculate new prices
new_prices = [price - 5 for price in prices]
print(new_prices)

# 3) Calculate revenue
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print(f"Total Revenue: $ {total_revenue:.2f}")

# 4) Calculate average daily revenue
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: $ {average_daily_revenue:.2f}")

# 5) List of cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)