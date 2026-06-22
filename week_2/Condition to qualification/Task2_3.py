"""
 This task is about a fintech app to see if a user is qualified to take a loan from the app
"""
age = int(input("Enter age: "))
credit_score = int(input("Enter ur credit score"))
monthly_income = int(input("Hw much do u earn monthly"))

#this contains three gates : the age conditon , credit score and monthly income
#for the age if the user input is less than 21 that is a disqualificaton 
#in the credit score section uses the comparing operator to check if everthing meets the
# condition to qualify
#what happen here is the conditions are combined into a boolean with logical operator


conditions = (age >=21) and ((credit_score > 700) or (credit_score>600 and monthly_income >5000)) and not (monthly_income < 1500)
print("loan qualification status:", conditions)