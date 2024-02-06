import datetime
pazarsayısı=0
for yıl in range(1901,2001):
    for ay in range(1,13):
        if datetime.date(yıl,ay,1).isoweekday()==7:
            pazarsayısı+=1
print(pazarsayısı)
