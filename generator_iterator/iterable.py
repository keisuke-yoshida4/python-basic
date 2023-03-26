fruits = ["apple", "lemon", "peach"]

# print(next(fruits))
fruits_iterator = (iter(fruits))
print(next(fruits_iterator))
print(next(fruits_iterator))
print(id(fruits_iterator))
print(id(iter(fruits_iterator)))
