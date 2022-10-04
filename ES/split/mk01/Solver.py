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

par = 1 #親の数

# ここから下を自分で開発
# このサンプルは 上限回数まで 解をランダムに作って評価しているだけ

#w = np.empty(N, dtype=object)

# １０個ランダムでアドレスを作成
checkList = [] # シュミレーション用データ
for i in range(10):
	checkList.append(SolverDef.makeRandAddress(N))

# スコアを作成
score = []
for i in range(len(checkList)):
	testScore = Simulator.evaluate(checkList[i])
	max -= 1
	if(testScore==0 or max==0): Simulator.finish()
	score.append(testScore)

core = SolverDef.minScore(score, checkList, par)

while True:
	checkList = [] # シュミレーション用データ
	for i in range(len(core)):
		for j in range(10): #進化計算
			checkList.append(SolverDef.evoAddress(core[i]))

	# 更新後スコア作成
	score = []
	for i in range(len(checkList)):
		testScore = Simulator.evaluate(checkList[i])
		#print(checkList[i])
		max -= 1
		if(testScore==0 or max==0): Simulator.finish()
		score.append(testScore)
	core = SolverDef.minScore(score, checkList,par)

Simulator.finish()