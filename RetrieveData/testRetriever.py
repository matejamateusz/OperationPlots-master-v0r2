from PLOT.PLOT import PLOT
from RetrieveData.RetrieveDataForPlot import RetrieveDataForPlot
from RetrieveData.Retriever import Retriever

__author__ = 'mmateja'
basic_path = "/home/mmateja/PycharmProjects/OperationPlots/"
#nameFileEnd = "Mu"


startfillnumber = 3819
endfillnumber = 4000

d = Retriever( basic_path, "lumi_LHCb", startfillnumber, endfillnumber)
data = d.retrieve("LPC") #LPC, CONDITION
r = RetrieveDataForPlot(data)
datax,datay=r.retrieveData("fillnumber","max_lumi")
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot=PLOT(value1, value2)
        plot.setTitle("LHCb Peak Instantaneous Lumi at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Inst Luminosity (10^24/cm^2*s^1)")
        plot.draw()
datax,datay=r.retrieveData("fillnumber","average_lumi")
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot=PLOT(value1, value2)
        plot.setTitle("LHCb Peak Instantaneous Lumi at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Inst Luminosity (10^24/cm^2*s^1)")
        plot.draw()
        #plot.savefig("OUTPUTPLOTS/2015PeakLumiFill.png")
plot.show()