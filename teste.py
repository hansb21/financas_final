from DataFile import *

n = 'Tesla'
t = 'TSLA'
temp = DataFile(n,t)

sma7 = temp.getData(7)
sma21 = temp.getData(21)

label7,sma7 = exportDataPlot(sma7,'SMA')
label21,sma21 = exportDataPlot(sma21,'SMA')

print()
len7 = len(sma7)
len21 = len(sma21)
if len7<len21:
	lenMin = len7
else:
	lenMin = len21
bB = False
bS = True
for i in range(lenMin):
	if sma7[i]>sma21[i]:
		if bS:
			print()
			bS = False
			bB = True
		print('B',end='')
	else:
		if bB:
			print()
			bB = False
			bS = True
		print('S',end='')