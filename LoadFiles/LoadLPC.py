from __builtin__ import dict

__author__ = 'mmateja'

from LoadFillNumbers import LoadFillNumbers
from IO.LPCData import LPCData
import numpy as np
class LoadLPC():

    def __init__(self, fillNumbers, basic_path, nameFileEnd):

        self.fillNumbers=fillNumbers
        self.data=LPCData()
        self.basic_path = basic_path
        self.nameFileEnd = nameFileEnd

    def load(self):
        fillnumber = self.fillNumbers.getFillNumbers()
        
        self.data.takeFillNumbers(fillnumber)
        for z in range(0, self.fillNumbers.getNumberOfFillNumbers()):

            # Create the proper path
            path = self.basic_path.replace('ROOT', 'LPCfiles') + "%d/%d_%s.txt" %(fillnumber[z], fillnumber[z], self.nameFileEnd)
            
            # Get the content of the data
            if self.nameFileEnd is 'lumireg_LHCb':
                try:
                    d=np.genfromtxt(path, dtype=None, names=['time_sec','stablebeams_flag','xmean','dx','ymean','dy','zmean','dz','xsigma','dxsigma','ysigma','dysigma','zsigma','dzsigma','xangle','dxangle','yangle','dyangle'], delimiter='').T
                except TypeError:
                    pass
                except IOError:
                    #d=np.empty
                    pass
                except ValueError:
                    pass
            elif self.nameFileEnd is 'beam1_LHCb' or self.nameFileEnd is 'beam2_LHCb':
                try:
                    d=np.genfromtxt(path, dtype=None, names=['time_sec','stablebeams_flag','xmean','dx','ymean','dy','xangle','dxangle','yangle','dyangle','xsigma','dxsigma','ysigma','dysigma'], delimiter=' ').T

                except TypeError:
                    pass
                except IOError:
                    #d=np.empty
                    pass
                except ValueError:
                    pass
            elif self.nameFileEnd is 'lumi_LHCb':
                try:
                    d=np.genfromtxt(path, dtype=None, names=['time_sec','stablebeams_flag','lumi','lumi_err','lumispec','lumispec_err'], delimiter=' ').T

                except TypeError:
                    pass
                except IOError:
                    #d=np.empty
                    pass
            #self.data.load(path, d)
            self.data.load(fillnumber[z], d)



