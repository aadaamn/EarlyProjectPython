hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Total price
total_price = 0
for harga in prices:
  total_price += harga

# Average price per cut
average_price = total_price / len(prices)
print("Average Haircut Price:" , average_price)

# New price
new_prices = [harga - 5 for harga in prices]
print(new_prices)


# Total Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:" , total_revenue)


# Average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:" , average_daily_revenue)


# Cuts under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)
