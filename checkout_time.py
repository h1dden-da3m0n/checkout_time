from datetime import timedelta, datetime as dt

x = int(input("Max h / day > "))

a = input("1st Start Time (##:##)> ")
morning_start = dt.strptime(a, "%H:%M")

b = input("1st End Time (##:##)> ")
morning_end = dt.strptime(b, "%H:%M")

c = input("2nd Start Time (##:##)> ")
afternoon_start = dt.strptime(c, "%H:%M")

chechout_at = afternoon_start + (timedelta(hours=x) - (morning_end - morning_start))
print("Time to go >>", chechout_at.time())
