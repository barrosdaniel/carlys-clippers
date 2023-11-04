hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1) Calculate the average price of a cut.
total_price = 0
for price in prices:
    total_price += price
number_of_prices = len(prices)

average_price = total_price / number_of_prices

print(f"Avergage Haircut Price: \n{average_price:.2f}")

new_prices = [price - 5 for price in prices]
print(new_prices)