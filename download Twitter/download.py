def getTweets(name, countNum):
	from twython import Twython
	t = Twython(app_key='NDVuk92uZ7ki1GlFOh6eOt5DD', #REPLACE 'APP_KEY' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
    app_secret='4DOrAcbMNPhEGAahmpKGhOSEUc5zZMDn0LETU56A795hbpr71q',
    oauth_token='3405518446-vHu6RBTE0hjPwveXcDxsos55Ism9QuebMvzzcql',
    oauth_token_secret='DTEiuQDRpj1U9ZgLAl1HMME3RRf2h02HMrwhsgjKzNMS9')

	user_timeline = t.get_user_timeline(screen_name=name, exclude_replies=True, count=countNum)

	return user_timeline



def writeTxt(data, fileName):
	import simplejson as json
	f = open(fileName + ".js", 'w')
	for ts in data:

		f.write(json.dumps(data))
	f.close()



def writeExcel(fileName, tweet):
    import xlsxwriter
    import json
    f = xlsxwriter.Workbook(fileName + ".xls")
    table = f.add_worksheet()

    table.write(0, 0, 'id')

    table.write(0, 1, 'coordinates')
    table.write(0, 2, 'created_at')
    table.write(0, 3, 'current_user_retweet')
    table.write(0, 4, 'entities')
    table.write(0, 5, 'geo')
    table.write(0, 6, 'in_reply_to_status_id')
    table.write(0, 7, 'in_reply_to_user_id')

    table.write(0, 8, 'place')
    table.write(0, 9, 'quoted_status_id')
    table.write(0, 10, 'source')
    table.write(0, 11, 'text')
    table.write(0, 12, 'user')

    table.write(0, 13, "contributors")

    

    row = 1
    for data in tweet:

        table.write(row, 0, data["id"])
        table.write(row, 1, data["coordinates"])
        table.write(row, 2, data["created_at"])
#        table.write(row, 3, data["current_user_retweet"])
        table.write(row, 4, json.dumps(data["entities"]))
        table.write(row, 5, data["geo"])
        table.write(row, 6, data["in_reply_to_status_id"])
        table.write(row, 7, data["in_reply_to_user_id"])
        table.write(row, 8, json.dumps(data["place"]))
     #   table.write(row, 9, data["quoted_status_id"])
        table.write(row, 10, data["source"])
        table.write(row, 11, data["text"])
        table.write(row, 12, json.dumps(data["user"]))
        table.write(row, 13, data["contributors"])
        row = row + 1
    f.close()




a = getTweets("queencodemonkey", 200)
writeTxt(a, "queencodemonkey")
writeExcel("queencodemonkey", a)


