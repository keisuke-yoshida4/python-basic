# game_text = """プレイするゲームを選択してください
#         1: ルーレット
#         2: ブラックジャック
#         3: ポーカー
#         """
casino_age = 18
text = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー'}

age = int(input("あなたは何歳ですか？"))
if age >= casino_age:
    print("あなたは{}歳以上なので、入場可能です。".format(casino_age))
    while True:
        print("プレイするゲームを選択してください。")
        for num, game_name in text.items():
            print(f"{num}: {game_name}")
        game = input(":")
        if game in text:
            print(f"あなたは{text[game]}を選びました")
            break
        else:
            print("1〜3を選んでください")
else:
    print("あなたは{}歳未満なので、入場不可能です。".format(casino_age))
