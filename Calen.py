import calendar

# Вводим год и месяц
year = int(input("Введите год: "))
month = int(input("Введите месяц: "))

# Генерируем календарь для указанного года и месяца
cal = calendar.month(year, month)

# Выводим календарь на экран
print("\n", cal)
