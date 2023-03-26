fruits_colors = {"apple": "red", "lemon": "yellow", "grapes": "purple"}
print(fruits_colors["apple"])
fruits_colors["peach"] = "pink"
print(fruits_colors)

dict_sample = {1: "one", 2: "two", "three": [1, 2, 3], 'four': {'inner': 'outer'}}
print(dict_sample["three"])
print(dict_sample["four"]["inner"])

# colors = {}
# colors[1] = 'blue'
# colors[0] = 'red'
# colors[2] = 'purple'
# print(colors)

mem = []
mem.append('blue')
mem.append('red')
mem.append('yellow')
print(mem[1])

for color in fruits_colors.values():
    print(color)

for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}")