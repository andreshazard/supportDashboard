#!/usr/bin/python
from apiCalls import *
from sheetConnector import *


class Sheet:
    def __init__(self):
        self.cellForBacklog = 'E2'
        self.cellForUnassigned = 'D2'
        self.cellForOpenThisMonth = 'Q2'
        self.cellForCloseThisMonth = 'R2'
        self.cellForAssignedToDev = 'N2'
        self.cellForWaitingOnCustomer = 'N3'
        self.cellForAssignedToSupport = 'N4'
        self.cellForAssignedToCSM = 'N5'
        self.cellForOpenToday = 'O2'
        self.cellForCloseToday = 'P2'
        self.cellForAndresQueue = 'G8'
        self.cellForAndresResolved = 'G9'
        self.cellForOscarQueue = 'G18'
        self.cellForOscarResolved = 'G19'
        self.cellForRolandoQueue = 'K8'
        self.cellForRolandoResolved = 'K9'
        self.cellForJaysenQueue = 'G13'
        self.cellForJaysenResolved = 'G14'
        self.cellForBoonQueue = 'G23'
        self.cellForBoonResolved = 'G24'
        self.cellForCGQueue = 'G28'
        self.cellForCGResolved = 'G29'
        self.cellForMikeQueue = 'G33'
        self.cellForMikeResolved = 'G34'
        self.WaCu = get_waiting_on_customer_cases()
        self.AsDev = get_assigned_to_dev_cases()
        self.AsCSM = get_assigned_to_csm_cases()
        self.AsSu = get_assigned_to_support()
        self.Op = get_open_cases()
        self.Cl = get_close_cases()

    def set_backlog(self):
        """Update backlog on sheet"""
        backlog = self.WaCu + self.AsCSM + self.AsSu + self.Op + self.Cl
        send_to_sheet(self.cellForBacklog, backlog)
        print 'Updated backlog on data sheet with ' + str(backlog)

    def set_unassigned_cases(self):
        """Update unassign cases on sheet"""
        unassigned = get_unassigned_cases()
        send_to_sheet(self.cellForUnassigned, unassigned)
        print 'Updated unassign cases on sheet with ' + str(unassigned)

    def set_open_this_month(self):
        """Update open cases of the month on sheet"""
        open_this_month = get_created_cases_of_month()
        send_to_sheet(self.cellForOpenThisMonth, open_this_month)
        print 'Updated open cases of the month on sheet with ' + str(open_this_month)

    def set_close_this_month(self):
        """Update close cases of the month on sheet"""
        close_this_month = get_resolved_cases_of_month()
        send_to_sheet(self.cellForCloseThisMonth, close_this_month)
        print 'Updated close cases of the month on sheet with ' + str(close_this_month)

    def set_waiting_on_customer(self):
        """Update waiting on customer cases on sheet"""
        waiting_on_customer = self.WaCu
        send_to_sheet(self.cellForWaitingOnCustomer, waiting_on_customer)
        print 'Updated waiting on customer cases on sheet with ' + str(waiting_on_customer)

    def set_assigned_to_cev(self):
        """Update assigned to dev cases on sheet"""
        assigned_to_dev = self.AsDev
        send_to_sheet(self.cellForAssignedToDev, assigned_to_dev)
        print 'Updated assigned to dev cases on sheet with ' + str(assigned_to_dev)

    def set_assigned_to_support(self):
        """Update assigned to support cases on sheet"""
        assigned_to_support = self.AsSu
        send_to_sheet(self.cellForAssignedToSupport, assigned_to_support)
        print 'Updated assigned to support cases on sheet with ' + str(assigned_to_support)

    def set_assigned_to_csm(self):
        """Update assigned to CSM cases on sheet"""
        assigned_to_csm = self.AsCSM
        send_to_sheet(self.cellForAssignedToCSM, assigned_to_csm)
        print 'Updated assigned to CSM cases on sheet with ' + str(assigned_to_csm)

    def set_open_today(self):
        """Update open cases of today on sheet"""
        open_today = get_created_cases_of_today()
        send_to_sheet(self.cellForOpenToday, open_today)
        print 'Update open cases of today on sheet with ' + str(open_today)

    def set_close_today(self):
        """Update close cases of today on sheet"""
        close_today = get_resolved_cases_of_today()
        send_to_sheet(self.cellForCloseToday, close_today)
        print 'Update close cases of today on sheet with ' + str(close_today)

    def set_engineer_queue_two_names(self, name, last_name, cell_queue):
        """Update engineer queue on sheet"""
        engineer_queue = get_query_of_engineer_two_names(name, last_name)
        send_to_sheet(cell_queue, engineer_queue)
        print 'Updated ' + name + ' queue on sheet with ' + str(engineer_queue)

    def set_engineer_queue_three_names(self, name, second_name, last_name, cell_queue):
        """Update engineer queue on sheet"""
        engineer_queue = get_query_of_engineer_three_names(name, second_name, last_name)
        send_to_sheet(cell_queue, engineer_queue)
        print 'Updated ' + name + ' queue on sheet with ' + str(engineer_queue)

    def set_engineer_resolved_two_names(self, name, last_name, cell_queue):
        """Update engineer resolved on sheet"""
        engineer_resolved = get_resolved_of_engineer_two_names(name, last_name)
        send_to_sheet(cell_queue, engineer_resolved)
        print 'Updated ' + name + ' resolved cases of the day on sheet with ' + str(engineer_resolved)

    def set_engineer_resolved_three_names(self, name, second_name, last_name, cell_queue):
        """Update engineer resolved on sheet"""
        engineer_queue = get_resolved_of_engineer_three_names(name, second_name, last_name)
        send_to_sheet(cell_queue, engineer_queue)
        print 'Updated ' + name + ' resolved on sheet with ' + str(engineer_queue)

print
print 'Starting update at ' + str(time.strftime("%Y-%m-%d %H:%M"))
print
sheet = Sheet()
sheet.set_backlog()
sheet.set_unassigned_cases()
sheet.set_waiting_on_customer()
sheet.set_assigned_to_cev()
sheet.set_assigned_to_support()
sheet.set_assigned_to_csm()
sheet.set_open_today()
sheet.set_close_today()
sheet.set_engineer_queue_two_names('Andres', 'Hazard', sheet.cellForAndresQueue)
sheet.set_engineer_resolved_two_names('Andres', 'Hazard', sheet.cellForAndresResolved)
sheet.set_engineer_queue_two_names('Oscar', 'Rivas', sheet.cellForOscarQueue)
sheet.set_engineer_resolved_two_names('Oscar', 'Rivas', sheet.cellForOscarResolved)
sheet.set_engineer_queue_two_names('Rolando', 'Bergmann', sheet.cellForRolandoQueue)
sheet.set_engineer_resolved_two_names('Rolando', 'Bergmann', sheet.cellForRolandoResolved)
sheet.set_engineer_queue_two_names('Jaysen', 'Lim', sheet.cellForJaysenQueue)
sheet.set_engineer_resolved_two_names('Jaysen', 'Lim', sheet.cellForJaysenResolved)
sheet.set_engineer_queue_three_names('Yik', 'Boon', 'Tan', sheet.cellForBoonQueue)
sheet.set_engineer_resolved_three_names('Yik', 'Boon', 'Tan', sheet.cellForBoonResolved)
sheet.set_engineer_queue_three_names('Goh', 'Chooi', 'Gaik', sheet.cellForCGQueue)
sheet.set_engineer_resolved_three_names('Goh', 'Chooi', 'Gaik', sheet.cellForCGResolved)
sheet.set_engineer_queue_two_names('Mike', 'Dawson', sheet.cellForJaysenQueue)
sheet.set_engineer_resolved_two_names('Mike', 'Dawson', sheet.cellForJaysenResolved)
