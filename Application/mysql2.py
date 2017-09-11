#!/usr/bin/env python
# -*- coding:utf-8 -*-
# zengzhiqian
# 2017-03-13

################################################
##
##	Pymysql	封装类
##
##	功能如下:
##		conn_db	连接mysql
##		exec_db	查询
##		inside_db	更新
##		close	关闭连接
##
################################################

import pymysql

class MysqlDB:

	'''
	Pymysql 类使用
	'''

	def __init__(self, host, user, pwd, db, port=3306, charset='utf8'):
		'参数初始化'
		self.host = host
		self.user = user
		self.pwd = pwd
		self.db = db
		self.port = port
		self.charset = charset

	def conn_db(self):
		'DB连接初始化'
		if not self.db:
			raise(NameError,"没有设置数据库信息")
		self.conn = pymysql.connect(self.host,self.user,self.pwd,self.db,self.port,self.charset)
		self.cur = self.conn.cursor()
		if not self.cur:
			raise(NameError,"连接数据库失败")
		else:
			print('Success Connect %s' % self.host)
			return self.cur

	def exec_db(self, sqlline):
		self.resultList = []
		for line in sqlline:
			r1 = self.cur.execute(line)
			self.resultLis = self.cur.fetchall()
		return self.resultLis

	def inside_db(self, sqlline):
		self.resultList = []
		for line in sqlline:
			r1 = self.cur.execute(line)
			r2 = self.cur.fetchone()
			self.resultList.append((r1,r2))
		self.conn.commit()
		return self.resultList

	def db_close(self):
		self.cur.close()
		self.conn.close()

if __name__ == '__main__':
	run = MysqlDB('192.168.10.102', 'root', '123456', 'test')
	run.conn_db()
	a1 = run.exec_db(['select * from userinfo;'])
	for i in a1:
		print(i)
	run.db_close()
