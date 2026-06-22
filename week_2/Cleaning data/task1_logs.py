#*The Scenario:** Our server generates raw logs that are often "dirty" with irregular spacing. You must extract key security information and perform a quick time-based calculation.
raw_log = "  2026-05-04 |  user_jdoe  |  LOGIN_SUCCESS  | IP:192.168.1.1 "

clean_log = raw_log.strip()
part = clean_log.split("|")

date_str = part[0].strip()
username = part[1].strip()
status = part[2].strip()
ip = part[3].strip()

username = username.replace("user_","").upper()
ip = ip.replace("IP:","")

from datetime import datetime, date
log_day = datetime.strptime(date_str, "%Y-%m-%d").date()

end_year = date(2026 ,12 ,31)
days_left = (end_year - log_day).days

print(f"[SECURITY ALERT]: User {username} accessed from {ip} on {log_day.strftime("%Y/%m/%d")}. Days remaining in year: {days_left}.")



#*The Scenario:** Our server generates raw logs that are often "dirty" with irregular spacing. You must extract key security information and perform a quick time-based calculation.
