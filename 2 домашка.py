day = input('ведите день рождение')
month = input('ведите месяц')

if day.isalpha() or month.isalpha() or len(day) != 2 or len(month) != 2:
    print('вы ввели дату не правильно')

else:
    day = int(day)
    month = int(month)
    if (21 <= day <= 31 and month == 3) or (1 <= day <= 20 and month == 4):
        print('owen')
    elif (21 <= day <= 30 and month == 4) or (1 <= day <= 21 and month == 5):
        print('телец')
    elif  (22 <= day <= 31 and month == 5) or (1 <= day <= 21 and month == 6):
        print('близнецы')
    elif (22 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
        print('рак')
    elif (23 <= day <= 31 and month == 7) or (1 <= day <= 21 and month == 8):
        print('лев')
    elif (22 <= day <= 30 and month == 8) or (1 <= day <= 23 and month == 9):
        print('дева')
    elif (24 <= day <= 31 and month == 9) or (1 <= day <= 23 and month == 10):
        print('весы')
    elif (24 <= day <= 30 and month == 10) or (1 <= day <= 22 and month == 11):
        print('Скаарпион')
    elif (23 <= day <= 31 and month == 11) or (1 <= day <= 22 and month == 12):
        print('Стрелец')
    elif (23 <= day <= 30 and month == 12) or (1 <= day <= 20 and month == 1):
        print('Козерог')
    elif (21 <= day <= 31 and month == 1) or (1 <= day <= 19 and month == 2):
        print('Водолей')
    elif (20 <= day <= 28 and month == 2) or (1 <= day <= 20 and month == 3):
        print('рыбы')