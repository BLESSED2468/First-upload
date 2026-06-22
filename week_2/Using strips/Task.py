"""# the scenari0: a client sent a CSV _style string where prices are messy. you must cleana the data and validate if it belongs to a premium category.
"""

# enables user input
record = input ("Enter the product record")

#this split the txt from the user ,that is product and price using :
product, price = record.split(":")

#this removes spacing and turns it into lowercase
product = product.strip().lower()

#this is where the removal of space, $ sign and "," takes place
price = price.strip().replace("$", "" ).replace(",","")

# turns the input from user to float(converts txt to real number)
price = float(price)

# List of the premium product
luxury_list = ["laptop", "smartphone", "camera"]

#checks if the product inputed by user is on the list and the price range inputted is above or below the category
premium_product = (product in luxury_list) and (price > 1000)


print(premium_product)
