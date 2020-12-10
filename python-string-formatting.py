# python string formatting
# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))

# python string with 2 decimals
# price = 49
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))

# python multiple values

# quantity = 100
# itemno = 45
# price = 90
# txt = "I want {} pieces of item number {} for {:.2f} dollars"
# print(txt.format(quantity, itemno, price))

#python string formatting with index numbers

# quantity = 100
# itemno = 45
# price = 90
# txt = "I want {0} pieces of item number {} for {:.2f} dollars"
# print(txt.format(quantity, itemno, price))

#python string formatting with named indexs

myorder = "I have a {carname} with model {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))



