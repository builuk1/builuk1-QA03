'''Напишите функцию, определяющую количество
простых чисел в списке целых.
Список передаётся в качестве параметра.
Полученный результат возвращается из функции.'''
def simple(number):
    for some_number in range(2,number):
        if number%some_number == 0:
            return False
    return True

def simple_list(list_of_numbers):
    new_list = []
    for number in list_of_numbers:
        if simple(number):
            new_list.append(number)
    l = len(new_list)
    return l


random_list = [1,4,5,7,3,5,6,8,137,42,65]
print(simple_list(random_list))