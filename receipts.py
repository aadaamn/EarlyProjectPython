#loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254

#stylist settle
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

#lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

#tax
sales_tax = 0.088

#customer one
customer_one_total = 0
customer_one_itemization = ""

#customer beli loveseat 
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

#customer beli lampu
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#sales tax
customer_one_tax = customer_one_total * sales_tax

#total include tax'
customer_one_total += customer_one_tax

#print 
print("Customer One Items : " + customer_one_itemization + "\n")
print("Customer One Total : " + str(customer_one_total) + "\n")