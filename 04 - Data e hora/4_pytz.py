from datetime import datetime

import pytz

data0 = datetime.now(pytz.UTC)
data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)
print(data0)
