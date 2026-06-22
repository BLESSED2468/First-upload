#what this does is import special tools from python liberary that help work with dates and times
from datetime import datetime, timedelta

#imports a library of mathematical functions 
import math

# This receives user start input and removes any spacing that the user adds to the starting or ending of there input
start_input = input("Enter project start date(YYYY-MM-DD): ").strip()

# This takes in the total work hours and converts it to an integer and removes any spacing made by the user
total_hours = int(input("Enter total estimated work hour").strip())

# Takes the user input on hourly rates and turns it to a float and remove spacing
hourly_rate = float(input("Enter Hourly rate: ").strip())

#Takes in the user input and turns it into readable format 

start_date = datetime.strptime(start_input, "%Y-%m-%d").date()

# multiplies the total
total_cost = total_hours * hourly_rate
workdays_needed = math.ceil(total_hours / 8)
completion_date = start_date + timedelta(days=workdays_needed)

if completion_date.weekday() ==5:
    completion_date += timedelta(days=2)

elif completion_date.weekday() ==6:
    completion_date += timedelta(days=1)
    
print(f"total project cost: ${total_cost:.2f}")
print(f"project completion date: {completion_date.strftime("%A, %B, %d, %Y")}")

