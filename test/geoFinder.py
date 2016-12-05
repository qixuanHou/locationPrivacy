
def connect():
    #return diction
    #la_long - address
    from geopy.geocoders import Nominatim
    #https://github.com/geopy/geopy
    return Nominatim()



def mapToJson(geolocator, la_long):
    location = geolocator.reverse(la_long)

    # withType = geolocator.geocode(location.address)
    # if (withType == None):
    #     print("none + " + la_long)
    #     return location.raw
    print location.raw

# import csv
# g = connect()
# f = open("try.csv", 'r')

# lines = csv.reader(f)

# for row in lines:
# 	pickup = row[11] + ', ' + row[10]
# 	mapToJson(g, pickup)



x = {u'display_name': u'604, 5th Avenue, Diamond District, Manhattan, New York County, NYC, New York, 10020, United States of America', u'place_id': u'121984837', u'lon': u'-73.97818175', u'boundingbox': [u'40.7576609', u'40.7578753', u'-73.9783709', u'-73.9779926'], u'osm_type': u'way', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'266170728', u'lat': u'40.7577681', u'address': {u'city': u'NYC', u'house_number': u'604', u'country': u'United States of America', u'county': u'New York County', u'suburb': u'Manhattan', u'state': u'New York', u'road': u'5th Avenue', u'country_code': u'us', u'neighbourhood': u'Diamond District', u'postcode': u'10020'}}
{u'display_name': u'Citi Bike - Barrow St & Hudson St, Barrow Street, Greenwich Village, Manhattan, New York County, NYC, New York, 10014, United States of America', u'place_id': u'48329610', u'lon': u'-74.0067443', u'boundingbox': [u'40.7316243', u'40.7318243', u'-74.0068443', u'-74.0066443'], u'osm_type': u'node', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'3708656252', u'lat': u'40.7317243', u'address': {u'city': u'NYC', u'country_code': u'us', u'country': u'United States of America', u'county': u'New York County', u'suburb': u'Manhattan', u'state': u'New York', u'road': u'Barrow Street', u'address29': u'Citi Bike - Barrow St & Hudson St', u'neighbourhood': u'Greenwich Village', u'postcode': u'10014'}}
{u'display_name': u'19, 8th Avenue, Chelsea, Manhattan, New York County, NYC, New York, 10014, United States of America', u'place_id': u'117299746', u'lon': u'-74.0047484898651', u'boundingbox': [u'40.7377922', u'40.7378902', u'-74.0048152', u'-74.0046818'], u'osm_type': u'way', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'250490458', u'lat': u'40.73784115', u'address': {u'city': u'NYC', u'house_number': u'19', u'country': u'United States of America', u'county': u'New York County', u'suburb': u'Manhattan', u'state': u'New York', u'road': u'8th Avenue', u'country_code': u'us', u'neighbourhood': u'Chelsea', u'postcode': u'10014'}}
{u'display_name': u'520 Madison Avenue, 520, Madison Avenue, Diamond District, Manhattan, New York County, NYC, New York, 10037, United States of America', u'place_id': u'120328424', u'lon': u'-73.9744251505177', u'boundingbox': [u'40.7599002', u'40.760584', u'-73.9748886', u'-73.9740314'], u'osm_type': u'way', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'266010397', u'lat': u'40.76022135', u'address': {u'building': u'520 Madison Avenue', u'city': u'NYC', u'house_number': u'520', u'country': u'United States of America', u'county': u'New York County', u'suburb': u'Manhattan', u'state': u'New York', u'road': u'Madison Avenue', u'country_code': u'us', u'neighbourhood': u'Diamond District', u'postcode': u'10037'}}
{u'display_name': u'Delecctica, 534, 3rd Avenue, Tudor City, Manhattan, New York County, NYC, New York, 10035, United States of America', u'place_id': u'4953492', u'lon': u'-73.9762059', u'boundingbox': [u'40.748403', u'40.748603', u'-73.9763059', u'-73.9761059'], u'osm_type': u'node', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'561239802', u'lat': u'40.748503', u'address': {u'city': u'NYC', u'house_number': u'534', u'country': u'United States of America', u'county': u'New York County', u'suburb': u'Manhattan', u'state': u'New York', u'road': u'3rd Avenue', u'country_code': u'us', u'cafe': u'Delecctica', u'neighbourhood': u'Tudor City', u'postcode': u'10035'}}
{u'display_name': u'806, Lexington Avenue, Diamond District, Manhattan, New York County, NYC, New York, 10065, United States of America', u'place_id': u'124305533', u'lon': u'-73.96695085', u'boundingbox': [u'40.7642768', u'40.7644301', u'-73.9670942', u'-73.9668075'], u'osm_type': u'way', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'266236265', u'lat': u'40.76435345', u'address': {u'city': u'NYC', u'house_number': u'806', u'country': u'United States of America', u'county': u'New York County', u'suburb': u'Manhattan', u'state': u'New York', u'road': u'Lexington Avenue', u'country_code': u'us', u'neighbourhood': u'Diamond District', u'postcode': u'10065'}}
{u'display_name': u'202, West 23rd Street, Chelsea, Manhattan, New York County, NYC, New York, 10011, United States of America', u'place_id': u'28437566', u'lon': u'-73.9959158', u'boundingbox': [u'40.7439388', u'40.7441388', u'-73.9960158', u'-73.9958158'], u'osm_type': u'node', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'2703092664', u'lat': u'40.7440388', u'address': {u'city': u'NYC', u'house_number': u'202', u'country': u'United States of America', u'county': u'New York County', u'suburb': u'Manhattan', u'state': u'New York', u'road': u'West 23rd Street', u'country_code': u'us', u'neighbourhood': u'Chelsea', u'postcode': u'10011'}}
{u'display_name': u"11 Times Square, 11, 8th Avenue, Hell's Kitchen, Manhattan, New York County, NYC, New York, 10036, United States of America", u'place_id': u'122643272', u'lon': u'-73.9896568259498', u'boundingbox': [u'40.7562425', u'40.7570057', u'-73.9899774', u'-73.9890938'], u'osm_type': u'way', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'266143341', u'lat': u'40.7566036', u'address': {u'building': u'11 Times Square', u'city': u'NYC', u'house_number': u'11', u'country': u'United States of America', u'county': u'New York County', u'suburb': u'Manhattan', u'state': u'New York', u'road': u'8th Avenue', u'country_code': u'us', u'neighbourhood': u"Hell's Kitchen", u'postcode': u'10036'}}
{u'display_name': u'430, 3rd Avenue, Tudor City, Manhattan, New York County, NYC, New York, 10016, United States of America', u'place_id': u'26074133', u'lon': u'-73.9802026', u'boundingbox': [u'40.7430739', u'40.7432739', u'-73.9803026', u'-73.9801026'], u'osm_type': u'node', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'2549932991', u'lat': u'40.7431739', u'address': {u'city': u'NYC', u'house_number': u'430', u'country': u'United States of America', u'county': u'New York County', u'suburb': u'Manhattan', u'state': u'New York', u'road': u'3rd Avenue', u'country_code': u'us', u'neighbourhood': u'Tudor City', u'postcode': u'10016'}}

print(x[display_name])
def plotMap(aFile):
    import gmplot
    import json
    f = open(aFile, 'r')
    lines = f.readlines()
    latitudes = list()
    longitudes = list()
    for line in lines:
        a = json.loads(line)
        try:
            lat = float(a['pickup']['lat'])

            lon = float(a['pickup']['lon'])
           
            latitudes.append(lat)
            longitudes.append(lon)
            print(longitudes)
        except:
            pass

    gmap = gmplot.GoogleMapPlotter(40.7509149, -73.9893313859352, 12)
    gmap.heatmap(latitudes, longitudes)


    gmap.draw("mymap.html")

	#https://github.com/vgm64/gmplot
# gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
# gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
# gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
# gmap.heatmap(heat_lats, heat_lngs)



def readJson(aFile):
    import json
    f = open(aFile, 'r')
    lines = f.readlines()
    for line in lines:
        a = json.loads(line)
        try:
            x = a['pickup']['osm_type']
            print(x)
        except:
            pass



def findType(aFile, newF):
    import csv
    import json


    f = open(aFile, 'r')
    new = open(newF, 'w')

    lines = f.readlines()
    for row in lines:
        x = json.loads(row)
        p = x["pickup"]["display_name"]
        d = x["dropoff"]["display_name"]
        wd = g.geocode(d)
        wp = g.geocode(p)
        if (wp == None):
            pass
        else:
            x["pickup"]["type"] = wp.raw["type"]
        if (wd == None):
            pass
        else:
            x["dropoff"]["type"] = wd.raw["type"]
        json.dump(x, new)
    
        new.write("\n")
    new.close()
    f.close()
findType("result_withoutType.txt", "withType.txt")







def writeJson(aFile, newFile):
    import csv
    import json


    f = open(aFile, 'r')
    newf = open(newFile, 'a')

    reader = csv.reader(f)
    g = connect()
    for row in reader:

        # result = {}
        # pickup = row[11] + ', ' + row[10]
        # dropoff = row[13] + ', ' + row[12]
        
        pickupRaw = mapToJson(g, "40.751171, -73.989838")
        print pickupRaw

        # dropoffRaw = mapToJson(dropoff)
        # dropoffRaw['dateTime'] = row[5]
        # pickupRaw['dateTime'] = row[6]
        # result['driverID'] = row[0]
        # result['trip_distance'] = row[9]
        # result['pickup'] = pickupRaw
        # result['dropoff'] = dropoffRaw

        # json.dump(result, newf)
        # newf.write("\n")
    f.close()
    newf.close()

