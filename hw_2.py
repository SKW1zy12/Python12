#Задача 1

#Одинарные кавычки
single_quoted_string = 'Это строка с одинарными кавычками.'

#Двойные кавычки
double_quoted_string = "Это строка с двойными кавычками."

# Тройные одинарные кавычки (для многострочных строк)
triple_single_quoted_string = '''Это многострочная строка
с тройными одинарными кавычками.'''

# Тройные двойные кавычки (для многострочных строк)
triple_double_quoted_string = """Это многострочная строка
с тройными двойными кавычками."""

#Задача 2

original_string = "Привет, "
repeated_string = original_string * 3
print(repeated_string)

#Задача 3

#В Python можно преобразовать различные типы данных в строки с помощью процесса, называемого "приведением к строке" или "конвертацией в строку"

#(int)
b = 125.0
c = 390.8
print(int(b))
print(int(c))

#(float)
f = 57
print(float(f))

#Задача 4

#Срезы строк в Python позволяют вам получать подстроку из исходной строки, выбирая определенный диапазон символов
#string[start:stop:step]
#string - это строка, из которой вы хотите извлечь срез
#start - индекс первого символа в срезе (включительно). Если не указан, считается, что start равен 0 (начало строки)
#stop - индекс первого символа, который не входит в срез (исключительно). Если не указан, считается, что stop равен длине строки
#step - шаг, с которым будет выбрана каждая последующая буква (по умолчанию равен

#Несколько примеров срезов строк:

text = "Hello, World!"
print(text[0 : 5])
print(text[7:11:2])
print(text[4:])
print(text[::-1])

#Задача 5
text_1 = """
Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.
"""

print(text_1.count('a'))
print(text_1.count('t'))

#Задача 6
some_string = "Adverts"
print(some_string[2] + some_string[3] + some_string[4])

#Задача 7
name1 = "Aidana"
name2 = "Adilet"

mixed_name = ""

# Перебираем буквы из обоих имен и добавляем их в смешанную строку
for letter1, letter2 in zip(name1, name2):
    mixed_name += letter1 + letter2

# Если имена имеют разную длину, добавляем оставшиеся буквы из более длинного имени
if len(name1) > len(name2):
    mixed_name += name1[len(name2):]
elif len(name2) > len(name1):
    mixed_name += name2[len(name1):]

print(mixed_name)