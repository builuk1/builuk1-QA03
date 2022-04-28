class GeometryValidation:
    __count = 0

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self,new_count):
        if new_count == 3:
            self.__count = new_count
        elif new_count == 4:
            self.__count = new_count
        else:
            print('ERROR')