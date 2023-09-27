# #Задача 1
# for i, _ in enumerate(range(5), start=1):
#     print(f'Строка {i}: 0')

# # #Задача 2
# # my_list = []
# # print(my_list)
# # for list in range(1, 100):
# #     print(list)

# #Задача 3
# # nums = []
# # print(nums)
# # for num in range(2, 498, 2):
# #     nums.append(num)
# # print(nums)

# #Задача 4
# # my_list = list(range(1, 1001))
# # min_value = min(my_list)
# # max_value = max(my_list)

# # print(f"Минимальное значение: {min_value}")
# # print(f"Максимальное значение: {max_value}")

# # sum_of_numbers = sum(my_list)
# # print(f"Сумма всех чисел: {sum_of_numbers}")

# #Задача 5
# nums = []
# for num in range(100):
#     nums.append(0)
# print(nums)

# #Задача 6 
# it_company = ('Google', 'Amazon', 'Microsoft')
# it_list = list(it_company)
# it_list.append('Tesla')
# it_company = tuple(it_list)
# print(it_company)

# #Задача 7
# for i, company in enumerate(it_company):
#     if company == 'Amazon':
#         print(f"Индекс 'Amazon' в списке: {i}")

# #Задача 8
# it_list[it_list.index('Google')] = 'Apple'
# it_company = tuple(it_list)
# print(it_company)

# #Задача 9
# print(it_company[0:3])

# #Задача 10
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other',
# 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the',
# 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your',
# 'appetite', 'with', 'our', 'Python', '3', 'overview') 
# list = text_tuple.count('Python')
# print(list)

# #Задача 11
# value1 = input("Введите значение для переменной 1: ")
# value2 = input("Введите значение для переменной 2: ")
# value1, value2 = value2, value1
# print(f"Значение переменной 1: {value1}")
# print(f"Значение переменной 2: {value2}")

# #Задача 12
# while True:
#     age = int(input("Введите ваш возраст: "))
#     if age >= 18:
#         print("Доступ разрешен")
#         break
#     else:
#         print("Извините, пользование данным ресурсом только с 18 лет")