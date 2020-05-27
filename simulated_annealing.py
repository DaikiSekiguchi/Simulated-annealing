# coding: utf-8

import math
import random

"""
y = 3x^4 − 5^3 + 2^2 の最小値を求める(焼きなまし法)

アルゴリズム
＜初期化処理＞
- ランダムな値で変数を初期化。

＜反復処理＞
1. 変更する変数を一つ選ぶ。
2. 変数の値を増加させるか、減少させるかを決定する。
3. 変数の値を変更後、新たら変数でコストを算出する。
4. 変更前と変更後のコストの大小を比較する。
5. 変更後のコストが小さければ採用する。コストが大きければ、確率的に採用する。
6. 温度を下げる。

＜終了条件＞
- 反復回数または温度指定。
"""


# 状態のスコア計算
def calc_score(x):
    return (3 * (x ** 4)) - (5 * (x ** 3)) + (2 * (x ** 2))


# 焼きなまし法
def simulated_annealing(current_temperature):
    cool = 0.99
    current_x = random.uniform(-10, 10)
    current_score = calc_score(current_x)

    while 0.001 < current_temperature:
        # 遷移する大きさを決定
        step = random.random()

        # 変数(x)の値を増加させるか、減少させるか
        temp_x1 = step
        temp_x2 = -step

        temp_score1 = calc_score(temp_x1)
        temp_score2 = calc_score(temp_x2)

        # 変更後のスコアを決定する
        if temp_score1 < temp_score2:
            new_x = temp_x1
            new_score = temp_score1
        else:
            new_x = temp_x2
            new_score = temp_score2

        # 温度から確率を定義する
        prob = pow(math.e, -abs(new_score - current_score) / current_temperature)

        # 変更後のコストが小さければ採用する。コストが大きければ、確率的に採用する。
        if (new_score < current_score) or (random.random() < prob):
            current_x = new_x
            current_score = new_score

        # 温度を下げる
        current_temperature = current_temperature * cool

    return current_x


if __name__ == "__main__":

    success, failure = 0, 0

    for i in range(0, 1000):
        ans = simulated_annealing(10000)

        if -0.05 <= ans <= 0.05:
            failure += 1

        if 0.8 < ans <= 0.9:
            success += 1

    print(success, failure)
