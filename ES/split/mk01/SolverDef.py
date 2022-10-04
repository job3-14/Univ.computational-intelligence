import random

bit = 150  #ビット反転数

# ランダムなアドレスを返す
# 引数は出力する長さ
def makeRandAddress(len):
    address = []
    for i in range(len):
        address.append(random.randint(0, 1))
    return address


# 最小スコアの配列を返す
# 引数はスコアとアドレスと親の数
def minScore(score, address, par):
    core = []
    sortdScore = []
    sortdScore = sorted(score)
    for i in range(par):
        minTmp = sortdScore[i]
        index = score.index(minTmp)
        core.append(address[index])
    return core


# ランダムに1/10個値を反転させる
# 引数は配列
def evoAddress(core):
    limit = int(len(core) / bit) # 反転させる要素数
    chengeAddress = []
    for i in range(limit):
        while True:
            tmp = random.randint(0, len(core)-1)
            if(not(tmp in chengeAddress)):
                chengeAddress.append(tmp)
                break

    for i in range(len(chengeAddress)):
        tmp = chengeAddress[i]
        if(core[tmp] == 0):
            core[tmp] = 1
        else:
            core[tmp] = 0
    return core