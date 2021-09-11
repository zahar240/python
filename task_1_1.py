minute = 60
hour = minute * 60
day = hour * 24

# Пользовательский ввод
duration = int(input("Введите целое положительное число: "))

duration_second = duration % minute
duration_minute = duration % day % hour // minute
duration_hour = duration % day // hour 
duration_day = duration // day

print(f"{duration_day} дн {duration_hour} час {duration_minute} мин {duration_second} сек")

# Входные данные - списк
durations_list = [12345678, 54, 4000, 2100, 100100, 0]

# Вывод вариант 1
for duration in durations_list:
    duration_second = duration % minute
    duration_minute = duration % day % hour // minute
    duration_hour = duration % day // hour 
    duration_day = duration // day
    print(f"{duration_day} дн {duration_hour} час {duration_minute} мин {duration_second} сек")

# Вывод вариант 2
for duration in durations_list:
    duration_second = duration % minute
    duration_minute = duration % day % hour // minute
    duration_hour = duration % day // hour 
    duration_day = duration // day
    if duration == 0:
        print(f"Временной отрезок равен 0")
    elif duration < minute:
        print(f"{duration_second} сек")
    elif duration < hour:
        print(f"{duration_minute} мин {duration_second} сек")
    elif duration < day:
        print(f"{duration_hour} час {duration_minute} мин {duration_second} сек")
    else:
        print(f"{duration_day} дн {duration_hour} час {duration_minute} мин {duration_second} сек")