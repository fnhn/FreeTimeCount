import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

file = open('info.txt', 'a+')
content = file.read()
file.close()

file1 = open('info.html', 'w')
content = content.decode("gb18030")
file1.write(content)
file1.close()
print 'Done.'