import random
from enum import Enum


class Hand():
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def janken():
    print("じゃんけんスタート!")

    # input関数は入力を読み込んで、文字列として返すのでint関数を用いて文字列を整数にします。

    player_hand = int(input("出す手を数値で入力 (0: グー, 1: チョキ, 2: パー) :"))

    if player_hand < Hand.ROCK or player_hand > Hand.SCISSORS:
        return print("0~2の数値を入力してください")

    computer_hand = random.randint(Hand.ROCK, Hand.SCISSORS)
    computer_hand2 = random.randint(Hand.ROCK, Hand.SCISSORS)
    janken_choices = ["グー", "チョキ", "パー"]

    print("あなたの出した手は " + janken_choices[player_hand])
    print("コンピュータ1の出した手は " + janken_choices[computer_hand])
    print("コンピューター2の出した手は" + janken_choices[computer_hand2])

    if player_hand == computer_hand == computer_hand2:
        print("あいこ")

    # andのほうがorよりも優先順位が高いです。

    elif ((player_hand == Hand.ROCK and computer_hand == Hand.PAPER and computer_hand2 == Hand.PAPER) or
          (player_hand == Hand.PAPER and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.SCISSORS) or
          (player_hand == Hand.SCISSORS and computer_hand == Hand.ROCK and computer_hand2 == Hand.ROCK)):
        print("あなたの勝ち!")
    elif ((player_hand == Hand.ROCK and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.ROCK)):
        print("コンピューター1の勝ち")
    elif ((player_hand == Hand.ROCK and computer_hand == Hand.PAPER and computer_hand2 == Hand.SCISSORS) or
          (player_hand == Hand.PAPER and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.ROCK) or
          (player_hand == Hand.SCISSORS and computer_hand == Hand.PAPER and computer_hand2 == Hand.ROCK) or
          (player_hand == Hand.PAPER and computer_hand == Hand.ROCK and computer_hand2 == Hand.SCISSORS) or
          (player_hand == Hand.PAPER and computer_hand == Hand.PAPER and computer_hand2 == Hand.SCISSORS) or
          (player_hand == Hand.ROCK and computer_hand == Hand.PAPER and computer_hand2 == Hand.ROCK) or
          (player_hand == Hand.ROCK and computer_hand == Hand.ROCK and computer_hand2 == Hand.PAPER) or
          (player_hand == Hand.ROCK and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.PAPER) or
          (player_hand == Hand.PAPER and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.PAPER) or
          (player_hand == Hand.PAPER and computer_hand == Hand.ROCK and computer_hand2 == Hand.ROCK) or
          (player_hand == Hand.SCISSORS and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.PAPER) or
          (player_hand == Hand.PAPER and computer_hand == Hand.ROCK and computer_hand2 == Hand.PAPER) or
          (player_hand == Hand.SCISSORS and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.PAPER) or
          (player_hand == Hand.SCISSORS and computer_hand == Hand.PAPER and computer_hand2 == Hand.SCISSORS) or
          (player_hand == Hand.SCISSORS and computer_hand == Hand.ROCK and computer_hand2 == Hand.SCISSORS) or
          (player_hand == Hand.SCISSORS and computer_hand == Hand.PAPER and computer_hand2 == Hand.PAPER) or
          (player_hand == Hand.ROCK and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.SCISSORS) or
          (player_hand == Hand.SCISSORS and computer_hand == Hand.ROCK and computer_hand2 == Hand.PAPER) or
          (player_hand == Hand.SCISSORS and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.ROCK)):
        print("あいこ")
    elif ((player_hand == Hand.PAPER and computer_hand == Hand.PAPER and computer_hand2 == Hand.ROCK) or
          (player_hand == Hand.ROCK and computer_hand == Hand.ROCK and computer_hand2 == Hand.SCISSORS)):
        print("コンピューター2の勝ち")

    else:
        print("あなたの負け!")


# じゃんけんゲームを実行
janken()
