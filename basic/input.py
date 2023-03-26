# age = input("何歳ですか？")
# print("あなたは {}歳です。".format(age))

age = int(input("何歳ですか？"))
casino_age = 18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""
if age >= casino_age:
    print("あなたは{}歳以上なので、入場可能です。".format(casino_age))
    game = input(game_text)
    if game == "1":
        print("あなたはルーレットを選びました")
    elif game == "2":
        print("あなたはブラックジャックを選びました")
    elif game == "3":
        print("あなたはポーカーを選びました")
    else:
        print("1〜3を選んでください")

else:
    print("あなたは{}歳未満なので、入場不可能です。".format(casino_age))
casino_age

