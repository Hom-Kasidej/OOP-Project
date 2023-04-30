import datetime

start = datetime.datetime.now()

print(start)

end = datetime.datetime.now() + datetime.timedelta(days=3)

print(end)

print(type((end - start).days))