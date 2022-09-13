#Welcome to hollow.my! plus with greetings

name = input("What is your name?\n")

print("Hi " + name + ", welcome to hollow.my!\n")

#category

category = "Tshirt , Hoodie , Outerwear , Socks\n\n"

#scammer or not

if name == "tonye" or name == "nangkoi" or name == "dimak" or "deeno":
    scammer_status = input("Are you a scammer?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if scammer_status == "yes" and good_deeds < 5:
        print("You are currently banned, " + name + "!\n" + "Big L + " +
              "Ratio")
        exit()
    else:
        print("Oh nice! You are welcomed here\n")
        print(
            name +
            ", what would you like to shop at our shop today? Here are the apparels we have in store:\n"
            + category)
else:
    print(
        name +
        ", what would you like to shop at our shop today? Here are the apparels we have in store:\n"
        + category)

#which one?
order = input("Which one would you like?\n")

#Set the price

if order == "Hoodie" or "hoodie":
    price = 169
elif order == "Tshirt" or "tshirt":
    price = 119
elif order == "Outerwear" or "outerwear":
    price = 199
elif order == "Socks" or "socks":
    price = 49

else:
 print(
        "Sorry we do not have that here, but you can suggest that via our customer service"
    )
 exit()

print("Sounds great " + name + "!\n\n" + "The price of the " + order + " is " +
      "RM" + str(price) + "\n\n")

quantity = input("How much of these would you like?\n")

total_price = int(price) * int(quantity)

#cashier
print("The total would be RM" + str(total_price))

#Use cash or credit card?

print("\n\n" +
      "Which payment method would you like to use?\nCash or credit card?")

payment_method = input("\n")

if payment_method == "credit card":
    print("There will be a 1% charge if you use credit card.")
else:
    print("Alright sure. Give me a minute")
