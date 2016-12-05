


def mapToJson(la_long):
	#return diction
	#la_long - address
	from geopy.geocoders import Nominatim
	geolocator = Nominatim()
	location = geolocator.reverse(la_long)
	print location.raw
	return location.raw



import csv
import geocoder
x = open("trip_data_1.csv", 'r')
f = open("result.csv", "w")

lines = csv.reader(x)

for row in lines:
	pickup = row[11] + ', ' + row[10]
	dropoff = row[13] + ', ' + row[12]

	p = mapToJson(pickup)

	ptype = geocoder.osm(p["display_name"])
	d = mapToJson(dropoff)
	dtype = geocoder.osm(d["display_name"])
	f.write("=======================================\n")
	f.write(p["display_name"] + "\n")
	f.write(row[5] + "\n")
	try:
		f.write(ptype.json["type"] + "\n")
	except:
		f.write("not found" + "\n")
	try: 
		f.write(ptype.json["quality"] + "\n")
	except:
		f.write("not found\n")

	f.write(d["display_name"] + "\n")
	f.write(row[6] + "\n")
	try:
		f.write(dtype.json["type"] + "\n")
	except:
		f.write("not found\n")
	try: 
		f.write(dtype.json["quality"] + "\n")
	except:
		f.write("not found\n")

	

#89D227B655E5C82AECF13C3F540D4CF4,BA96DE419E711691B9445D6A6307C170,CMT,1,N,2013-01-01 15:11:48,2013-01-01 15:18:10,4,382,1.00,-73.978165,40.757977,






