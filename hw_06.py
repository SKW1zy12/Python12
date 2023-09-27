# #Задача 1
# try:
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("Ошибка: деление на 0 невазможно")

# #Задача 2
# try:
#     str = input("Введите строку, представляющую собой число: ")
#     number = int(str)
#     print("Вы ввели целое число:", number)
# except:
#     print("Ошибка: Введенная строка не является числом.")

# #Задача 3
# text = "Hello World "
# words = set(text.split())
# unique_words = len(words)
# print("Количество уникальных слов:", unique_words)

# #Задача 4
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# set1 = set(list1)
# set2 = set(list2)

# common_elements = set1.intersection(set2)

# print("Общие элементы, используя set:", common_elements)

# frozen_set1 = frozenset(list1)
# frozen_set2 = frozenset(list2)

# frozen_common_elements = frozen_set1.intersection(frozen_set2)

# print("Общие элементы, используя frozenset:", frozen_common_elements)