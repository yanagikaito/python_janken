import random


def janken():
    print("じゃんけんスタート!")
    player_hand = int(input("出す手を数値で入力 (0: グー, 1: チョキ, 2: パー) :"))

    if player_hand < 0 or player_hand > 2:
        print("0~2の数値を入力してください")
        exit()

    computer_hand = random.randint(0, 2)
    computer_hand2 = random.randint(0, 2)
    janken_choices = ["グー", "チョキ", "パー"]

    print("あなたの出した手は " + janken_choices[player_hand])
    print("コンピュータの出した手は " + janken_choices[computer_hand])
    print("コンピューター2の出した手は" + janken_choices[computer_hand2])

    if player_hand == computer_hand == computer_hand2:
        print("あいこ")
    elif ((player_hand == 0 and computer_hand == 1 and computer_hand2 == 1) or (player_hand == 1 and computer_hand == 2
                                                                                and computer_hand2 == 2) or (
                  player_hand == 2 and computer_hand == 0 and computer_hand == 0)):
        print("あなたの勝ち!")
    elif ((player_hand == 0 and computer_hand == 1 and computer_hand2 == 2) or (
            player_hand == 1 and computer_hand == 2
            and computer_hand2 == 0) or (
                  player_hand == 2 and computer_hand == 1 and computer_hand2 == 0) or
          (player_hand == 1 and computer_hand == 0 and computer_hand2 == 2) or
          (player_hand == 1 and computer_hand == 1 and computer_hand2 == 2) or
          (player_hand == 0 and computer_hand == 1 and computer_hand2 == 0) or
          (player_hand == 0 and computer_hand == 0 and computer_hand2 == 1) or
          (player_hand == 0 and computer_hand == 2 and computer_hand2 == 1) or
          (player_hand == 1 and computer_hand == 2 and computer_hand2 == 1) or
          (player_hand == 1 and computer_hand == 0 and computer_hand2 == 0) or
          (player_hand == 2 and computer_hand == 2 and computer_hand2 == 1) or
          (player_hand == 1 and computer_hand == 0 and computer_hand2 == 1)):
        print("あいこ")
    elif ((player_hand == 1 and computer_hand == 1 and computer_hand2 == 0)):
        print("コンピューター2の勝ち")
    else:
        print("あなたの負け!")


# じゃんけんゲームを実行
janken()
