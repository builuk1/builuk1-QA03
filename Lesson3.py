# #Lesson3
# #if...elif...else
# print(2+2)
# print(2/4)
# #2+2  + оператор   2 операнд    бинарные
# #-2  - оператор 2 операнд    унарный
# # Математические + - * / // % **
# # Логические > < >= <= == !=
# print(5>2)
# print(4<4)
# print('4','>=','4',4>=4)
# print(5<=3)
# print(2==2)
# print(4!=4)
# age = 13 #PEP 8 CISCO
# if age < 18:#True
#     print('Child')
# if age > 18:
#     print('Adult')
# if True:
#     print('ALWAYS')
# if False:
#     print('NEWER')
#
# if 1:
#     print(1)
#
# if 'Something':
#     print('Something')
#
# if file:
#     ....
# age = 18
# if age <= 18:
#     print('Child')
# if age >= 18:
#     print('Adult')
# age = 18
# if age < 18:
#     print('Child')
# else:
#     print('Adult')

#Если вес меньше 150 выводит вес. Если вес больше 150 выводит
#'Превышено значение'
# weight = 120
# if weight < 150:
#     print('Your weight is', weight)
# else:
#     print('Oversize')

age = 1100
if age < 0:
    print('Error-')
elif age < 13:#else if
    print('Child')
elif age < 18:#else if
    print('Teen')
elif age < 135:#else if
    print('Adult')
else:
    print('Error+')

#try...except...else...finally Lesson23

#Если вес меньше 150 выводит вес. Если вес больше 150 выводит
#'Превышено значение'
# weight = 120
# if weight < 150:
#     print('Your weight is', weight)
# else:
#     print('Oversize')

weight = 44
if type(weight) == type('1'):
    print('Text type')
elif type(weight) == type(1.0):
    print('Float type')
elif weight < 0:
    print('error-')
elif weight > 150:
    print('error+')
elif weight < 150:
    print('Your weight is', weight)
else:
    print('Oversize')
