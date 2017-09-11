#	这是Python对Unix系统远程连接的类包装。
#
#	主要使用是开源的 Paramiko 连接和执行，辅助其他模块作为添加。
#
#	连接初始化需要 hostname user password port
#		e.g. Connect('10.10.10.10', 'root', '123456', '22')
#
#	具体方法详情请看帮助
#

import paramiko

#开启调试模式时，需要改成True。
_DEBUG = False

#开启日志模式
paramiko.util.log_to_file('/tmp/Connect.log')

class Connect:
	'''
	Paramiko 类使用
	'''

	def __init__(self, hostname, user, password, port=36000):
		'''
		参数初始化
		SSH连接初始化
		SSH传输初始化
		'''
		self.hostname = hostname
		self.user = user
		self.password = password
		self.port = port

		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(self.hostname, self.port, self.user, self.password)
		
		self.transport = self.ssh.open_sftp()

	def run_shell(self, shell):
		'''
		传输一个shell命令；
		返回执行结果。
		'''
		stdin, stdout, stderr = self.ssh.exec_command(shell)
		result = stdout.readlines()
		return result

	def run_shell_list(self, shell_list):
		'''
		传输一个shell命令列表
		使用for循环，依次执行，并将结果添加到返回列表
		返回结果列表
		'''
		self.resultList = []
		for shell in shell_list:
			stdin, stdout, stderr = self.ssh.exec_command(shell)
			self.resultList.append(stdout.read())
			self.resultList.append(stderr.read())
		return self.resultList

	def get_file(self, remote_path, local_path):
		'''
		从客户端服务器 remote_path 下载文件
		放在本地 local_path
		'''
		try:
			self.transport.get(remote_path, local_path)
			print('Get %s success!' % remote_path)
		except:
			print('WARRING! Get %s fail.' % remote_path)

	def put_file(self, local_path, remote_path):
		'''
		从本地服务器 local_path 上传文件
		放在客户端服务器 local_path
		'''
		try:
			self.transport.put(local_path, remote_path)
			print('Put %s success!' % local_path)
		except:
			print('WARRING! Put %s fail.' % local_path)

	def close(self):
		'''
		关闭连接
		'''
		self.transport.close()
		self.ssh.close()

if __name__ == '__main__':
	for ip in open('/tmp/ip.txt'):
		ip = ip.replace("\n","")
		connect_ssh = Connect(ip, 'root', '_Qazxsw123_')
		print('Connect is Success!')
		for script in open('/tmp/script.txt'):
			Script = script.replace("\n","")
			connect_ssh.put_file(Script, Script)
			for line in connect_ssh.run_shell('sh ' + Script):
				print(line)
		connect_ssh.close()
