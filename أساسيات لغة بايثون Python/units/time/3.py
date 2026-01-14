from datetime import datetime

world_cup_2026 = datetime(year=2026,month=11,day=21,hour=13,minute=12,second=5)
print(world_cup_2026)
now = datetime.now()
print(now)
today = datetime.today()
print(today)
world_cup_2026 = datetime.fromisoformat('2026-11-22 12:33:33')
print(world_cup_2026)
count_down = now - world_cup_2026
print('count down' , count_down)