#

import redis
import configparser
import traceback

class redis_info():
	'''
	连接Redis
	'''
	
	def __self__(self, host, rdb, pwd, port=6379):
		'''
		初始化参数
		'''
		
		self.host = host
		self.rdb = rdb
		self.pwd = pwd
		self.port = port

	def read_conn(self, file_path):
		'''
		读取file_path配置信息
		连接redis
		'''

		config = configparser.ConfigParser()
		config.read(file_path)
		self.host = config.get("redis", "REDIS_HOST")
		self.rdb = config.get("redis", "REDIS_RDB")
		self.pwd = config.get("redis", "REDIS_PWD")
		self.port = config.get("redis", "REDIS_PORT")

		try:
			reids_conn = redis.Redis(self.host, self.port, self.rdb, self.pwd)
			return reids_conn
		except:
			traceback.print_exc()
			return None
		finally:
			print('Redis connect is over!')

if __name__ == '__main__':
	redis_info.read_conn('/tmp/testa.sh')
