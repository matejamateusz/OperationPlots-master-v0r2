from  Plot import Plot

from LoadFiles.LoadFiles import LoadFiles
from LoadFiles.LoadDataFromFiles import LoadDataFromFiles
from PLOT.PLOT import PLOT
class PlotCondition(Plot):


    def __init__(self,x,y,basic_path,nameFileEnd, startfillnumber, endfillnumber):
        Plot.__init__(self,x,y)

        loader=LoadDataFromFiles(basic_path, nameFileEnd, startfillnumber, endfillnumber)
        loader.load(basic_path+"Fillnumbers.txt","Condition")
        dataObject=loader.getData()

        self.datax=eval("dataObject.get"+x+"()")
        self.datay=eval("dataObject.get"+y+"()")

    def getData(self):
        return  self.datax,self.datay


