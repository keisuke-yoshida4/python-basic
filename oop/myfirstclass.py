class Person:

    num_legs = 2
    count = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking... with {Person.num_legs} legs")

    def run(self):
        print(f"{self.name} is running")


john = Person("John", 28, "male")
print(Person.count)
taro = Person("Taro", 18, "male")
print(Person.count)
emma = Person("Emma", 40, "female")
print(Person.count)

# インスタンスメソッド
print(john.name)
print(john.age)
print(john.gender)

print(taro.name)
print(taro.age)
print(taro.gender)

john.walk()
emma.walk()
john.run()

print(john.num_legs)
print(taro.num_legs)

print(Person.num_legs)
print("Person.num_legs = 3を実行")
Person.num_legs = 3
print(john.num_legs)
print(taro.num_legs)
john.num_legs = 4
print("john.num_legs = 4を実行")
print(john.num_legs)
print(taro.num_legs)