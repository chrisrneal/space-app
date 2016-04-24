# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 02:13:09 2016

@author: Tobi
"""
#MCDAODHD.A2016106.1200.051.NRT
#AIRS.2016.04.15.216.L2.RetStd.v6.0.31.0.G16107141544.hdf
aerosolDir = "Data/Aerosol/"
relhumDir = "Data/RelHum/"
so2Dir = "Data/SO2/"
SRCH_TRMS=['flu', 'cough', 'allergies']
dataSets=[]
 #trainingData # Tweets by # environmental factors array
trainingData=[]
trainingLables=[]

#for  each of the 7 days
for t in range(7):
    #need load data set for every instramen
    dataSets.append(rawDataSet(aerosolDir+"MCDAODHD.A20161"+str(t+6).zfill(2) +".0600.051.NRT.csv"))
    tweets = getTweets() #should this happen out side of loop? bulk collection of tweets?
    for q in tweets:
        trainingData.append([])
        trainingData[-1]=[set.getData(q['lat'], q['long']) for set in dataSets]
        #need a better system for categorazing
        if q.text==SRCH_TRMS[0]:
            tweetType = 0
        elif q.text==SRCH_TRMS[1]:
            tweetType = 1
        elif q.text==SRCH_TRMS[2]:
            tweetType = 2
        trainingLables.append(tweetType)
    del dataSets[:]