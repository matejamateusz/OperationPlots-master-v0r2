__author__ = 'mmateja'

import numpy as np
from TakeFillNumbers import TakeFillNumbers
import collections
class LPCData(TakeFillNumbers):

    def __init__(self):
        self.data={}

    def load(self,filename, datafromonefile):
        self.data[filename] = datafromonefile

    def getmax(self, variablename):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=np.max(value[variablename])
            except TypeError:
                xlist[key]=[]
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['max_'+variablename] = xlist.values()
        return ylist

    def getaverage(self, variablename):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=np.mean(value[variablename])
            except TypeError:
                xlist[key]=[]
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['average_'+variablename] = xlist.values()
        return ylist

    def getvalue(self, variablename):
        xlist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=(value[variablename])
            except TypeError:
                xlist[key]=[]
        return xlist

    def gettime_hour(self):
        xlist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=(value['time_sec']-value['time_sec'][0])/3600
            except TypeError:
                xlist[key]=[]
        return xlist

    def gettime_sec(self):
        xlist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=(value['time_sec'])
            except TypeError:
                xlist[key]=[]
        return xlist

    def gettime_date(self):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=(value['time_sec'][5])
            except TypeError:
                xlist[key]=[]
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['time_date']=xlist.values()
        return ylist
