import urllib2, json,base64
accesstoken="USALXFD8FEZA1SEPBFJP"
Institution="10007772"
course="U56119"
page=0
url="http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(Institution,course)
request=urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n', ''))

response=urllib2.urlopen(request)
data=json.load(response)
#print json.dumps(data,indent=2)

for c in data:
	if c['Code']=="SALARY":
		det=c['Details']
		for d in det:
			if d['Code']=="INSTMED":
				print "The median salary 6 months after graduation for Software Engineering students from Napier is" ,d['Value']

for c in data:
	if c['Code']=="SALARY":
		det=c['Details']
		for d in det:
			if d['Code']=="LDMED":
				print "The median salary in the sector for software engineering graduates 40 months after graduation is",d['Value']


for c in data:
	if c['Code']=="NSS":
		det=c['Details']
		for d in det:
			if d['Code']=="Q1":
				print "The proportion of software engineering students who agree or strongly agree with the statement Staff are good at explaining things is",d['Value']