from datetime import datetime, timedelta
delta = timedelta(days=20 , seconds=47 , minutes= 3 , hours= 3 , weeks= 4)
now = datetime.now ()
print(now- delta)

print(now.strftime())