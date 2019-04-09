import const

def target_fun():
	#const.aDict['2'][1]+=10
	l = const.aDict['2']
	l[1] += 10
	const.aDict['2'] = l
	print("const.aDict: ",const.aDict)
