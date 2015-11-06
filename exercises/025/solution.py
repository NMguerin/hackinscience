import datetime

jour = datetime.date.today()
heure_now = datetime.datetime.now().time()
heure = heure_now.replace(microsecond=0)
print("Today is %s and it is %s" % (jour, heure))
