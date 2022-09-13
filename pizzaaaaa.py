# Toppings
toppings = [ "pepperoni" , "pineapple" ,"cheese" ,"sausage" ,"olives","anchovies", "mushrooms"]

#each slice cost
prices = [2 , 6 , 1 , 3 , 2 , 7 , 2]

# 2$ slices
num_two_dollar_slices = prices.count(2)

# Length of toppings
num_pizza = len(toppings)
print("We sell" , num_pizza , "different kinds of pizza!")

#2D list
pizza_and_prices = [[2 , "pepperoni"] , [6 , "pineapple"] , [1 , "cheese"] , [3 , "sausages"] , [2 , "olives"] , [7 , "anchovies"] , [2 , "mushrooms"]]

# New topping
pizza_and_prices.insert(3 , [2.5 ,"peppers"])

# Sorting pizza in increasing price(ascending)
pizza_and_prices = sorted(pizza_and_prices)
print(pizza_and_prices)

# Cheapest pizza
cheapest_pizza = pizza_and_prices[:1]

# Anchovies shit af
pizza_and_prices.pop(-1)

# Priciest pizza
priciest_pizza = pizza_and_prices[-1:]

# Three cheapest
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)