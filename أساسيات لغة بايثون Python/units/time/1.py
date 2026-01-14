from datetime import date
time=date(2025,11,21)
print(time)
today = date.today()
some_day = date .fromordinal(777777)
print(some_day)
another_day =date.fromisoformat('2025-11-30')
print(another_day)
day_to_worldcup = time-today
print(day_to_worldcup)
print(type(day_to_worldcup))