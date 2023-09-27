#Dictionary -  словари 
#Типы данных: list, tuple, int, str, float, bool, set, frozenset, dict
# student = {'name':'Nurbolot', 'age':19}
# print(student)
# print(student['name'])
# print(student['age'])
# student.setdefault('language', 'Python') #метод для добавления в список
# print(student)
# student.pop('age') #Метод удаления из списка по ключу
# print(student)
# student['language'] = "Java" #Систаксис для обновления значения по ключу
# print(student)
# print(student.keys())#Метод для получения ключей из словаря
# print(student.values()) #Метод для получения значений из словаря
# print(student.items())#метод для получения ключа и значения за раз

# geeks = {'Name':'Geeks', 'count_students':340, 'address':'Amatova 18'}
# print(geeks)
# for key, value in geeks.items():
#     print(key, value)

# # dct = {}
# # print(type(dct))

# contact = {'MCHS':'112'}
# while True:
#     command = input("1 - посмотреть, 2 - добаваить, 3 - удалить, 4 - обновить: ")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("Имя: ")
#         add_number =  input("Номер: ")
#         contact.setdefault(add_name, add_number)
#         print("Контакт", add_number, "успешно добавлен")
#     elif command == "3":
#         remove_name = input("Кого удалить?:  ")
#         contact.pop(remove_name)
#         print("Контакт", remove_name, "успешно удален")
#     elif command == "4":
#         update_name = input("Кого обноваить?: ")
#         update_number = input("Новый номер: ")
#         contact[update_name] = update_number
#         print("Номер контакта", update_name, "успешно обновлен на", update_number)
#     else:
#         print("Такой комманды нету")

#Functions - функции 
# def hello():
#     print("Hello World")
# hello()
# hello()

# def welcome():
#     name = input("Имя: ")
#     print("Привет", name)
# # welcome()

# def add():
#     num1 = int(input("Первое число: "))
#     num2 = int(input("Второе число: "))
#     print(num1 + num2)
# add()

# def mult(num1, num2): #num 1 и num2 являются параметром функции mult
#     print(num1 + num2)
# mult(5, 3)#число 5 и 3 являются аргументами функции
# mult(8108231083, 13921931)

# def div(num1, num2):
#     try:
#         print(num1 / num2)
#     except ZeroDivisionError:
#         print("Ошибка! на ноль делать нельзя")
# div(25, 5)
# div(16, 3)