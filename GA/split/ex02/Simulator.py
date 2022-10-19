import sys
import copy

def dim(): 
	return 100

def evalmax(): 
	return 1000;

count = 0;
wbest = [-1] * dim()
fbest = sys.maxsize

def evaluate(answer): 
	data = (72,51,29,98,46,25,54,82,43,48,43,43,58,60,20,51,40,49,45,53,78,39,26,51,53,54,28,84,37,99,99,81,34,23,52,49,47,58,88,29,65,47,84,20,60,29,41,20,77,25,51,26,42,54,48,20,42,40,32,59,82,49,58,30,34,77,30,71,20,21,56,60,31,23,74,36,52,97,56,50,60,1155,26,99,43,48,35,45,38,34,60,35,34,59,76,37,23,23,58,84)

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
