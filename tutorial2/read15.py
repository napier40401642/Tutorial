import urllib2, json,base64
accesstoken="USALXFD8FEZA1SEPBFJP"
url="http://data.unistats.ac.uk/api/v4/KIS/Institutions.json"

request=urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n', ''))

response=urllib2.urlopen(request)
data=json.load(response)
for c in data:
	
	if c['Name']=="University Of Abertay Dundee": #find University Of Abertay Dundee
		print c['UKPRN'],c['Name']

