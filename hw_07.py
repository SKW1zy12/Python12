# #Задача 1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

#Задача 2
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100}
# for key in numbers:
#     numbers[key] *= 5
# print(numbers)

#Задача 3
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] *= 2
# print(student)

# #Задача 4
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = 16
# print(student)

# #Задача 5
# student = {'name': 'Askhat', 'age': 17}
# student.pop('age')
# print(student)

#Задача 6
# student = {'name' : 'Askhat'}
# student.setdefault('address', 'Западный Анар')
# print(student)

#Задача 7
# def abu():
#     user = input("Введите фразу: ")
#     user1 = user.split()
#     a = []
#     for word in user1:
#         a.append(word[0].upper())
#     b = "".join(a)
#     print(b)
# abu()

# #Задачча 8
# def abu():
#     abu = "Money, money, money, it's always sunny, in the richmen's world".lower()
#     print("money:", abu.count("money"))
#     print("it's:", abu.count("it's"))
#     print("always:", abu.count("always"))
#     print("sunny:", abu.count("sunny"))
#     print("in:", abu.count("in"))
#     print("the:", abu.count("the"))
#     print("richmen's:", abu.count("richmen's"))
#     print("world:", abu.count("world"))
# abu()

# Задача 9
# def isogram(word):
#     word = word.lower()
#     unique_letters = set()
#     for letter in word:
#         if letter in unique_letters:
#             return False
#         unique_letters.add(letter)
#     return True
# word1 = "hello"
# word2 = "world"
# word3 = "algorithm"
# print(isogram(word1))


# #Задача 10
# Задача 10
# def n():
#     n = int(input("Введите число: "))
#     a_n = int(str(n)[::-1])
#     print(a_n)
# n()

# #Задача 11
# def user(): 
#     while True:
#         user = input("Можете задать вопрос: ")
#         if user.find("?")>=0:
#             print("Конечно!")
#         elif user.find("!")>=0:
#             print("Успокойся")
#         elif user == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("ну и что")
# user()