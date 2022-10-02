import sys
import copy

def dim(): 
	return 5

def evalmax(): 
	return 100

count = 0;
wbest = [-1] * dim()
fbest = sys.maxsize

def evaluate(answer): 
	data = (10, 20, 35, 45, 50)

	global count
	global wbest
	global fbest

	count += 1
	if(count > evalmax()):
		print("評価回数オーバー")
		sys.exit()
		
	if(len(answer)!=len(data)): 
		print("要素数エラー")
		sys.exit()

	for x in answer:
		if ( (x!=0) and (x!=1) ):
			print("要素エラー")
			sys.exit()

	sum=0
	for i in range(len(data)):
		if(answer[i]==0): sum += data[i]
		else: sum -= data[i]

	if(sum<0): sum *= -1

	if(sum < fbest):
		fbest=sum
		wbest = copy.deepcopy(answer)

#	print(count, sum, sep=",")
	return sum

def finish(): 
	print(count, fbest, wbest, sep="\t")
	sys.exit()
