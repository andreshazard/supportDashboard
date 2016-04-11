import base64
import json
import urllib2
import sys
import time
import datetime
from datetime import date


def first_day_of_month(d):
    return str(date(d.year, d.month, 1))


def date_to_time_stamp(d):
    return int(time.mktime(datetime.datetime.strptime(d, "%Y-%m-%d").timetuple()))


def get_from_api(query):
    try:
        # Generate call from API
        base_url = 'https://servicerocket.desk.com/api/v2/cases/search?q='
        api_call = base_url + query
        request = urllib2.Request(api_call)
        username = 'andres.hazard@servicerocket.com'
        password = 'Desk123456'
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        json_obj = urllib2.urlopen(request)
        data = json.load(json_obj)
        return data['total_entries']
    except:
        sys.exit('Error getting data from Desk. Check if username and password are correct')


def get_unassigned_cases():
    # Get the amount of Unassigned cases
    query = 'assigned:NONE%20group:Learndot%20status:new,open,pending'
    unassigned_cases = get_from_api(query)
    return unassigned_cases


def get_waiting_on_customer_cases():
    # Get the amount of Waiting on Customer cases
    query = 'group:Learndot%20status:new,open,pending%20custom_status:%22Waiting%20on%20Customer%22'
    waiting_on_customer = get_from_api(query)
    return waiting_on_customer


def get_assigned_to_dev_cases():
    # Get the amount of Assigned To Dev cases
    query = 'group:Learndot%20status:pending%20custom_status:%22Assigned%20to%20DEV%22'
    assigned_to_dev = get_from_api(query)
    return assigned_to_dev


def get_assigned_to_csm_cases():
    # Get the amount of Assigned To CSM
    query = 'group:Learndot%20status:new,open,pending%20custom_status:%22Assigned%20to%20CSM%22'
    assigned_to_csm = get_from_api(query)
    return assigned_to_csm


def get_assigned_to_support():
    # Get the amout of Assigned To Support
    query = 'group:Learndot%20status:open,new,pending%20custom_status:%22Assigned%20to%20Support%22'
    assigned_to_support = get_from_api(query)
    return assigned_to_support


def get_open_cases():
    # Get the amout of Open
    query = 'group:Learndot%20status:new,open,pending%20custom_status:Open'
    open_cases = get_from_api(query)
    return open_cases


def get_close_cases():
    # Get the amout of Close
    query = 'group:Learndot%20status:new,open,pending%20custom_status:Close'
    open_cases = get_from_api(query)
    return open_cases


def get_resolved_cases_of_month():
    # Get resolved cases of current month
    query = 'group:Learndot%20%28ticket_customer.updated_at:%5B' + str(firstDay) + '%20TO%20' + str(
        today) + '%5D%29%20status:resolved'
    resolved_cases = get_from_api(query)
    return resolved_cases


def get_created_cases_of_month():
    # Get created cases of current month
    query = 'group:Learndot%20%28ticket_customer.created_at:%5B' + str(firstDay) + '%20TO%20' + str(today) + '%5D%29'
    created_cases = get_from_api(query)
    return created_cases


def get_created_cases_of_today():
    # Get created cases of today
    query = 'group:Learndot%20created:today'
    created_cases = get_from_api(query)
    return created_cases


def get_resolved_cases_of_today():
    # Get resolved cases of today
    query = 'group:Learndot%20updated:today%20status:resolved'
    resolved_cases = get_from_api(query)
    return resolved_cases


def get_query_of_engineer_two_names(name, last_name):
    # Get query of engineer with two names
    query = 'assigned:%22' + name + '%20' + last_name + '%22%20status:open,new,pending%20custom_status:%22Open,' \
            'Assigned%20to%20Support,Assigned%20to%20CSM,Waiting%20on%20Customer,Customer%20Review,Closed%22'
    engineer_query = get_from_api(query)
    return engineer_query


def get_query_of_engineer_three_names(name, second_name, last_name):
    # Get query of engineer with three names
    query = 'assigned:%22' + name + '%20' + second_name + '%20' + last_name + '%22%20status:open,new,pending%20custom_status:%22Open,' \
            'Assigned%20to%20Support,Assigned%20to%20CSM,Waiting%20on%20Customer,Customer%20Review,Closed%22'
    engineer_queue = get_from_api(query)
    return engineer_queue


def get_resolved_of_engineer_two_names(name, last_name):
    query = 'assigned:%22' + name + '%20' + last_name + '%22%20updated:today%20status:resolved'
    engineer_resolved = get_from_api(query)
    return engineer_resolved


def get_resolved_of_engineer_three_names(name, second_name, last_name):
    query = 'assigned:%22' + name + '%20' + second_name + '%20' + last_name + '%22%20updated:today%20status:resolved'
    engineer_resolved = get_from_api(query)
    return engineer_resolved


firstDay = date_to_time_stamp(first_day_of_month(date.today()))
today = date_to_time_stamp(str(date.today()))
