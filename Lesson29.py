class WashingMachine:
    # поля класса
    __weight = 10
    count_of_water = 10
    color = 'white'
    electric_count = 100
    id = 1

    # методы класса
    @classmethod
    def activate(cls):
        cls.electric_count = 100000000000

    # методы объекта
    def __init__(self, weight, color):
        # поля объекта
        self.weight = weight
        self.color = color

    # методы объекта
    def __add__(self, other):  # +
        self.weight = self.weight + other.weight

    def __int__(self):
        print("NOT INT")

    def __str__(self):
        return f'Weight : {self.weight}\nColor : {self.color}'

    def washing(self, weight_of_clothes):
        if self.weight > weight_of_clothes:
            print('Start wash')
        elif self.weight == weight_of_clothes:
            print('It is too hard, but I try wash')
        else:
            print('Sooo much....')

    def drying(self):
        print('Start dry')

    def spining(self):
        print('Start wash')

    @property  # getter
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if new_weight >= 0 and new_weight <= 1000:
            self.__weight = new_weight
        else:
            print('WEIGHT')

    @weight.deleter
    def weight(self):
        print('Ouh noooo')


bosch = WashingMachine(20, 'red')
noname = WashingMachine(70, 'red')
WashingMachine.activate()
print(WashingMachine.electric_count)
print(bosch.electric_count)
print(bosch.weight)
# print(noname.weight)
# bosch + noname
# print(bosch.weight)
# bosch + noname
# print(bosch.weight)
a = 5
# int(bosch)
# bosch + a #not work
# bosch.count_of_water = 20
# print(bosch.count_of_water)
# print(bosch.color)
print(bosch)
s = str(bosch)
print(s)
print(bosch.weight)
bosch.washing(19)
bosch.washing(20)
bosch.washing(21)
# class O:
#     number = 0
#     def __init__(self,number):
#         self.number = number
#     def __add__(self, other):
#         self.number1 = self.number + other.number + 1
#         return self.number1
#
#     def __eq__(self, other):
#         return 'Lie'
#     def __str__(self):
#         return str(self.number)
#
# a = O(2)
# b = O(2)
# c = a + b
# print(a == b)
# print(a.number,'+',b,'=',a + b)
bosch.weight = 10000000
print(bosch.weight)
bosch.washing(21)
del bosch.weight

print(WashingMachine.color)
print(WashingMachine.id)  # Поле класса
WashingMachine.id = 100  # Меняем базовое значение поля класса
print(bosch.id)  # Поле объекта класса, которое мы получаем из класса
# bosch.id = 33#Создание поля объекта и перезапись вместо поля класса
print(bosch.id)  #
print(WashingMachine.id)
print(noname.id)
WashingMachine.id = 500

print(bosch.id)  #
print(WashingMachine.id)
print(noname.id)
