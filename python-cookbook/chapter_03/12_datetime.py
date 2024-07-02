from datetime import datetime, timedelta

a = datetime(2024, 7, 2)
print(a.year, a.month, a.day, a.hour, a.minute, a.second)
print(a, a.date(), a.time())

b = timedelta(22, 55, 100)
print(b, b.days, b.seconds, b.microseconds)

print(a + b)
