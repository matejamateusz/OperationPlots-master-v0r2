__author__ = 'mmateja'

from LoadFiles.LoadDataFromFiles import LoadDataFromFiles
class Retriever:

    def __init__(self,basic_path,nameFileEnd,startfillnumber=0, endfillnumber=None):
        self.basic_path= basic_path
        self.nameFileEnd=nameFileEnd
        self.startfillnumber=startfillnumber
        self.endfillnumber=endfillnumber


    def retrieve(self,nameDataType):

        loader=LoadDataFromFiles(self.basic_path, self.nameFileEnd, self.startfillnumber, self.endfillnumber)
        loader.load(self.basic_path+"Fillnumbers.txt",nameDataType)
        dataObject=loader.getData()
        return dataObject