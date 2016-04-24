# -*- coding: utf-8 -*-

"""
the library: https://github.com/sixohsix/twitter
example: https://github.com/ideoforms/python-twitter-examples/blob/master/twitter-search-geo.py
"""

import os
import datetime

from twitter import Twitter, OAuth

class TwitterSearch():
	"""
	use:	
	from twitter_search import TwitterSearch
	twitter_connection = TwitterSearch()
	flu_tweets = twitter_connection.query(lat=51.474144, lng=0.035401, search_word='flu', radius=100, num_results=10)
	for tweet in flu_tweets:
		print tweet
	"""


	def __init__(self):
		self.twitter = Twitter(auth=self._auth())


	def _auth(self):
		ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
		ACCESS_SECRET = os.environ['ACCESS_SECRET']
		CONSUMER_KEY = os.environ['CONSUMER_KEY']
		CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
		return OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

	def query(self, lat=51.474144, lng=0.035401, search_word='', radius=100, num_results=10):
		tweets = []
		last_id = None
		result_count = 0
		while result_count <  num_results:
			query = self.twitter.search.tweets(q = search_word, geocode = "%f,%f,%dkm" % (lat, lng, radius), count = num_results, max_id = last_id)
			
			print "found results #", len(query["statuses"])
			for result in query["statuses"]:
				user = result["user"]["screen_name"]
				text = result["text"]
				text = text.encode('ascii', 'replace')

				if result["geo"]:
					latitude = result["geo"]["coordinates"][0]
					longitude = result["geo"]["coordinates"][1]
				else:
					latitude = lat
					longitude = lng			

				row = (user, text, latitude, longitude)
				tweets.append(row)
				result_count += 1	
				print result_count
			last_id = result["id"]
		return tweets


if __name__ == "__main__":

	twitter_connection = TwitterSearch()
	latitude = 40.7
	longitude = -74.03
	search_word = 'flu'
	num_results = 2000
	radius = 5

	now = datetime.datetime.now().isoformat().replace(':','-').replace('.','-').replace(':','')
	f_name = "time-{}-tweets-lat-{}-lng-{}-query-{}-radius-{}-num_results-{}".format(now, latitude, longitude, search_word, radius, num_results)
	f = open(f_name, 'w+')

	flu_tweets = twitter_connection.query(lat=latitude, lng=longitude, search_word=search_word, radius=radius, num_results=num_results)
	len(flu_tweets)

	for tweet in flu_tweets:
		f.write(str(tweet))
		f.write('\n')

	print "saved in ", f_name