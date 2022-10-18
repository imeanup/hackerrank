import calendar
m, d, y = input().split(" ")
M, D, Y = int(m), int(d), int(y)
val = calendar.weekday(Y, M, D)
print(calendar.day_name[val].upper())
