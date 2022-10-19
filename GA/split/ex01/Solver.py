import numpy as np

import sys
sys.path.append('.')

import Simulator
import SolverDef
import random

# 利用できる整数の個数をNに代入
N = Simulator.dim()

# 解の評価回数上限をmaxに代入
# (max+1)回以上，Simulator.evaluate(w)を呼び出すとエラー
max = Simulator.evalmax()

# ここから下を自分で開発
# このサンプルは 上限回数まで 解をランダムに作って評価しているだけ

#w = np.empty(N, dtype=object)

checkList = [] # シュミレーション用データ

# １０個ランダムでアドレスを作成
for i in range(10):
	checkList.append(SolverDef.makeRandAddress(N))

# スコアを作成
score = []
for i in range(len(checkList)):
	testScore = Simulator.evaluate(checkList[i])
	if(testScore==0): print("割り込み終了!!!!!")
	if(testScore==0): Simulator.finish()
	score.append(testScore)

core = SolverDef.minScore(score, checkList)
#for i in range(10):
#	checkList.append(SolverDef.evoAddress(core))
Simulator.finish()

#if(f==0): Simulator.finish()


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

