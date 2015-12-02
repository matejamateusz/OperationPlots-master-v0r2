# OperationalPlots-master-v0r3 Python script by Mateusz Jan Mateja

##TEMPLATE PLOTTING
Here is shown the template plotting with example values of variables for Condition data structure
basic_path = "/group/online/tfc/ROOT/"

startfillnumber = 3819 #number of fillnumber from which starts retrieving data
endfillnumber = 5000 #number of fillnumber to which ends retrieving data

print 'Retrieving data from Mu between fill# ' + str(startfillnumber) + ' and fill# ' + str(endfillnumber)
d = Retriever( basic_path, "Mu", startfillnumber, endfillnumber)
mu = d.retrieve("Condition") #LPC, CONDITION
r = RetrieveDataForPlot(mu)

xaxis = "fillnumber"  #options: TIME_DATE, FILLNUMBER
yaxis = "max_condition" #options: MAX_CONDITION, AVERAGE_CONDITION
print 'Doing ' + yaxis + ' vs ' + xaxis
datax,datay = r.retrieveData(xaxis,yaxis)
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()):
    if "time_date" in xaxis and yaxis:
        value1 = dateformat(value1)
        plot = PLOT()
        plot.setDate()
        plot.setTitle("LHCb Peak Mu at p-p 6.5 TeV in 2015")
        plot.setxlabel("Date")
        plot.setylabel("Peak Mu")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakMuTime.png")
    else:
        plot = PLOT()
        plot.setTitle("LHCb Peak Mu at p-p 6.5 TeV in 2015")
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Mu")
        plot.draw(value1, value2, 'b', 6)
        plot.savefig("OUTPUTPLOTS/2015PeakMuFill.png")