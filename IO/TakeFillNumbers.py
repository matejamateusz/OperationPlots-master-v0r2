__author__ = 'mmateja'
import collections
class TakeFillNumbers():

    def takeFillNumbers(self, fillnumber):
        self.fillnumber = fillnumber

    def getfillnumber(self):
        xlist = {}
        ylist = {}
        for z in self.fillnumber:
            xlist[z] = z
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['fillnumbers']=xlist.values()
        return ylist
