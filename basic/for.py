fruits = ["apple", "peach", "grape", "banana"]
# for fruit in fruits:
#     print(f"I love {fruit}!!")
#
# for char in "hello world":
#     print(f"char:{char}")
#
# like = input("好きなフルーツを入力してください")
# for fruit in fruits:
#     if fruit == like:
#         print("I love {}!!".format(like))
#     else:
#         print("{}は別に普通".format(fruit))
favorite_fruits = []
normal_fruits = []
for fruit in fruits:
    choice = input(f"{fruit}は好き？ y/n")

    if choice == "y":
        favorite_fruits.append(fruit)
    else:
        normal_fruits.append(fruit)
print(f"favorite fruits:{favorite_fruits}")
print(f"normal fruits:{normal_fruits}")
