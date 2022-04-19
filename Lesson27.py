class Mobile:
    model = 'Xiaomi Mi10'
    color = 'Grey'  # public
    _os = 'Android'  # protected
    version = '10'
    __IMEI = 1  # privat
    blacklist = [111,222,333]

    def __init__(self):
        self.__IMEI = Mobile.__IMEI
        Mobile.__IMEI = Mobile.__IMEI + 1
    def charge(self):
        print('Charging....')

    def call(self):
        print('Call')

    def darknet(self, new_IMEI):
        self.__IMEI = new_IMEI
        if new_IMEI == 777:
            self.__change_ram()

    def show_IMEI(self):
        print(self.__IMEI)

    def __change_ram(self):
        print('You are cheater!!!')

    def usb_connect(self,option='Charge'):
        if option == 'Charge':
            print('Charging.........')
        elif option == 'Camera':
            print('Smile :)')
        elif option == 'FileStorage':
            print('Ready to work!')
        else:
            print('Reconnect')

    def usb_connect_v2(self,Charge=False,Camera=False,FileStorage=False):
        if Charge:
            print('Charging.........')
        elif Camera:
            print('Smile :)')
        elif FileStorage:
            print('Ready to work!')
        else:
            print('Reconnect')
    def IMEI_checker(self):
        if self.__IMEI == 777:
            print('Потрачено')
        elif self.__IMEI in self.blacklist:
            print('ПОТРАЧЕНО')
        else:
            print('OK')

class IPhone(Mobile):
    model = 'Iphone'
    _os = 'IOS'

    def Itunes(self):
        print('My music')
my_phone = Mobile()

# my_phone.__change_ram(4)
# s = str()
# l = []
# l = list()
#
# print(my_phone.model)
# my_phone.charge()
# my_phone.call()
# print(my_phone.color)
# my_phone.color = 'red'
# print(my_phone.color)
# print(my_phone._os)
# my_phone._os = 'XOS'
# print(my_phone._os)
# # print(my_phone.__IMEI)
# my_phone.show_IMEI()
# my_phone.darknet('99999')
# my_phone.show_IMEI()
#
# my_phone.show_IMEI()
# your_phone = Mobile()
# sten_phone = Mobile()
# my_phone.show_IMEI()
# your_phone.show_IMEI()
# sten_phone.show_IMEI()
# my_phone.darknet(777)
my_phone.usb_connect()
my_phone.usb_connect('Camera')
my_phone.usb_connect_v2(0,0,1)
my_phone.darknet(222)
my_phone.IMEI_checker()

apple = IPhone()
print(apple._os)
apple.Itunes()