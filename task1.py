money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0 # Месяцы без долгов

while True:
    delta = spend - salary
    if delta > money_capital:
        break
    money_capital -= delta
    spend += spend * increase
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
