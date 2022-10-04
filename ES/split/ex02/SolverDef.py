import random

# ランダムなアドレスを返す
# 引数は出力する長さ
def makeRandAddress(len):
    address = []
    for i in range(len):
        address.append(random.randint(0, 1))
    return address


# 最小スコアの配列を返す
# 引数はスコアとアドレス
def minScore(score, address):
    minTmp = min(score)
    index = score.index(minTmp)
    return address[index]


# ランダムに1/10個値を反転させる
# 引数は配列
def evoAddress(core):
    limit = int(len(core) / 10) # 反転させる要素数
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