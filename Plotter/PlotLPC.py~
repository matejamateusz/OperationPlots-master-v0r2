__author__ = 'mmateja'

from  Plot import Plot

from LoadFiles.LoadFiles import LoadFiles
from LoadFiles.LoadDataFromFiles import LoadDataFromFiles
from PLOT.PLOT import PLOT
class PlotLPC(Plot):


    def __init__(self,x,y,basic_path,nameFileEnd, startfillnumber, endfillnumber):
        Plot.__init__(self,x,y)

        loader=LoadDataFromFiles(basic_path, nameFileEnd, startfillnumber, endfillnumber)
        loader.load(basic_path+"Fillnumbers.txt","LPC")
        dataObject=loader.getData()
        y_field = y.split('_')
        self.datax=eval("dataObject.get"+x+"()")
        self.datay=eval("dataObject.get"+y_field[0]+"('"+y_field[2]+"')")

    def getData(self):
        return  self.datax,self.datay


