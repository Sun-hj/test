#1-100之间除去7的倍数并且数字中含7的数，其余每行打印一个数字。
a=0
while a <100:
	a+=1
	if a%7==0:
		continue
	elif a%10==7:
		continue
	elif a//10==7:
		continue
	print(a)