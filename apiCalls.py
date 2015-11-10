import base64
import json
import urllib2
from testingMonthDates import *


def getFromAPI(query):
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


def getUnassignedCases():
    # Get the ammount of Unassigned cases
    query = 'assigned:NONE%20group:Learndot%20status:new,open,pending'
    UnassignedCases = getFromAPI(query)
    return UnassignedCases


def getWatingOnCustomerCases():
    # Get the ammout of Waiting on Customer cases
    query = 'group:Learndot%20status:new,open,pending%20custom_status:%22Waiting%20on%20Customer%22'
    WatingOnCustomer = getFromAPI(query)
    return WatingOnCustomer


def getAssignedToDevCases():
    # Get the ammout of Assigned To Dev cases
    query = 'group:Learndot%20status:new,open,pending%20custom_status:%22Assigned%20to%20DEV%22'
    AssignedToDev = getFromAPI(query)
    return AssignedToDev


def getAssginedToCSMCases():
    # Get the ammout of Assigned To CSM
    query = 'group:Learndot%20status:new,open,pending%20custom_status:%22Assigned%20to%20CSM%22'
    AssignedToCSM = getFromAPI(query)
    return AssignedToCSM


def getAgginedToSupport():
    # Get the ammout of Assigned To Support
    query = 'group:Learndot%20status:open,new,pending%20custom_status:%22Assigned%20to%20Support%22'
    AssignedToSupport = getFromAPI(query)
    return AssignedToSupport


def getOpenCases():
    # Get the ammout of Open
    query = 'group:Learndot%20status:new,open,pending%20custom_status:Open'
    Open = getFromAPI(query)
    return Open


def getCloseCases():
    # Get the ammout of Open
    query = 'group:Learndot%20status:new,open,pending%20custom_status:Close'
    Open = getFromAPI(query)
    return Open


def getResolvedCasesOfMonth():
    # Get resolved cases of current month
    query = 'group:Learndot%20updated:month%20status:resolved%20label:%22%21Spam%22'
    ResolvedCases = getFromAPI(query)
    return ResolvedCases


def getCreatedCasesOfMonth():
    # Get created cases of current month
    query = 'group:Learndot%20created:month%20label:%22%21Spam%22'
    CreatedCases = getFromAPI(query)
    return CreatedCases


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
