from collections import defaultdict
import numpy as np

def Loadfillnumber(path):
    fillnumber = np.loadtxt(path).tolist()
    return fillnumber
fillnumber = Loadfillnumber('Fillnumbers.txt') #/group/online/tfc/ROOT/Fillnumbers.txt

d = defaultdict(dict)

for num in fillnumber:
     path = "%d/%d_lumi_LHCb.txt" %(num, num)   #/group/online/tfc/LPCfiles/%d/%d_lumi_LHCb.txt
     print path
     print fillnumber
     for line in open(path):
         (time_sec, stablebeams_flag, lumi, lumi_err, lumi_spec, lumi_spec_err) = line.split()
         d['time_sec'] = time_sec
         t0 = d['time_sec'].values()[0]
         print t0
        #d['time_hour'].append((time_sec-t0)/3600)
        # d['stablebeams_flag'].append(stablebeams_flag)
        # d['lumi'].append(lumi)
        # d['lumi_err'].append(lumi_err)
        # d['lumi_spec'].append(lumi_spec)
        # d['lumi_spec_err'].append(lumi_spec_err)


    # plot=PLOT(d['time_sec'], d['lumi'])
         #plot.draw()
   #  d.clear()
    # plot.show()