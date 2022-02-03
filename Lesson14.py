# '''Задание 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран.
# * Без использования метода count'''
# s = 'Abrakadabra'
# symbol = 'ra'
# print(s.count(symbol))
# '''Задание 5
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.
# * Без использования метода replace'''
# s = 'Abrakadabra'
# symbol = 'ra'
# new_symbol = 'RA'
# print(s.replace(symbol,new_symbol))
#
# print(s)

s = 'AbrakaDabrA'  # QiWi Yandex yandex qiwi Qiwi QIWI
s = s.lower()
symbol = 'a'
symbol = symbol.lower()
count = 0
for i in range(len(s)):
    if s[i] == symbol:
        count = count + 1
print(count)
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())

'''Задание 1
Есть некоторый текст. Реализуйте следующую функциональность:
■ Изменить текст таким образом, чтобы каждое предложение начиналось
с большой буквы;
■ Посчитайте сколько раз цифры встречаются в тексте;
■ Посчитайте сколько раз знаки препинания встречаются в тексте;
■ Посчитайте количество восклицательных знаков в
тексте.'''
# s = 'Helllo123'
# print(s.isalnum())

number = '0123456789'
spe = '!?,.'
s = 'some interesting, text and else! what i am doing. how do you do? i am fine! thank you.'
count_number = 0
count_symbol = 0
count_spe = 0
count_spea = 0
for i in range(len(s)):
    print(s[i])
    a = s[i]
    for n in range(len(number)):
        if a == number[n]:
            count_number = count_number + 1
    for q in range(len(spe)):
        if a == spe[q]:
            count_spe = count_spe + 1
    if a == spe[0]:
        count_spea = count_spea + 1
print(count_symbol, count_number, count_spe,count_spea)

t = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
t = t.capitalize()
symbols = '!.?'
for i in range(2, len(t)):
    for s in range(len(symbols)):
        print(t[i - 2:i])
        if t[i - 2:i] == (symbols[s] + ' '):
            # print('y')
            t = t[:i] + t[i].upper() + t[i + 1:]
print(t)
s = 'Hello World!'
print(s[0:5])#Hello
print(s[-6:-1])#World
print(s[-6:])#World!
print(s[:5])#Hello
print(s[::-1])#!dlroW olleH

word = 'Hello World!'
for letter in word:
    print(letter)

#in
number = '0123456789'
spe = '!?,.'
s = 'some interesting, text and else! what i am doing. how do you do? i am fine! thank you.'
count_number = 0
count_symbol = 0
count_spe = 0
count_spea = 0
for i in range(len(s)):
    print(s[i])
    a = s[i]

    if a in number:
        count_number = count_number + 1
    if a in spe:
        count_spe = count_spe + 1
    if a == spe[0]:
        count_spea = count_spea + 1
print(count_symbol, count_number, count_spe,count_spea)

word = 'Hello World!'
print(word.find('l'))
print(word.rfind('l'))

#https://docs.python.org/3/library/stdtypes.html#string-methods
#https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

weight = '44'#str(input('Enter your weight : '))
if weight.isnumeric():
    weight = int(weight)
    if weight < 0:
        print('error-')
    elif weight > 150:
        print('error+')
    elif weight < 150:
        print('Your weight is', weight)
    else:
        print('Oversize')


n = 0
maximum = -10000000
minimum = -10000000
count = 0
summa = 0
av = 0
while n != 7:
    if maximum == -10000000:
        maximum = n
    if minimum == -10000000:
        minimum = n
    n = int(input("Enter number : "))
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n
    count = count + 1
    summa = summa + n
    av = summa / count

s = ''
while True:
    num = input('Please, enter a number:')
    for i in range(len(num)):
        if num[i] == '6' or num[i] == '3':
            continue
        else:
            s = s + num[i]
print(int(s))