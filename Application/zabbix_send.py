#!/usr/bin/python
#coding=utf-8
import urllib
import urllib2
import json
import sys
import socket
reload(sys)
sys.setdefaultencoding('utf8')
print "脚本名称:", sys.argv[0]
def problemMessage():
  return "##### <font color=red> Monitor message \nProblem\n </font>"

def resolvedMessage():
  return "##### <font color=green> Monitor message \nResolved </font>"

def errorMessage():
#  return (sys.argv[1])
  return "##### <font color=red> %s </font>" % sys.argv[1]
def extractionMessage():
  return problemMessage() + '\n' + errorMessage()

def sendDingDingMessage(url, data):
  req = urllib2.Request(url)
  req.add_header("Content-Type", "application/json; charset=utf-8")
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
  response = opener.open(req, json.dumps(data))
  return response.read()

def main():
  posturl = "https://oapi.dingtalk.com/robot/send?access_token=38ea4a51e74603e0b369ac2c74d831355c3a181b52b40ffa7286abcb63b121a5"
  data = {"msgtype": "markdown", "markdown": {"text": extractionMessage(),"title": "Monitor Message"}, "at": {"atMobiles": "15622361127", "isAtAll": "false"}}
  sendDingDingMessage(posturl, data)

main()
