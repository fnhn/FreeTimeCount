# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import os
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


course_id = 0
f1 = open('4.txt', 'w')



colleges = (
	u'社会科学学院',
	u'教务部()',
	u'MOOC',
	u'材料学院',
	u'传播学院',
	u'大学英语教学部',
	u'电子科学与技术学院',
	u'法学院',
	u'高等研究院',
	u'高尔夫学院',
	u'管理学院',
	u'光电工程学院',
	u'国际交流学院',
	u'化学与化工学院',
	u'机电与控制工程学院',
	u'计算机与软件学院',
	u'建筑与城市规划学院',
	u'经济学院',
	u'生命科学学院',
	u'师范学院',
	u'数学与计算科学学院',
	u'体育部',
	u'图书馆',
	u'土木工程学院',
	u'外国语学院',
	u'文学院',
	u'武装部',
	u'物理科学与技术学院',
	u'校团委',
	u'信息工程学院',
	u'学生部',
	u'医学院',
	u'艺术设计学院',
	u'招生就业办公室',
	u'中国经济特区研究中心',
)

url = "http://192.168.2.20/newkc/akcjj0.asp?xqh=20142"
cookiejar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
urllib2.install_opener(opener)
response = urllib2.urlopen(url)
content = response.read()
content = content.decode("gb18030")
print content

url = "http://192.168.2.20/newkc/akechengdw.asp"
response = urllib2.urlopen(url)
content = response.read()
content = content.decode("gb18030")
print content


url = "http://192.168.2.20/newkc/kccx.asp?flag=kkdw"


txt = open("2.txt", "w")

for college in colleges:

	values = {
		'bh': college,
	}

	values['bh'] = values['bh'].encode("gb18030")
	values = urllib.urlencode(values)
	request = urllib2.Request(url, values)
	response = urllib2.urlopen(request)
	content = response.read()
	content = content.decode("gb18030")
	#print content
	#content = unicode(content, "gbk2312").encode('utf8')
	page = open("1.html", "w")

	page.write(content)
	page.close()

	obj_course = re.compile('<td width=.*152.*><a href=\"(.+)\".*>(.*)</a>[.\r\n]*</td>')
	course = obj_course.findall(content)
	obj_time = re.compile("<td width=\"150\">(<small><small>)?(.*)</td>")
	time = obj_time.findall(content)

	i = 0
	for each in course:
		a = each[0].strip()
		c = each[1].strip()
		t = time[i][1].replace("<small/><small/>", "").strip()

		if t == "上课时间":
			i = i + 1
			t = time[i][1].replace("<small/><small/>", "").strip()

		txt.write(str(course_id) + "|" + c + "|" + t + "\n")

		url_students = "http://192.168.2.20/newkc/" + a;
		print url_students
		response = urllib2.urlopen(url_students)
		content = response.read().decode("gb18030")
		obj_stunos = re.compile('<td>([0-9]{10})</td>')
		stunos = obj_stunos.findall(content)

		f1.write(str(course_id))
		for stuno in stunos:
			f1.write(" " + stuno)
		f1.write("\n")

		i = i + 1

		course_id = course_id + 1



txt.close()
f1.close()
