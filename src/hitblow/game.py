import random

def play():
    # 1から100の間でランダムな数字を1つ決める
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 6

    print("=========================================")
    print(" 🎮 数当てミニゲーム (1 〜 100) 🎮")
    print(f" {max_attempts}回以内に正解の数字を当ててね！")
    print("=========================================")

    while attempts < max_attempts:
        try:
            # プレイヤーに入力を促す
            guess = int(input(f"\n[{attempts + 1}/{max_attempts}回目] 予想する数字を入力してね: "))
        except ValueError:
            print("⚠️ 数字を入力してね！")
            continue

        attempts += 1

        # 判定
        if guess < secret_number:
            print("⬆️ もっと【大きい】よ！")
        elif guess > secret_number:
            print("⬇️ もっと【小さい】よ！")
        else:
            print(f"\n🎉 おめでとう！！ {attempts}回目で大正解！ 🥳")
            break
    else:
        print(f"\n💀 ゲームオーバー...！ 正解は【{secret_number}】でした。")

'''
from .core import judge, make_secret


def play(digits=3):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")
        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break
'''