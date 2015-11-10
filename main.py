from apiCalls import  *
import time
from pylab import *
import matplotlib

def getPieChart(WaCu, AsDe, AsCM, AsSu):
# make a square figure and axes
    figure('Statuses', figsize=(10,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
# The slices will be ordered and plotted counter-clockwise.
    labels = 'Waiting On Customer', 'Assigned to Dev', 'Assigned to CSM', 'Assigned to Support'
    fracs = [WaCu, AsDe, AsCM, AsSu]
    explode=(0, 0.05, 0, 0)
    colors = ['lightgreen', 'lightskyblue', 'orange', 'yellow']
    pie(fracs, explode=explode, labels=labels,
                    autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)
                    # The default startangle is 0, which would start
                    # the Frogs slice on the x-axis.  With startangle=90,
                    # everything is rotated counter-clockwise by 90 degrees,
                    # so the plotting starts on the positive y-axis.
    title('Tickets Statuses')
    show()




def getOpenVsResolved():
    import numpy as np
    import matplotlib.pyplot as plt
    import calendar
    import time
    import datetime
    now = datetime.date.today()
    N = 3
    casesOpen = getCreatedCasesOfLastThreeMonth()
    menStd = (2, 3, 4)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, casesOpen, width, color='b', yerr=menStd)
    casesResolved = getResolvedCasesOfLastThreeMonth()
    womenStd = (3, 5, 2)
    rects2 = ax.bar(ind + width, casesResolved, width, color='g', yerr=womenStd)
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Tickets')
    ax.set_title('Open VS Resolved')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((calendar.month_name[now.month - 1], calendar.month_name[now.month - 2], calendar.month_name[now.month - 3]))
    ax.legend((rects1[0], rects2[0]), ('Open', 'Resolved'))


    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    plt.show()


def getActiveCasesChart(number):
    from Tkinter import *
    AcCa = WaCu + AsCM + AsSu + Op + Cl
    root = Tk()
    Label(root,
            text=("***Active Cases***: " + str(AcCa)),
                 fg = "light green",
                 bg = "black",
                 font = "Helvetica 76 bold italic").pack()
    Label(root,
            text=("Goal of the week :  " + str(number)),
                 fg = "light green",
                 bg = "black",
                 font = "Helvetica 76 bold italic").pack()


def getUnassignedCasesChart():
    from Tkinter import *
    root = Tk()
    Label(root,
            text=("***Unassigned Cases***: " + str(getUnassignedCases())),
                 fg = "light green",
                 bg = "black",
                 font = "Helvetica 76 bold italic").pack()


WaCu = getWatingOnCustomerCases()
AsDe = getAssignedToDevCases()
AsCM = getAssginedToCSMCases()
AsSu = getAgginedToSupport()
Op   = getOpenCases()
Cl    = getCloseCases()
getPieChart(WaCu, AsDe, AsCM, AsSu)
getOpenVsResolved()
getActiveCasesChart(80)
getUnassignedCasesChart()
