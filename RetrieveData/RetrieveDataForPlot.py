__author__ = 'mmateja'


class RetrieveDataForPlot:

    def __init__(self,dataObject):
        self.dataObject=dataObject

    def retrieveData(self,xaxis,yaxis):
        self.datax=eval("self.dataObject.get"+xaxis+"()")
        if 'condition' in yaxis:
            self.datay=eval("self.dataObject.get"+yaxis+"()")
        else:
            y_field = yaxis.split('_')
            self.datay=eval("self.dataObject.get"+y_field[0]+"('"+y_field[2]+"')")

        return  self.datax,self.datay

