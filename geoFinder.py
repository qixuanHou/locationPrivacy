
def mapToJson(la_long):
	#return diction
	#la_long - address
	from geopy.geocoders import Nominatim
	#https://github.com/geopy/geopy
	geolocator = Nominatim()
	location = geolocator.reverse(la_long)
	return location.raw


def getAttribute(rawLocation, attribute):
	import json
	return rawLocation[attribute]

def appendAttribute(rawLocation, attribute, value):
	rawLocation[attribute] = value
	return rawLocation



def writeToFile(content, file):
    f = open(file, "a")
    f.write(content)
    f.close()

def plotMap():
	import gmplot
	#https://github.com/vgm64/gmplot


def readCSV(file, index):
##        [0]medallion,
##        [1]hack_license,
##        [2]vendor_id,
##        [3]rate_code,
##        [4]store_and_fwd_flag,
##        [5]pickup_datetime,
##        [6]dropoff_datetime,
##        [7]passenger_count,
##        [8]trip_time_in_secs,t
##        [9]rip_distance,
##        [10]pickup_longitude,
##        [11]pickup_latitude,
##        [12]dropoff_longitude,
##        [13]dropoff_latitude
        import csv
        result = list()
        with open(file, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                        result.append(row[index])
        return result



print(readCSV('text.csv', 1))

