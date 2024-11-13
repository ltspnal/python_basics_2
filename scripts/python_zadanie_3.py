import math

def calculate_orbital_period(R, v):
    return (2 * R * math.pi) / v

print("Введите данные для первой планеты:")
R1 = float(input("Радиус орбиты (в миллионах километров): ")) * 1_000_000
v1 = float(input("Орбитальная скорость (в км/ч): "))

print("\nВведите данные для второй планеты:")
R2 = float(input("Радиус орбиты (в миллионах километров): ")) * 1_000_000
v2 = float(input("Орбитальная скорость (в км/ч): "))

L1 = calculate_orbital_period(R1, v1)
L2 = calculate_orbital_period(R2, v2)

L1_days = L1 / 24
L1_years = L1_days / 365.25

L2_days = L2 / 24
L2_years = L2_days / 365.25

print("\nРезультаты:")
print(f"Длина года на первой планете: {L1_years:.2f} земных лет.")
print(f"Длина года на второй планете: {L2_years:.2f} земных лет.")

if L1_years > L2_years:
    print("Год на первой планете длиннее, чем на второй.")
elif L1_years < L2_years:
    print("Год на второй планете длиннее, чем на первой.")
else:
    print("Длина года на обеих планетах одинаковая.")