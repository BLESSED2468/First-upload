
from datetime import date
raw_log = "  2026-05-04 |  user_jdoe  |  LOGIN_SUCCESS  | IP:192.168.1.1 "

"""
STRING CLEANING
 Remove the leading/ trailing whitespace and split the data into individual component 
 (Date, username, status, ip).

 """
trimmed_raw_log = raw_log.strip()
data_components_list = trimmed_raw_log.split("|")


"""
Data transformation:
    
    -The username must be converted to all uppercase
    -The ip address must be extracted without the ip: prefix
"""

username = data_components_list[1].strip()
access_date = data_components_list[0].strip()
ip_address= data_components_list[3].strip()

#extract the real username from the username in the raw log
real_name = username.split("_")[1].upper()
real_ip_address= ip_address.split(":")[1]

real_date_object = date.fromisoformat(access_date)
final_date = real_date_object.strftime("%d/%m/%Y")

end_year = date(2026 ,12 ,31)
days_left = (end_year - real_date_object).days

print( f"[SECURITY ALERT]: User {real_name} accessed from {real_ip_address} on {final_date}. Days remaining in year: {days_left}.")
"""

raw_log = "  2026-05-04 |  user_jdoe  |  LOGIN_SUCCESS  | IP:192.168.1.1 "


STRING CLEANING
 Remove the leading/ trailing whitespace and split the data into individual component 
 (Date, username, status, ip)."""

"""
Data transformation:
    
    -The username must be converted to all uppercase
    -The ip address must be extracted without the ip: prefix
"""

raw_log = "  2026-05-04 |  user_jdoe  |  LOGIN_SUCCESS  | IP:192.168.1.1 "

log_cleaning = raw_log.strip()
clean_data = log_cleaning.split("|")

date_str = log_cleaning[0].strip()
user_name = log_cleaning[1].strip()
ip_log = log_cleaning[3].strip()

name = user_name.replace("user","_").strip().upper()
ip = ip_log.replace("IP",":").strip()

from datetime import datetime 
date_str = date.fromisoformat(access_date)

final_date = date_str.strftime("%d/%m/%Y")

end_year = date(2026, 11, 30)
days_left = (end_year - date_str).days

print(days_left)
