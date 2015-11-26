import base64
import json
import urllib2
import sys
import time
import datetime
from datetime import date


def firstDayOfMonth(d):
    return str(date(d.year, d.month, 1))


def dateToTimestamp(d):
    return int(time.mktime(datetime.datetime.strptime(d, "%Y-%m-%d").timetuple()))


def getFromAPI(query):
    try:
        # Generate call from API
        baseURL = 'https://servicerocket.desk.com/api/v2/cases/search?q='
        APIcall = baseURL + query
        request = urllib2.Request(APIcall)
        username = ''
        password = ''
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        json_obj = urllib2.urlopen(request)
        data = json.load(json_obj)
        return data['total_entries']
    except:
        sys.exit('Error getting data from Desk. Check if username and password are correct')


def getUnassignedCases():
    # Get the amount of Unassigned cases
    query = 'assigned:NONE%20group:Learndot%20status:new,open,pending'
    UnassignedCases = getFromAPI(query)
    return UnassignedCases


def getWatingOnCustomerCases():
    # Get the amout of Waiting on Customer cases
    query = 'group:Learndot%20status:new,open,pending%20custom_status:%22Waiting%20on%20Customer%22'
    WatingOnCustomer = getFromAPI(query)
    return WatingOnCustomer


def getAssignedToDevCases():
    # Get the amout of Assigned To Dev cases
    query = 'group:Learndot%20status:pending%20custom_status:%22Assigned%20to%20DEV%22'
    AssignedToDev = getFromAPI(query)
    return AssignedToDev


def getAssginedToCSMCases():
    # Get the amout of Assigned To CSM
    query = 'group:Learndot%20status:new,open,pending%20custom_status:%22Assigned%20to%20CSM%22'
    AssignedToCSM = getFromAPI(query)
    return AssignedToCSM


def getAgginedToSupport():
    # Get the amout of Assigned To Support
    query = 'group:Learndot%20status:open,new,pending%20custom_status:%22Assigned%20to%20Support%22'
    AssignedToSupport = getFromAPI(query)
    return AssignedToSupport


def getOpenCases():
    # Get the amout of Open
    query = 'group:Learndot%20status:new,open,pending%20custom_status:Open'
    Open = getFromAPI(query)
    return Open


def getCloseCases():
    # Get the amout of Close
    query = 'group:Learndot%20status:new,open,pending%20custom_status:Close'
    Open = getFromAPI(query)
    return Open


def getResolvedCasesOfMonth():
    # Get resolved cases of current month
    query = 'group:Learndot%20%28ticket_customer.updated_at:%5B' + str(firstDay) + '%20TO%20' + str(today) + '%5D%29%20status:resolved'
    print query
    ResolvedCases = getFromAPI(query)
    return ResolvedCases


def getCreatedCasesOfMonth():
    # Get created cases of current month
    query = 'group:Learndot%20%28ticket_customer.created_at:%5B' + str(firstDay) + '%20TO%20' + str(today) + '%5D%29'
    CreatedCases = getFromAPI(query)
    return CreatedCases


def getCreatedCasesOfToday():
    # Get created cases of today
    query = 'group:Learndot%20created:today'
    CreatedCases = getFromAPI(query)
    return CreatedCases


def getResolvedCasesOfToday():
    # Get resolved cases of today
    query = 'group:Learndot%20updated:today%20status:resolved'
    ResolvedCases = getFromAPI(query)
    return ResolvedCases


def getCreatedCasesOfLastThreeMonth():
    # Get crested cases of the last three months
    dateRanges = getRangeOfLastThreeMonth()
    results = []
    for x in dateRanges:
        firstRange = int(x[0])
        secondRange = int(x[1])
        query = 'group:Learndot%20(ticket_customer.created_at:%5B' + str(firstRange) + '%20TO%20' + str(secondRange) + '%5D)%20label:%22%21Spam%22'
        createdCasesInRange = getFromAPI(query)
        results.append(createdCasesInRange)
    return results


def getResolvedCasesOfLastThreeMonth():
    # Get Resolved cases of the last three months
    dateRanges = getRangeOfLastThreeMonth()
    results = []
    for x in dateRanges:
        firstRange = int(x[0])
        secondRange = int(x[1])
        query = 'group:Learndot%20(ticket_customer.updated_at:%5B' + str(firstRange) + '%20TO%20' + str(secondRange) + '%5D)%20status:resolved,closed%20label:%22%21Spam%22'
        resolvedCasesinRange = getFromAPI(query)
        results.append(resolvedCasesinRange)
    return results


def getAndresQueue():
    # Get queue of Andres
    query = 'assigned:%22Andres%20Hazard%22%20status:open,new,pending%20custom_status:%22Open,Assigned%20to%20Support,Assigned%20to%20CSM,Waiting%20on%20Customer,Customer%20Review,Closed%22'
    andresQueue = getFromAPI(query)
    return andresQueue


def getAndresResolved():
    # Get the resolved cases of the day by Andres
    # query = 'assigned:%22Andres%20Hazard%22%20%28ticket_customer.created_at:%5B' + str(firstDay) + '%20TO%20' + str(today) + '%5D%29%20status:resolved'
    query = 'assigned:%22Andres%20Hazard%22%20updated:today%20status:resolved'
    andresResolved = getFromAPI(query)
    return andresResolved


def getOscarQueue():
    # Get queue of Oscar
    query = 'assigned:%22Oscar%20Rivas%22%20status:open,new,pending%20custom_status:%22Open,Assigned%20to%20Support,Assigned%20to%20CSM,Waiting%20on%20Customer,Customer%20Review,Closed%22'
    oscarQueue = getFromAPI(query)
    return oscarQueue


def getOscarResolved():
    # Get the resolved cases of the day by Oscar
    # query = 'assigned:%22Oscar%20Rivas%22%20%28ticket_customer.created_at:%5B' + str(firstDay) + '%20TO%20' + str(today) + '%5D%29%20status:resolved'
    query = 'assigned:%22Oscar%20Rivas%22%20updated:today%20status:resolved'
    oscarResolved = getFromAPI(query)
    return oscarResolved


def getJaimeQueue():
    # Get queue of Jaime
    query = 'assigned:%22Jaime%20Cornejo%22%20status:open,new,pending%20custom_status:%22Open,Assigned%20to%20Support,Assigned%20to%20CSM,Waiting%20on%20Customer,Customer%20Review,Closed%22'
    jaimeQueue = getFromAPI(query)
    return jaimeQueue


def getJaimeResolved():
    # Get the resolved cases of the day by Jaime
    # query = 'assigned:%22Jaime%20Cornejo%22%20%28ticket_customer.created_at:%5B' + str(firstDay) + '%20TO%20' + str(today) + '%5D%29%20status:resolved'
    query = 'assigned:%22Jaime%20Cornejo%22%20updated:today%20status:resolved'
    jaimeResolved = getFromAPI(query)
    return jaimeResolved


def getBoonQueue():
    # Get queue of Boon
    query = 'assigned:%22Yik%20Boon%20Tan%22%20status:open,new,pending%20custom_status:%22Open,Assigned%20to%20Support,Assigned%20to%20CSM,Waiting%20on%20Customer,Customer%20Review,Closed%22'
    boonQueue = getFromAPI(query)
    return boonQueue


def getBoonResolved():
    # Get the resolved cases of the day by Boon
    # query = 'assigned:%22Yik%20Boon%20Tan%22%20%28ticket_customer.created_at:%5B' + str(firstDay) + '%20TO%20' + str(today) + '%5D%29%20status:resolved'
    query = 'assigned:%22Yik%20Boon%20Tan%22%20updated:today%20status:resolved'
    boonResolved = getFromAPI(query)
    return boonResolved


def getCGQueue():
    # Get queue of CG
    query = 'assigned:%22Goh%20Chooi%20Gaik%22%20status:open,new,pending%20custom_status:%22Open,Assigned%20to%20Support,Assigned%20to%20CSM,Waiting%20on%20Customer,Customer%20Review,Closed%22'
    cgQueue = getFromAPI(query)
    return cgQueue


def getCGResolved():
    # Get the resolved cases of the day by CG
    # query = 'assigned:%22Goh%20Chooi%20Gaik%22%20%28ticket_customer.created_at:%5B' + str(firstDay) + '%20TO%20' + str(today) + '%5D%29%20status:resolved'
    query = 'assigned:%22Goh%20Chooi%20Gaik%22%20updated:today%20status:resolved'
    cgResolved = getFromAPI(query)
    return cgResolved


def getMikeQueue():
    # Get queue of Mike
    query = 'assigned:%22Mike%20Dawson%22%20status:open,new,pending%20custom_status:%22Open,Assigned%20to%20Support,Assigned%20to%20CSM,Waiting%20on%20Customer,Customer%20Review,Closed%22'
    mikeQueue = getFromAPI(query)
    return mikeQueue


def getMikeResolved():
    # Get the resolved cases of the day by CG
    # query = 'assigned:%22Mike%20Dawson%22%20%28ticket_customer.created_at:%5B' + str(firstDay) + '%20TO%20' + str(today) + '%5D%29%20status:resolved'
    query = 'assigned:%22Mike%20Dawson%22%20updated:today%20status:resolved'
    mikeResolved = getFromAPI(query)
    return mikeResolved


firstDay = dateToTimestamp(firstDayOfMonth(date.today()))
today = dateToTimestamp(str(date.today()))
