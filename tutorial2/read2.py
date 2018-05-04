import urllib2, json,base64,re
accesstoken="USALXFD8FEZA1SEPBFJP"
Institution="10007772" #napier
#Institution="10007849"  #Abertay

#page=2 #computing at Napier
page=4 #Software Engineering  at napier
#page = 0 #Accounting and Finance at Arbertay
url="http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Courses.json?pageIndex={}".format(Institution,page)
request=urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n', ''))

response=urllib2.urlopen(request)
data=json.load(response)
for c in data:
# # 	# if c['Title']== "Computing":
	if c['Title']== "Software Engineering":

	#if c['Title']=='Accounting and Finance':
		print c['KisCourseId'],c['Title']

# for c in data:
# 	print c['KisCourseId'],c['Title']