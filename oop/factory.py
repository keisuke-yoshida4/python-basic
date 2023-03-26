import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        # if (today.tm_mon, today.tm_mday) < (month, date):
        #     age = today.tm_year - year -1
        # else:
        #     age = today.tm_year - year
        return cls(name=name, age=age)

    @staticmethod
    def create_from_dob2(name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return Person(name=name, age=age)


class Baby(Person):
    pass


emma = Baby.create_from_dob("Émma", 1989, 3, 27)
emily = Baby.create_from_dob2("Émily", 1999, 5, 27)
john = Baby("John", 20)
print(john.name)
print(emma.name)
print(emma.age)
print(emily.age)
print(type(john))
print(type(emma))
# staticmethodの問題点
print(type(emily))