# -*- coding: utf-8 -*-
import urllib2
import urllib
from sgmllib import SGMLParser
 
class ListName(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_h4 = ""
		self.name = []
	def start_option(self, attrs):
		self.is_h4 = 1
	def end_option(self):
		self.is_h4 = ""
	def handle_data(self, text):
		if self.is_h4 == 1:
			self.name.append(text)

class ListName1(SGMLParser):
	def __init__(self):
		SGMLParser.__init__(self)
		self.is_h4 = ""
		self.name = []
	def start_td(self, attrs):
		self.is_h4 = 1
	def end_td(self):
		self.is_h4 = ""
	def handle_data(self, text):
		if self.is_h4 == 1:
			self.name.append(text)
 
url = 'http://192.168.2.20/axsxx/xy1.asp'

college = (
	u'材料学院', 
	u'传播学院', 
	u'电子科学与技术学院', 
	u'法学院', 
	u'高等研究院', 
	u'管理学院', 
	u'光电工程学院', 
	u'国际交流学院', 
	u'国际交流与合作部', 
	u'国际拓展部', 
	u'化学与化工学院', 
	u'机电与控制工程学院', 
	u'计算机与软件学院', 
	u'建筑与城市规划学院', 
	u'经济学院', 
	u'生命科学学院', 
	u'师范学院', 
	u'师范学院（高尔夫学院）', 
	u'数学与计算科学学院', 
	u'土木工程学院',
	u'外国语学院',
	u'文学院',
	u'物理科学与技术学院',
	u'信息工程学院',
	u'医学院',
	u'艺术设计学院',
)

fp = open('info.txt', 'w+')

for each in college:

	values = {
		'bh' : each,
		'SUBMIT' : u'查询'
	}
	for key in values.keys():
		values[key] = values[key].encode('gb2312')

	data = urllib.urlencode(values)
	#data = 'bh=2014%BC%C6%CB%E3%BB%FA%D3%EB%C8%ED%BC%FE%D1%A7%D4%BA08'
	print data

	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	content = response.read()
	listname = ListName()
	listname.feed(content)

	for item in listname.name:
		url1 = 'http://192.168.2.20/axsxx/xy2.asp'

		values1 = {
			'bh' : item.decode('gb2312'),
			'SUBMIT' : u'查询'
		}
		for key1 in values1.keys():
			values1[key1] = values1[key1].encode('gb2312')

		data1 = urllib.urlencode(values1)
		#data = 'bh=2014%BC%C6%CB%E3%BB%FA%D3%EB%C8%ED%BC%FE%D1%A7%D4%BA08'
		print data1

		req1 = urllib2.Request(url1, data1)
		response1 = urllib2.urlopen(req1)
		content1 = response1.read()
		listname1 = ListName1()
		listname1.feed(content1)
		for item1 in listname1.name:
			fp.write(item1.strip() + '|')
fp.close()