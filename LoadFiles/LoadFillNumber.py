__author__ = 'mmateja'
import numpy as np

class LoadFillNumbers():

    def __init__(self,pathOfFillNumbersFile, startfillnumber, endfillnumber):
        #self.fillnumber = np.loadtxt(pathOfFillNumbersFile, ndmin=1) #ndmin in case of one fillnumber, numpy>1.9.0
        self.fillnumber = np.loadtxt(pathOfFillNumbersFile) 
        # if self.fillnumber.size == 1:
        #     self.fillnumber = np.array([self.fillnumber])
        start = startfillnumber
        end = endfillnumber
        rangelist = np.arange(start, end+1, dtype=float)
        rangedfillnumbers = list(set(rangelist) & set(self.fillnumber))
        rangedfillnumbers = np.asarray(rangedfillnumbers, dtype=float)
        rangedfillnumbers = np.sort(rangedfillnumbers)
        self.fillnumber = rangedfillnumbers

    def getFillNumbers(self):
        return self.fillnumber

    def getNumberOfFillNumbers(self):
        return self.fillnumber.size
