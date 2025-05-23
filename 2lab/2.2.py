salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Начальное значение подушки безопасности
current_spend = spend  # Переменная для расчета расходов

for _ in range(months):
    if salary < current_spend:
        money_capital += current_spend - salary
    current_spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))