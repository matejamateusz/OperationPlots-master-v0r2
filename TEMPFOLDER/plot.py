# __author__ = 'mmateja'
#
# import numpy as np
#
# data={}
# data['date']=np.arange('2005-02', '2005-03', dtype='datetime64[D]')
# print data['date'][1]
# data['lumi']=np.random.rand(data['date'].size)
#
# #from PLOT import PLOT, Loadfillnumber
#
#
#
#
# #f = open('Fillnumbers.txt', 'r')
# #print f.read()
#
#
# num_files, fillnumber = Loadfillnumber('Fillnumbers.txt') #/group/online/tfc/ROOT/Fillnumbers.txt
#
# print fillnumber, num_files
#
# time_of_run = []
# max_lumi_per_fill = []
#
#
# storage_files = {}
#
# #Getting luminosities from LPC files
# for z in range(0, num_files):  #1 +1
#     path = "%d/%d_lumi_LHCb.txt" %(fillnumber[z], fillnumber[z])   #/group/online/tfc/LPCfiles/%d/%d_lumi_LHCb.txt
#     print path
#     storage_files[path]=np.loadtxt(path, delimiter=' ').T #OPEN(path)
#     print storage_files
#
#
#
#     storage_files[path]=np.loadtxt('', delimiter=' ') #OPEN(path)
#
# v=storage_files.itervalues() #dictionary for stored values
# for fileLUMI in v:
#     print fileLUMI
#
#
#
# raw_input("Press enter to continue")