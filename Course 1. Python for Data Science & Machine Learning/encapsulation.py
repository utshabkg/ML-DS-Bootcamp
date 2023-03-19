class Student:
    def __init__(self):
        self.name = 'Emon'
        self._age = 20
        self.__session = 2018

    def get_session(self):
        print(self.__session)
    def set_session(self, session):
        self.__session = session

s = Student()
print(s.get_session())

s.set_session(2020)
print(s.get_session())
# print(s._age)
# print(s.__session)

