__author__ = 'mmateja'

import numpy as np
from TakeFillNumbers import TakeFillNumbers
import collections
from PLOT.PLOT import transformtotimestamp

class ConditionData(TakeFillNumbers):

    def __init__(self):
        self.data={}


    def load(self, filename, datafromonefile):
        self.data[filename] = datafromonefile

    def getvalue(self):
        xlist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=(value['value'])
            except TypeError:
                xlist[key]=[]
        return xlist

    def getmax_condition(self):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=np.max(value['value'])
            except TypeError:
                xlist[key]=[]
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['max_Condition'] = xlist.values()
        return ylist

    def getaverage_condition(self):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=np.mean(value['value'])
            except TypeError:
                xlist[key]=[]
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['average_Condition'] = xlist.values()
        return ylist

    def gettime_date(self):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            try:
                xlist[key]=(value['time_year'][5], value['time_month'][5],
                        value['time_day'][5], value['time_hour'][5], value['time_minute'][5], value['time_sec'][5])
            except TypeError:
                xlist[key]=[]
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['time_date']=xlist.values()
        zlist = transformtotimestamp(ylist)
        return zlist
