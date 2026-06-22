"""
Our warehouse needs to ship units in large crates (12 units) and small boxes(4 unit)

So: this task is like a calculator that helps to calculate the number of crates that will be
needed for whatever unit the user has
"""

#allows for user input and converts the input to number
total_unit = int(input("Enter total unit: "))

# this then takes the input and divide it by the number of units to makes a crate which in this case is 12
large_crates = total_unit //12

#this % refers to the remainder that were left to make a crate 
remainder = total_unit % 12

#then we assign the remainders into small_boxes and divide it by 4 because its the total unit that makes up a small box
small_boxes = remainder // 4

#this then says that any unit remaining from the smallbox should be stored under losse
loose = remainder  % 4

total_cost = 0

total_cost += large_crates *50
total_cost += small_boxes *20
total_cost += loose *5

print(f"crates: {large_crates} , boxes: {small_boxes} , loose: {loose}, total_cost: ${total_cost}" )