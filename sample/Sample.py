# -1が商で2が余り
# -1=3x(-1)+2
p = 1
m = 2
i = (p - m) % 3
print(i)

n = int(input('ピラミッドの段数を入力してください'))
for j in range(1, n + 1):
    print(' ' * (n - j) + '*' * (2 * j - 1))
print("---------------------------------")

print("砂時計の形を表示")


def sandclock(size):
    # range(start, stop, step): startから始まり、stopの値まで（stopは含まず）
    # stepずつ増減するシーケンスを生成します。
    for i in range(size, 0, -1):
        # (size - i) 空白
        # (2 * i - 1) *の数
        print(" " * (size - i) + "*" * (2 * i - 1))
    for i in range(2, size + 1):
        print(" " * (size - i) + "*" * (2 * i - 1))


sandclock(5)

# pygameインストールされているかテスト
import pygame

print(pygame.ver)
