#try, except
# try:
#     num1 = 10
#     num2 = 0
#     print(num1/num2)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# while True:
#     try:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите втрое число: "))
#         print(f"Результат после сложения: {num1 + num2}")
#         print(f"Результат после вычитания: {num1 - num2}")
#     except ValueError:
#         print(f"Введите цифры!!!")

#set, frozenset
# num =  {2 ,3, 4, 5, 6, 7, }
# print(num)
# print(type(num))

#Не имеет дублкатов
#Не имеет структуры  индексы и срезы
#Изменяймый тип данных

# name =  {"geeks", "Abu", "Kutbu", "Nurbu", "geeks"}
# print(name)

# num = { 1, 2, 3 , 4, 5, "1"}
# print(num)

# try: 
#     num = {1, 2 ,3, 4, 5, 6, 7, 8 }
#     print(num [3])
# except:
#     print(" Set()  Не может использавать индексы или срезы")

# num = {1, 2, 3, 4}
# num.add(5)
# num.add(5)
# print(num)
# num.remove(2)
# print(num)

# name = frozenset(["Nurti", "Kumi", "Toha"])
# print(type(name))
# print(name)
# name.add("AbuDabu")
# print(name)
# name.remove("Kumi")