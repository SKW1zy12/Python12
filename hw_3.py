# #Задача 1
# a = 10
# b = 20
# if a < b:
#     print("20 больше")
# else:
#     print("10 больше")

# #Задача 1.2
# num = int(input("Введите число: "))
# if num > 0:
#     print("Число положительное")
# elif num < 0:
#     print("Число отрицательное")
# else:
#     print("Число равно нулю")

# #Задача 1.5
# num = int(input("Ведите число: "))
# print(abs(num))

#Задача 2
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# if num1 != num2:
#     print("Yes")
# else:
#     print("No")

#Задача 3
# num = input(input("Введите число: "))
# if num > 100 or num < -100:
#     print("-")
# else:
#     print("+")

#Задача 4
# month = int(input("Введите номер месяца (от 1 до 12): "))
# if month >= 1 and month <= 12:
#     if month in [12, 1, 2]:
#         season = "зима"
#     elif month in [3, 4, 5]:
#         season = "весна"
#     elif month in [6, 7, 8]:
#         season = "лето"
#     else:
#         season = "осень"
#     print(f"Сезон года: {season}")
# else:
#     print("Введен некорректный номер месяца. Пожалуйста, введите число от 1 до 12.")

# #Задача 5
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# if num1 > 10 and num2 > 10 and num3 > 10:
#     print("yes")
# else:
#     print("no")

# #Задача 6
# num1 = 20
# num2 = 10
# num3 = 30
# count_positive = 0
# if num1 > 0:
#     count_positive += 1
# if num2 > 0:
#     count_positive += 1
# if num3 > 0:
#     count_positive += 1
# print(f"Количество положительных чисел среди данных: {count_positive}")

# #Задача 7
# months = int(input("Введите количество месяцев: "))
# years = int(input("Введите количество лет: "))
# total_days = (years * 365) + (months * 29)
# print(f"Общее количество дней за {years} лет и {months} месяцев составляет {total_days} дней.")

#Задача 8
# age = int(input("Введите возраст Алмаза: "))
# if age < 18:
#     print("Еще рано")
# elif age >= 18:
#     print("Идем служить")
# elif age >= 40:
#     print("Уже не надо")