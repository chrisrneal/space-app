from twitter_search import TwitterSearch
import datetime
import csv
import json


locations = [(40.787764, -73.962949, 'new_york'),  # new york
(37.798926, -122.414257, 'san_fran'), # san fran 
(34.034023, -118.242361, 'LA'), # LA
(43.696059, -79.413813, 'toronto') # Toronto
] 

# locations = [(40.787764, -73.962949, 'new_york')]  # new york
 
key_words = ["flu", "asthma", "allergy"]

# key_words = ["flu"]

twitter_connection = TwitterSearch()

NUM_RESULTS = 5000
RADIUS = 10	


log = open("mining.log", "a+")
log = csv.writer(log)

for word in key_words:
	for location in locations:

		latitude = location[0]
		longitude = location[1]
		city = location[2]
		search_word = word
		radius = RADIUS
		num_results = NUM_RESULTS


		tweets, tweets_raw = twitter_connection.query(lat=latitude, lng=longitude, search_word=search_word, radius=radius, num_results=num_results)
		number_tweets = len(tweets)


		now = datetime.datetime.now().isoformat().replace(':','-').replace('.','-').replace(':','')
		f_name = "time-{}-{}-{}.DATA".format(now, city, search_word)
		f = open(f_name, 'w+')
		writer  = csv.writer(f)
		for tweet in tweets:
			writer.writerow(tweet)

		print latitude, longitude, search_word,
		print number_tweets, f_name	
		log.writerow([city, search_word, number_tweets, f_name])
		
		f_json_name = "time-{}-{}-{}.json".format(now, city, search_word)

		with open(f_json_name, 'w+') as outfile:
			json.dump(tweets_raw, outfile, indent=4)	