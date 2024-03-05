import pygame
import random
from pygame.locals import *

# 初期化
pygame.init()

# パネルのサイズ
WIDTH = 1200
HEIGHT = 990
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# タイトル
pygame.display.set_caption("じゃんけんゲーム")

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# メイン関数
def main():
    clock = pygame.time.Clock()
    run = True

    # フォント作成
    # "msgothic"を指定してあげると日本語表示されるようになる
    sysfont = pygame.font.SysFont("msgothic", 45)

    # テキストを描画したウィンドウを作成
    game_start = sysfont.render("じゃんけんスタート", False, (0, 0, 0))
    game_win = sysfont.render("先に3勝した方が勝ち", True, (0, 0, 0))
    player_hand = sysfont.render("出す手を数値で入力 (0: グー, 1: チョキ, 2: パー)", True, (0, 0, 0))

    player_hand_value = None
    player_hand_text = None
    plyer_hand_choices = None

    while run:
        screen.fill((0, 0, 255))

        # テキストを描画する
        screen.blit(game_start, (15, 60))
        screen.blit(game_win, (15, 150))
        screen.blit(player_hand, (15, 200))

        # 入力されたじゃんけんの数字を描画する
        if player_hand_text:
            screen.blit(player_hand_text, (15, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ウィンドウが閉じられたらループを終了する
                run = False
            # キーを押したとき
            elif event.type == pygame.KEYDOWN:
                # ESCキーならスクリプトを終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    run = False
                # エンターキーなら入力されたじゃんけんの数字を表示する
                elif event.key == K_RETURN:
                    if player_hand_value in [0, 'グー', 1, 'チョキ', 2, 'パー']:
                        player_hand_text = sysfont.render("選択した数字: " + str(player_hand_value), True, (0, 0, 0))
                        plyer_hand_choices = sysfont.render("あなたの出した手は " + str(player_hand_text), True,
                                                            (0, 0, 0))
                # 数字キーならじゃんけんの数字を受け取る
                elif event.key in [K_0, 'グー', K_1, 'チョキ', K_2, 'パー']:
                    player_hand_value = int(pygame.key.name(event.key))
                    # 数字キーならじゃんけんの数字を受け取りじゃんけんの名前を表示させるようにしたい
                    plyer_hand_choices = str(pygame.key.name(event.key))


# スペースがない場合、その言語は単語として解析されず、1 つの単語の一部として解析されます。
if __name__ == '__main__':
    main()
