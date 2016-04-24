# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:00:08 2016

@author: Tobi
"""
import csv

class rawDataSet:
    def __init__(self, file):
        self.geoData = []
        with open(file, 'r+') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                 self.geoData.append([float(x) for x in row])
        self.height, self.width = self._pixelSize()
        self.height/=2
        self.width/=2
                 
    def _pixelSize(self):
        dim = []
        dim.append(abs(self.geoData[0][0]-self.geoData[1][0]))
        dim.append(abs(self.geoData[0][1]-self.geoData[1][1]))
        return dim
        #is the pixle size homogeneous?
        for i in range(len(self.geoData)-1):
            print(self.geoData[i+1][0]-self.geoData[i][0]) 
        
    def getData(self, lat, long):
        for point in self.geoData:
            if lat >= point[0]-self.height and lat <= point[0]+self.height:
                if long >= point[1]-self.width and long <= point[1]+self.width:
                    return [point[i] for i in range(2,len(point))]
                    break
    
    