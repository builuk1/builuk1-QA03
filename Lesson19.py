# def simple(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# l = [1, 2, 3]
# print(l.pop())
# print(l.append(4))
#
#
# def pop(somelist):
#     return somelist.pop()
#
#
# def append(somelist, data):
#     somelist.append(data)
#
#
# l = [1, 2, 3]
# print(pop(l))
# print(append(l, 4))
# print(l)
#
#
# # Рекурсия
#
# # return > break
# def somfunction():
#     return 'Something'
#     print("You can't see this in console")
#
#
# while False:
#     print("You can't see this in console")
# if False:
#     print("You can't see this in console")
#
#
# def calc(a, b):  # Позиционные аргументы
#     return a + b
#
#
# print(calc(2, 2))
#
#
# def calc1(a, b, c=2):  # Аргументы по умолчанию
#     return a + b + c
#
#
# print(calc1(2,2))
#range(start,finish,step)
def custom_range(start,finish=False,step=False):
    numbers = []
    if finish:
        if start < finish:
            while start != finish:
                numbers.append(start)
                if step:
                    start = start + step
                else:
                    start = start + 1
        elif start > finish:
            while start != finish:
                numbers.append(start)
                if step:
                    start = start + step
                else:
                    return numbers
    else:
        n = 0
        while n < start:
            numbers.append(n)
            n = n + 1
    return numbers

for i in range(1,12,1):
    print(i,end=' ')
print()
for i in custom_range(1,12,1):
    print(i, end=' ')