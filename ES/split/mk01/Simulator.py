import sys
import copy

def dim(): 
	return 200

def evalmax(): 
	return 200 * 10

count = 0;
wbest = [-1] * dim()
fbest = sys.maxsize

def evaluate(answer): 
	data = (897,981,371,624,361,530,578,203,799,308,194,261,672,782,666,559,964,458,731,222,636,682,218,123,592,376,933,106,189,130,768,87,98,6,915,363,165,992,297,166,952,547,640,24,334,528,460,40,501,723,761,257,987,969,120,171,931,763,190,170,383,829,845,544,901,143,196,519,874,82,902,397,768,71,941,30,67,759,589,662,248,723,723,809,469,318,657,327,103,170,625,453,509,968,862,638,609,923,605,81,546,147,422,232,585,599,216,265,509,587,976,689,706,356,864,525,564,991,642,262,892,889,733,420,561,163,858,873,800,474,768,932,889,791,498,574,968,873,205,971,264,651,65,164,37,782,70,800,613,605,180,507,792,823,703,238,610,237,482,17,231,52,18,304,246,589,896,941,469,975,213,863,302,713,280,242,768,382,550,613,279,308,96,732,859,452,284,640,184,686,577,16,282,57,642,240,78,53,135,415)

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
