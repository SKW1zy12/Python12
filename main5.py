#Циклы for, while
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)

# for number in range(1000):
#     print(number)

# for py in range(1, 1001):
#     print("Python", py)

# numbers = [10, 3, 4, 1, 3, 7, 45, 101, 123, 112, 9]
# print(type(numbers))
# for num in numbers:
#     # print(type(num))
#     if num % 2 == 0:
#         print(num, "четный")
#     else:
#         print(num, "нечетный")

# mentors = ("Syimyk", "Islam", 'Kudbohon', 'Janysh', 'Nur')
# print(mentors)
# for mentor in mentors: #Итерация по циклу for
#     print("Здраствуйте", mentor)
# print('Здраствуйте', mentors[0])
# print('Здраствуйте', mentors[1])
# print('Здраствуйте', mentors[3])
# print('Здраствуйте', mentors[4])

# name = "Nurbolot"
# print(name)
# for n in name:
#     print(n)

# nums = [] #Пустой сипсок
# print(nums)
# for num in range(100, 151, 2):
#     nums.append(num)
# print(nums)

# while True:
#     print("Geeks")

# num1 = 10
# num2 = 30
# while num2 > num1:
#     num1 += 1
#     print(num1)

n = 0 
while True:
    n += 1
    print("Я ЛЮБЛЮ ТЕБЯ ДАНИЕЛЬ", n)
    if n ==1000000000000:
        print("STOP")
        break #Break заствляет прервать цикл досрочно

#     elif n == 19998:
#         print("CONTINUE")
#         continue #continue продалжает цикл без остоновки


# import random
# letters = 'qwertyuiopasdfghjklzxcvbnm123456789'

# result = ""

# len_password = int(input('Длина пароля: '))
# for i  in range(len_password):
#     random_letter = random.choice(letters)
#     result += random_letter
# print(result)

# import random
# cities = ["Osh", "Bishkek", "Batken", "Naryn" "Talas"]
# random_city = random.choice(cities)
# n = 0
# while True:
#     user_city = input("Город: ")
#     if random_city == user_city:
#         print("Вы выиграли!")
#         break
#     elif n == 3:
#         print("У вас закончились попытки")
#         break
#     else:
#         n += 1
#         print("неправильно, у вас", 3 - n, "Попытки")