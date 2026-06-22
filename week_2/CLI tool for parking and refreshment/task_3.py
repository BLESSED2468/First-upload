#this enables the python to understand time without it, the python will think its an ordinary text
from datetime import datetime

#what this does is for example if the the user spends 1hr:30min it  turn into two 2hr because parking only charges full hours
import math
"""
The Scenario: You are building a CLI tool for the front desk to bill clients for refreshments and parking.

guests = 6
refreshment_price = 12.50
arrival = 09:20
department = 10:30
"""

#user is to input the number of guest and the int make it possible to accept integers
guest = int(input("Enter number of guest").strip())

#Empty total. This acts like an empty container to store money
subtotal =0

#This loops through each guest.eg
#if guest = 2, python does:
#guest 1:
#guest 2:  it repeats the question depending on the number of guest inputed
for i in range(1, guest + 1):

#enables user input on prices , and where making use of float because money have decimals
    price = float(input(f"Enter refreshment_price for guest {i}: ").strip())
subtotal += price

#the user is to input the time of arrival and strip removes any spacing by user
arrival = input("Enter time of arrival").strip()

#the user is to input time of departure
departure = input("Enter time of departure").strip()

#this multiplies the number of guest and price  after input
subtotal = (guest * price)

#if the user input more than 5 it give a discount of 10%
if guest >5:
    subtotal *= 0.10

#this converts the input into real time format that python understands
arrival_time = datetime.strptime(arrival, "%H:%M")
departure_time= datetime.strptime(departure, "%H:%M")

#finds the duration by subtracting the arrival and departure time
duration = departure_time - arrival_time

#converts into minutes
total_minutes = duration.seconds / 60
#converts into hours
parking_hours = math.ceil(total_minutes /60)
#this is the parking fee
parking_fee = parking_hours *5

grand_total = subtotal + parking_fee
tax = grand_total * 0.010
total_due = grand_total + tax

print("="*31)
print(f"{"OFFICE RECEIPT":^31}")
print("="*31)
print(f"{"refreshments:":<20} {subtotal:>7.2f}")
print(f"{"parking_fee:":<20} {parking_fee:>7.2f}")
print(f"{"tax (7.5):":<20} {tax:>7.2f}")
print("_"*31)
print(f"{"TOTAL DUE:":<20} {total_due:>7.2f}")
print("="*31)