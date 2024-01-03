# my = ('Fri 06 Nov 2022 10:55 00:00:01 ')

from datetime import datetime

dayText = datetime.now().strftime('%a') # hafta kuni
day = datetime.now().strftime('%d') # sana
monthText = datetime.now().strftime('%h') # oy
yearFull = datetime.now().strftime('%Y') # yil
hour = datetime.now().strftime('%H') # soat
minute = datetime.now().strftime('%M') # minut
second= datetime.now().strftime('%S') # soniya

print(dayText,day,monthText,yearFull,end=' ')
print(f"{hour}:{minute} 00:00:{second}")
