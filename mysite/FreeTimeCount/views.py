# -*- coding: utf8 -*-

from django.template.response import TemplateResponse
from FreeTimeCount.models import *
import re
import string
import datetime

# Create your views here.

def index(request):
	response = TemplateResponse(request, 'FreeTimeCount/index.html', {})
	return response

def date(request):

	time1_2 = []
	time3_4 = []
	time5_6 = []
	time7_8 = []
	time9_10 = []
	time11_12 = []
	week_day = None

	is_time1_2_free = True
	is_time3_4_free = True
	is_time5_6_free = True
	is_time7_8_free = True
	is_time9_10_free = True
	is_time11_12_free = True

	if request.POST:


		end_date = request.POST['date']

		start_date = datetime.datetime(2015, 3, 2)

		obj = re.compile('(\d+)-(\d+)-(\d+)')
		end_date = obj.findall(end_date)
		print end_date
		print end_date[0][0] + end_date[0][1] + end_date[0][2]

		end_date = datetime.datetime(string.atoi(end_date[0][0]), string.atoi(end_date[0][1]), string.atoi(end_date[0][2]))
		days = (end_date - start_date).days

		week_day = end_date.strftime("%w")
		print "week_day=" + week_day

		is_single_week = 1 if (days / 7) % 2 == 0 else 0

		for member in Member.objects.all():

			if member.stuID[3] != '4':
				continue

			is_time1_2_free = True
			is_time3_4_free = True
			is_time5_6_free = True
			is_time7_8_free = True
			is_time9_10_free = True
			is_time11_12_free = True

			student = Students.objects.filter(stu_no=member.stuID)
			courseTable = CourseTable.objects.filter(student=student)
			for ct in courseTable:
				courses = Course.objects.filter(course_id=ct.course_id)
				for course in courses:
					if course.weekday != '0':

						if is_single_week:
							if (course.weekday[1] == str(week_day)) and (course.weekday[0] == '0' or course.weekday[0] == '1'):
								course_time = course.time.strip("[']")
								print "course_time=" + course_time
								masses = course_time.split(",")

								for mass in masses:
									if mass == '1' or mass == '2':
										is_time1_2_free = False
									if mass == '3' or mass == '4':
										is_time3_4_free = False
									if mass == '5' or mass == '6':
										is_time5_6_free = False
									if mass == '7' or mass == '8':
										is_time7_8_free = False
									if mass == '9' or mass == '10':
										is_time9_10_free = False
									if mass == '11' or mass == '12':
										is_time11_12_free = False
						else:
							if (course.weekday[1] == str(week_day)) and (course.weekday[0] == '0' or course.weekday[0] == '2'):
								course_time = course.time.strip("[']")
								print "course_time=" + course_time
								masses = course_time.split(",")

								for mass in masses:
									if mass == '1' or mass == '2':
										is_time1_2_free = False
									if mass == '3' or mass == '4':
										is_time3_4_free = False
									if mass == '5' or mass == '6':
										is_time5_6_free = False
									if mass == '7' or mass == '8':
										is_time7_8_free = False
									if mass == '9' or mass == '10':
										is_time9_10_free = False
									if mass == '11' or mass == '12':
										is_time11_12_free = False

			if is_time1_2_free:
				time1_2.append(student[0].name)
			if is_time3_4_free:
				time3_4.append(student[0].name)
			if is_time5_6_free:
				time5_6.append(student[0].name)
			if is_time7_8_free:
				time7_8.append(student[0].name)
			if is_time9_10_free:
				time9_10.append(student[0].name)
			if is_time11_12_free:
				time11_12.append(student[0].name)		

						
	else:
		print "not a post"

	if week_day == '日':
		week_day = '一'
	elif week_day == '1':
		week_day = '一'
	elif week_day == '2':
		week_day = '二'
	elif week_day == '3':
		week_day = '三'
	elif week_day == '4':
		week_day = '四'
	elif week_day == '5':
		week_day = '五'
	elif week_day == '6':
		week_day = '六'


	response = TemplateResponse(request, 'FreeTimeCount/date.html', {
		"time1_2" 	: ",".join(time1_2),
		"time3_4" 	: ",".join(time3_4),
		"time5_6" 	: ",".join(time5_6),
		"time7_8" 	: ",".join(time7_8),
		"time9_10"	: ",".join(time9_10),
		"time11_12"	: ",".join(time11_12),
		"week_day"	: week_day,
		"date"		: (request.POST['date'] if request.POST else None),
	})
	return response

def distribute(request):


	response = TemplateResponse(request, 'FreeTimeCount/distribute.html', {})
	return response


def member(request):

	courseTable = None
	student = None
	courses = []

	if request.POST:

		name = request.POST['name'].strip()
		number = request.POST['number'].strip()



		if len(name) != 0:
			student = Students.objects.filter(name=name)
			courseTable = CourseTable.objects.filter(student=student)
			for ct in courseTable:
				courses.append(Course.objects.filter(course_id=ct.course_id))

		elif len(number) != 0:
			student = Students.objects.filter(stu_no=number)
			courseTable = CourseTable.objects.filter(student=student)
			for ct in courseTable:
				courses.append(Course.objects.filter(course_id=ct.course_id))


	else:
		print 'not a post request'

	response = TemplateResponse(request, 'FreeTimeCount/member.html', {"students": student, "courses": courses, "len": (len(student) if student != None else 0)})
	return response

def insert(request):
	'''Students.objects.all().delete()
	Course.objects.all().delete()
	CourseTable.objects.all().delete()

	# Step1
	file = open("FreeTimeCount/info/students.txt", "r")
	content = file.read()
	file.close()

	pieces = content.split("|")

	i = 2
	c = 5
	index = 0
	query_set_list = []
	while i < len(pieces):
		if len(pieces[i].strip()) != 0:
			c = c + 1
		if c == 6:
			c = 0
			print pieces[i]

			if pieces[i - 1] != u'学号':
				try:
					s = Students(id=index, stu_no=pieces[i - 1], name=pieces[i], sex=pieces[i + 1], major=pieces[i + 2],college=pieces[i + 3])
				except:
					print "error"

			index = index + 1

			query_set_list.append(s)

		i = i + 1

	Students.objects.bulk_create(query_set_list)


	# Step2
	file = open("FreeTimeCount/info/course.txt", "r")
	content = file.read()
	file.close()

	pieces = content.split("\n")


	query_set_list = []
	index = 0

	for piece in pieces:

		print "piece=" + piece

		if len(piece) == 0:
			continue

		weekday = "0"
		time = "0"
		mass = piece.split("|")

		id = string.atoi(mass[0])
		course_name = mass[1]

		if mass[2] == "." or len(mass) == 2 or len(mass[2]) == 0:
			print "the time session is empty"
			s =  Course(id=index, course_id=id, weekday=weekday, course_name=course_name, time=time, place="wenkelou")
			index = index + 1
			#print "id=" + str(id + 1)
			query_set_list.append(s)
		else:
			print "mass[2]=" + mass[2]

			masses = mass[2].split(";");

			for m in masses:
				if m.find('单') != -1:
					weekday = "1"
				elif m.find('双') != -1:
					weekday = "2"
				else:
					weekday = "0"

				if m.find('一') != -1:
					weekday = weekday + "1"
				elif m.find('二') != -1:
					weekday = weekday + "2"
				elif m.find('三') != -1:
					weekday = weekday + "3"
				elif m.find('四') != -1:
					weekday = weekday + "4"
				elif m.find('五') != -1:
					weekday = weekday + "5"
				elif m.find('六') != -1:
					weekday = weekday + "6"
				elif mass.find('日') != -1:
					weekday = weekday + "7"

				print "weekday=" + str(weekday)

				obj = re.compile('([,0-9]+)')
				time = obj.findall(m)
				s =  Course(id=index, course_id=id, weekday=weekday, course_name=course_name, time=time, place="wenkelou")
				index = index + 1
				#print "id=" + str(id + 1)
				query_set_list.append(s)


	Course.objects.bulk_create(query_set_list)





	#Step3

	file = open("FreeTimeCount/info/course_detail.txt", "r")
	content = file.read()
	file.close()

	index = 0
	query_set_list = []

	pieces = content.split("\n")

	for student in Students.objects.all():
		print student.name

		for piece in pieces:

			if len(piece) == 0:
				break

			if piece.find(student.stu_no) != -1:
				mass = piece.split(" ")
				ct = CourseTable(id=index, student=student, course_id=mass[0])
				index = index + 1
				query_set_list.append(ct)

	CourseTable.objects.bulk_create(query_set_list)'''

	Member.objects.all().delete()


	m = Member(stuID="2013150099"); m.save();	
	m = Member(stuID="2013150030"); m.save();	
	m = Member(stuID="2013800169"); m.save();
	m = Member(stuID="2014150169"); m.save();
	m = Member(stuID="2014150168"); m.save();
	m = Member(stuID="2014160073"); m.save();
	m = Member(stuID="2014072033"); m.save();
	m = Member(stuID="2014020536"); m.save();
	m = Member(stuID="2014150122"); m.save();
	m = Member(stuID="2014150278"); m.save();
	m = Member(stuID="2014150063"); m.save();
	m = Member(stuID="2014150240"); m.save();
	m = Member(stuID="2014150262"); m.save();
	m = Member(stuID="2014150155"); m.save();
	m = Member(stuID="2014150211"); m.save();
	m = Member(stuID="2014150239"); m.save();
	m = Member(stuID="2014150261"); m.save();
	m = Member(stuID="2014160123"); m.save();
	m = Member(stuID="2014150231"); m.save();
	m = Member(stuID="2014150329"); m.save();
	m = Member(stuID="2014130107"); m.save();
	m = Member(stuID="2014150105"); m.save();
	m = Member(stuID="2014160015"); m.save();	
	m = Member(stuID="2014150158"); m.save();	
	m = Member(stuID="2014130097"); m.save();
	m = Member(stuID="2014150280"); m.save();	
	m = Member(stuID="2014080125"); m.save();	
	m = Member(stuID="2014160149"); m.save();	
	m = Member(stuID="2014080281"); m.save();


	response = TemplateResponse(request, 'FreeTimeCount/distribute.html', {})
	return response
