from datetime import datetime
import time

dt = datetime(2020, 1, 1)
dt = datetime.now()
dt=datetime.strptime("2024/02/02" , "%Y/%m/%d")
dt=datetime.fromtimestamp(time.time())
print(dt)

