import os 
from pro_fun import target_fun
from pro_fun2 import fun
import const
import multiprocessing
from multiprocessing import Manager


def main():
	manager = Manager()
	const.aDict = manager.dict()
	# error 写成下面这样相当于重新给变量赋值了，变成了普通的dict,不能在进程间共享
	# const.aDict = {'1':'sun','2':'yi','3':'rong'}
	d = {'1':'sun','2':'yi','3':'rong'}
	for key, value in d.items():
		const.aDict[key] = value
	print("const.aDict",const.aDict)	
	p = multiprocessing.Process(target = target_fun)
	p.start()
	p.join()
	print("const.aDict",const.aDict)
	p2= multiprocessing.Process(target = fun)
	p2.start()
	p2.join()
	print("const.aDict",const.aDict)


if __name__ == "__main__":
	main()