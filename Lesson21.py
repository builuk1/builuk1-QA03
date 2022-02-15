# #Файлы
# import random
# import time
# #IDE
# # f = open('test.txt','wt')#t - text /b - binary
# # #open('fff','rt')
# # f.write('My name is Andrey\nHow are you?')
# # # time.sleep(15)
# # f.close()
# # # random.randint()
# # f = open('test.txt','rt')
# # print(f.read())
# # f.close()
# # #w - write открыть файл на запись
# # #r - read открыть файл на чтение, если он есть, если нет ошибка
# #
# # f = open('test.txt','rt')
# # print(f.read())#Считывает файл целиком НЕ БЕЗОПАСЕН
# # f.close()
# #
# # f = open('test.txt','rt')
# # print(f.readline())#Считывает файл построчно, как итерируемый объект
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # f.close()
# #
# # f = open('test.txt','rt')
# # print(f.readlines())#Считывает файл целиком как список
# # f.close()
# #
# # #w - write открыть файл на запись, если нет файла создать, если есть файл перезаписать
# # f = open('test.txt','wt')#t - text /b - binary
# # f.write('My name is Andrey\nHow are you?\n')
# # s = 'Star Wars is an American epic space opera[1] multimedia franchise created by George Lucas, which began with the eponymous 1977 film[b] and quickly became a worldwide pop-culture phenomenon. The franchise has been expanded into various films and other media, including television series, video games, novels, comic books, theme park attractions, and themed areas, comprising an all-encompassing fictional universe.[c] In 2020, its total value was estimated at US$70 billion, and it is currently the fifth-highest-grossing media franchise of all time.The original film (Star Wars), retroactively subtitled Episode IV: A New Hope (1977), was followed by the sequels Episode V: The Empire Strikes Back (1980) and Episode VI: Return of the Jedi (1983), forming the original Star Wars trilogy. Lucas later returned to the series to direct a prequel trilogy, consisting of Episode I: The Phantom Menace (1999), Episode II: Attack of the Clones (2002), and Episode III: Revenge of the Sith (2005). In 2012, Lucas sold his production company to Disney, relinquishing his ownership of the franchise. This led to a sequel trilogy, consisting of Episode VII: The Force Awakens (2015), Episode VIII: The Last Jedi (2017), and Episode IX: The Rise of Skywalker (2019).All nine films of the "Skywalker saga" were nominated for Academy Awards, with wins going to the first two releases. Together with the theatrical live action "anthology" films Rogue One (2016) and Solo (2018), the combined box office revenue of the films equated to over US$10 billion, which makes it the second-highest-grossing film franchise of all time.[3][4] An additional film, Rogue Squadron, is planned for release. A number of other films, including an \nindependent trilogy, are suggested to be in development.'
# # f.write(s)
# # f.close()
#
# #a - add открыть файл на запись, если нет файла создать, если есть файл дописать в конец append
# f = open('test.txt','at')#t - text /b - binary
# f.write('My name is Andrey\nHow are you?\n')
# s = 'Star Wars is an American epic space opera[1] multimedia franchise created by George Lucas, which began with the eponymous 1977 film[b] and quickly became a worldwide pop-culture phenomenon. The franchise has been expanded into various films and other media, including television series, video games, novels, comic books, theme park attractions, and themed areas, comprising an all-encompassing fictional universe.[c] In 2020, its total value was estimated at US$70 billion, and it is currently the fifth-highest-grossing media franchise of all time.The original film (Star Wars), retroactively subtitled Episode IV: A New Hope (1977), was followed by the sequels Episode V: The Empire Strikes Back (1980) and Episode VI: Return of the Jedi (1983), forming the original Star Wars trilogy. Lucas later returned to the series to direct a prequel trilogy, consisting of Episode I: The Phantom Menace (1999), Episode II: Attack of the Clones (2002), and Episode III: Revenge of the Sith (2005). In 2012, Lucas sold his production company to Disney, relinquishing his ownership of the franchise. This led to a sequel trilogy, consisting of Episode VII: The Force Awakens (2015), Episode VIII: The Last Jedi (2017), and Episode IX: The Rise of Skywalker (2019).All nine films of the "Skywalker saga" were nominated for Academy Awards, with wins going to the first two releases. Together with the theatrical live action "anthology" films Rogue One (2016) and Solo (2018), the combined box office revenue of the films equated to over US$10 billion, which makes it the second-highest-grossing film franchise of all time.[3][4] An additional film, Rogue Squadron, is planned for release. A number of other films, including an \nindependent trilogy, are suggested to be in development.'
# f.write(s)
# f.close()
#
# #x - ? открыть файл на запись, если файл есть ошибка, если нет создаёт новый
# # f = open('test1.txt','xt')#t - text /b - binary
# # f.write('I am your father, Luke')
# # f.close()
# #+ - открытие файла на чтение и запись
# f = open('test.txt','at+')#t - text /b - binary
# f.write('I am your father, Luke')
# f.close()
# f = open('test.txt','at+')#t - text /b - binary
# print(f.read())
# f.close()
# import random
# f = open('numbers2.txt','wt')
# for i in range(10):
#     for j in range(10):
#         f.write(str(random.randint(1,9)))
#     f.write('\n')
# f.close()

# n1 = open('numbers1.txt','rt')
# n2 = open('numbers2.txt','rt')
# n3 = open('numbers3.txt','wt')
# ln1 = n1.readline()
# ln2 = n2.readline()
# while ln1 or ln2:
#     n3.write(ln1)
#     n3.write(ln2)
#     ln1 = n1.readline()
#     ln2 = n2.readline()
# n3.close()
#Некорректная работа, проверьте на заранее подготовленных данных
# n1 = open('numbers1.txt','rt')
# n2 = open('numbers2.txt','rt')
# n3 = open('numbers3.txt','wt')
# ln1 = n1.readline()
# ln2 = n2.readline()
# while n1.readline() or n2.readline():
#     n3.write(n1.readline())
#     n3.write(n1.readline())
# n3.close()