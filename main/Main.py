import random
from enum import Enum
import time

print("じゃんけんスタート")


class Hand():
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Decision():
    DRAW = "あいこ"
    LOSE = "負け"
    WIN = "勝ち"
    RULE = [DRAW, LOSE, WIN]


class Score():
    PLAYER_DRAW = 0
    PLAYER_LOSE = 0
    PLAYER_WIN = 0


def janken():
    while True:

        # input関数は入力を読み込んで、文字列として返すのでint関数を用いて文字列を整数にします。

        player_hand = int(input("出す手を数値で入力 (0: グー, 1: チョキ, 2: パー) :"))

        computer_hand = random.randint(Hand.ROCK, Hand.SCISSORS)
        computer_hand2 = random.randint(Hand.ROCK, Hand.SCISSORS)
        janken_choices = ["グー", "チョキ", "パー"]

        if player_hand < Hand.ROCK or player_hand > Hand.SCISSORS:
            return print("0~2の数値を入力してください")

        print("あなたの出した手は " + janken_choices[player_hand])
        print("コンピュータ1の出した手は " + janken_choices[computer_hand])
        print("コンピューター2の出した手は" + janken_choices[computer_hand2])
        time.sleep(0.9)
        if player_hand == computer_hand == computer_hand2:
            print(Decision.DRAW)


        # andのほうがorよりも優先順位が高いです。
        elif ((player_hand == Hand.PAPER and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.SCISSORS) or
              (player_hand == Hand.ROCK and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.SCISSORS) or
              (player_hand == Hand.PAPER and computer_hand == Hand.ROCK and computer_hand2 == Hand.ROCK) or
              (player_hand == Hand.SCISSORS and computer_hand == Hand.PAPER and computer_hand2 == Hand.PAPER)):
            # デバッグ
            print(Decision.WIN)
        elif ((player_hand == Hand.SCISSORS and computer_hand == Hand.ROCK and computer_hand2 == Hand.SCISSORS) or
              (player_hand == Hand.PAPER and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.PAPER) or
              (player_hand == Hand.ROCK and computer_hand == Hand.PAPER and computer_hand2 == Hand.ROCK)):
            # デバッグ
            print("コンピューター1の" + Decision.WIN)
        elif ((player_hand == Hand.ROCK and computer_hand == Hand.PAPER and computer_hand2 == Hand.SCISSORS) or
              (player_hand == Hand.PAPER and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.ROCK) or
              (player_hand == Hand.SCISSORS and computer_hand == Hand.PAPER and computer_hand2 == Hand.ROCK) or
              (player_hand == Hand.PAPER and computer_hand == Hand.ROCK and computer_hand2 == Hand.SCISSORS) or
              (player_hand == Hand.ROCK and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.PAPER) or
              (player_hand == Hand.SCISSORS and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.PAPER) or
              (player_hand == Hand.PAPER and computer_hand == Hand.ROCK and computer_hand2 == Hand.PAPER) or
              (player_hand == Hand.SCISSORS and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.PAPER) or
              (player_hand == Hand.SCISSORS and computer_hand == Hand.PAPER and computer_hand2 == Hand.SCISSORS) or
              (player_hand == Hand.SCISSORS and computer_hand == Hand.ROCK and computer_hand2 == Hand.PAPER) or
              (player_hand == Hand.ROCK and computer_hand == Hand.PAPER and computer_hand2 == Hand.PAPER) or
              (player_hand == Hand.SCISSORS and computer_hand == Hand.ROCK and computer_hand2 == Hand.ROCK) or
              (player_hand == Hand.ROCK and computer_hand == Hand.ROCK and computer_hand2 == Hand.SCISSORS) or
              (player_hand == Hand.ROCK and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.ROCK)):
            # デバッグ
            print(Decision.DRAW)
        elif ((player_hand == Hand.PAPER and computer_hand == Hand.PAPER and computer_hand2 == Hand.ROCK) or
              (player_hand == Hand.PAPER and computer_hand == Hand.PAPER and computer_hand2 == Hand.SCISSORS) or
              (player_hand == Hand.SCISSORS and computer_hand == Hand.SCISSORS and computer_hand2 == Hand.ROCK) or
              (player_hand == Hand.ROCK and computer_hand == Hand.ROCK and computer_hand2 == Hand.PAPER)):
            print("コンピューター2の" + Decision.WIN)

        else:
            print("あなたの" + Decision.LOSE)

        # 勝敗判定
        i = (player_hand - computer_hand - computer_hand2) % 3
        print(Decision.RULE[i])
        if i == 0:
            Score.PLAYER_DRAW += 1
        elif i == 1:
            Score.PLAYER_LOSE + 1
        else:
            Score.PLAYER_WIN + 1
            time.sleep(0.9)

        # 出力結果
        print("{}勝/{}負/{}引き分け".format(Score.PLAYER_WIN, Score.PLAYER_LOSE, Score.PLAYER_DRAW))
        if Score.PLAYER_WIN == 3:
            print("「3勝であなたの勝ち}")


# じゃんけんゲームを実行
janken()
