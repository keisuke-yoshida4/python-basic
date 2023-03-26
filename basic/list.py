fruits = ["apple", "peach", "melon", "grapes"]
# print(fruits[0])
# print(fruits[-1])
# hetero_list = [1, 3, 4, fruits]
# print(hetero_list[-1])
# print("hello world"[3])

fruits.append("banana")
print(fruits)
fruits.insert(3, "lemon")
print(fruits)
fruits.remove("peach")
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
print(len(fruits))