import time
import threading

def time_p(*args):
	for value in args:
		print('args %s' % value)

class Use_threading:


	def __init__(self):
		pass

	def worker_th(self, file_list, func):
		for a in file_list:
			for b in xrange(100):
				print(a, b)
				t = threading.Thread(target=func,args=(a))
				t.start()

if __name__ == '__mian__':
	Use_threading.worker_th('/tmp/ip.txt', time_p())
