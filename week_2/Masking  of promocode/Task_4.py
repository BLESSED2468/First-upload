""" The task is check if a user promocode is valid by meeting the conditions and masking 
    some of the the code for security reasons
"""

#this allows for user input and is where the user input is stored
code = input("Enter promo code: ")

#this has two functions 
#first: the .startwith("SAVE") this indicates the user input which is the code must begin with the letters SAVE
#second: the len(code) ==12 this means that the letters of the code must be up 12 for it to be true
# the "and " kind of acts like a bool it ensure that the conditions for both are ment for it to be true
is_valid = code.startswith("SAVE") and len(code) ==12

#then it proceeds to this part after the conditions from is_valid are true
#and masks the first four letters and last two letters
if is_valid:
    masked = code[:4] + "****" + code[-2:]
else:
    masked = "Invalid code"

print("masked code:", masked)
print("valid status", is_valid)