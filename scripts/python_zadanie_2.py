import math

i = float(input("Введите годовую процентную ставку (в %): "))
s = float(input("Введите сумму займа (в рублях): "))
n = int(input("Введите количество месяцев: "))

p = i / 12 / 100

m = s * p * (1 + p) ** n / ((1 + p) ** n - 1)

total_payment = m * n
overpayment = total_payment - s

print("\nРезультаты расчёта:")
print(f"Ежемесячная выплата: {m:.2f} руб.")
print(f"Общая сумма выплат: {total_payment:.2f} руб.")
print(f"Переплата по кредиту: {overpayment:.2f} руб.")