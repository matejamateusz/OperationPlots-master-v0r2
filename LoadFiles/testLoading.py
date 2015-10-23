
__author__ = 'mmateja'


from LoadDataFromFiles import LoadDataFromFiles

loader=LoadDataFromFiles()
loader.load("/home/mmateja/PycharmProjects/OperationPlots/Fillnumbers.txt","lumi")
a=loader.getData()
v=a.data['/home/mmateja/PycharmProjects/OperationPlots/3819/3819_lumi_LHCb.txt']
print v[0]

