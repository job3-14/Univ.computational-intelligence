import numpy as np

import sys
sys.path.append('.')

import Simulator
import random

# 利用できる整数の個数をNに代入
N = Simulator.dim()

# 解の評価回数上限をmaxに代入
# (max+1)回以上，Simulator.evaluate(w)を呼び出すとエラー
max = Simulator.evalmax()

# ここから下を自分で開発
# このサンプルは 上限回数まで 解をランダムに作って評価しているだけ

w = np.empty(N, dtype=object)

for i in range(max):
	for j in range(N): w[j]=random.randint(0,1)

	# 解 w の評価値を求める
	# w は 長さNの１次元２値配列
	f = Simulator.evaluate(w)

	# 評価値のログ
	#print((i+1), f, sep="\t")

	# 誤差0の解を発見できたら終了
	if(f==0): Simulator.finish()

# 誤差0の解があるとは限らない
# あるとしても 発見できるとは限らない
# 発見できなかったときは 最後に呼び出す
Simulator.finish()


'''
備考

Simulator.py のグローバル変数を直接読み書きするのは禁止
	count
	wbest
	fbest

個々の整数の値を求めることは禁止
	「個々の整数の値を求める」ということは
	分割問題にしか通用しない解法を使う，ということ
	進化計算は，問題の知識を使わず，どの問題でも汎用的に
	解を求めることが可能
'''

