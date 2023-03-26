fruits = ["apple", "peach", "grapes", "banana"]
print("lemon" in fruits)

select_fruits = input("あなたの好きなフルーツはなんですか？")

if select_fruits in fruits:
    print("{}ですね。差し上げますよ。".format(select_fruits))
    fruits.remove(select_fruits)
else:
    print("{}ですね。仕入れました。".format(select_fruits))
    fruits.append(select_fruits)

print("今あるフルーツはこちらです。{}".format(fruits))