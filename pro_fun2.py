import const

def fun():
	# Manager.dict()当value为list(可变对象)时，不能直接修改，必须重新赋值。
	# 错误做法 ：const.aDict['3'].append(100)
	l = const.aDict['3']
	l.append(100)
	const.aDict['3'] = l
	print("const.aDict: ",const.aDict)