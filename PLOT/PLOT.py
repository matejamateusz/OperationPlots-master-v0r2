__author__ = 'mmateja'
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.dates as mdates
from datetime import datetime
from datetime import datetime
import pytz # $ pip install pytz
import tzlocal # $ pip install tzlocal
#  FOR ALL PLATFORMS to get access to the tz database on all platforms
# and compute the correct "seconds since the Epoch" (POSIX timestamp) corresponding to the input time tuples:
import numpy as np


def dateformat(value1):
        value1 = [datetime.fromtimestamp(v1) for v1 in value1]
        return value1

def transformtotimestamp(dict):
        local_timezone = tzlocal.get_localzone() # pytz tzinfo representing local time
        epoch = datetime(1970, 1, 1, tzinfo=pytz.utc)
	list_utc_timestamp = []
	for tt in dict['time_date']:
		delta = (local_timezone.localize(datetime(*tt), is_dst=None) - epoch)
		utc_timestamp = delta.seconds + delta.days*24*3600
		list_utc_timestamp.append(utc_timestamp)
        dict['time_date'] = list_utc_timestamp
        return dict

# def transformtotimestamp(xdict):
#     return {"time": map(lambda k: time.mktime(datetime.datetime(*k).timetuple()), xdict["time"])}

class PLOT:
    def __init__(self):
        #self.x = x#.astype(datetime)
        #self.y = y
        self.figure = plt.figure()

        self.ax = plt.subplot(111)
        self.ax.fmt_xdata = mdates.DateFormatter('%d/%m')
        #self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

        #self.figure.suptitle("LHCB")
        self.xlabel = "TITLE OF XLABEL"
        self.ylabel = 'TITLE OF YLABEL'

        self.y_min = 0
        self.y_max = 1

        self.color = 'b'
        self.markersize = 7
        self.linestyle = 'None'
        self.marker = Line2D.filled_markers[0]
        plt.grid()


	
    def show(self):
        plt.show()

    def draw(self, x, y, *args):
        #plt.xticks(rotation=45)# horizontalalignment='right')
        #print len(self.x), len(self.y)
        plt.plot(x, y, marker=self.marker, linestyle=self.linestyle, color=args[0],
                 markersize=args[1])
        #plt.tight_layout()

    def sety_limits(self, y_min, y_max):
        self.y_min = y_min
        self.y_max = y_max
        plt.ylim(self.y_min, self.y_max)

    def setTitle(self, title):
        self.setTitle=title
        self.figure.suptitle(self.setTitle)

    def setDate(self):
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
        plt.xticks(rotation=0)# horizontalalignment='right')

    def setxlabel(self, xlabel):
        self.xlabel = xlabel
        plt.xlabel(self.xlabel)

    def setylabel(self, ylabel):
        self.ylabel = ylabel
        plt.ylabel(self.ylabel)

    def disableGrid(self):
        plt.grid(False)

    def setShape(self, shape):
        self.style[1] = shape

    def setMarkerSize(self, size):
        self.markersize = size

    def setColor(self, color):
        self.color = color

    def setMarkerType(self, numberOfMarker):
        self.marker = Line2D.filled_markers[numberOfMarker]

    def setlineStyle(self, style):
        self.linestyle = style

    def savefig(self, nameoffile):
        plt.savefig(nameoffile)
