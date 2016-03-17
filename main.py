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

    def set_andres_queue(self):
        """Update andres queue on sheet"""
        andres_queue = get_andres_queue()
        send_to_sheet(self.cellForAndresQueue, andres_queue)
        print 'Updated andres queue on sheet with ' + str(andres_queue)

    def set_andres_resolved(self):
        """Update andres resolved cases of the the month on sheet"""
        andres_resolved = get_andres_resolved()
        send_to_sheet(self.cellForAndresResolved, andres_resolved)
        print 'Updated andres resolved cases of the day on sheet with ' + str(andres_resolved)

    def set_oscar_queue(self):
        """Update oscar queue on sheet"""
        oscar_queue = get_oscar_queue()
        send_to_sheet(self.cellForOscarQueue, oscar_queue)
        print 'Updated oscar queue on sheet with ' + str(oscar_queue)

    def set_oscar_resolved(self):
        """Update oscar resolved cases of the the month on sheet"""
        oscar_resolved = get_oscar_resolved()
        send_to_sheet(self.cellForOscarResolved, oscar_resolved)
        print 'Updated oscar resolved cases of the day on sheet with ' + str(oscar_resolved)

    def set_jaysen_queue(self):
        """Update jaysen queue on sheet"""
        jaysen_queue = get_jaysen_queue()
        send_to_sheet(self.cellForJaysenQueue, jaysen_queue)
        print 'Updated jaysen queue on sheet with ' + str(jaysen_queue)

    def set_jaysen_resolved(self):
        """Update jaysen resolved cases of the the month on sheet"""
        jaysen_resolved = get_jaysen_resolved()
        send_to_sheet(self.cellForJaysenResolved, jaysen_resolved)
        print 'Updated jaysen resolved cases of the day on sheet with ' + str(jaysen_resolved)

    def set_boon_queue(self):
        """Update boon queue on sheet"""
        boon_queue = get_boon_queue()
        send_to_sheet(self.cellForBoonQueue, boon_queue)
        print 'Updated boon queue on sheet with ' + str(boon_queue)

    def set_boon_resolved(self):
        """Update boon resolved cases of the the month on sheet"""
        boon_resolved = get_boon_resolved()
        send_to_sheet(self.cellForBoonResolved, boon_resolved)
        print 'Updated boon resolved cases of the day on sheet with ' + str(boon_resolved)

    def set_cg_queue(self):
        """Update cg queue on sheet"""
        cg_queue = get_cg_queue()
        send_to_sheet(self.cellForCGQueue, cg_queue)
        print 'Updated cg queue on sheet with ' + str(cg_queue)

    def set_cg_resolved(self, Desk):
        """Update cg resolved cases of the the month on sheet"""
        cg_resolved = get_cg_resolved()
        send_to_sheet(self.cellForCGResolved, cg_resolved)
        print 'Updated cg resolved cases of the day on sheet with ' + str(cg_resolved)

    def set_mike_queue(self, Desk):
        """Update Mike queue on sheet"""
        mike_queue = get_mike_queue()
        send_to_sheet(self.cellForMikeQueue, mike_queue)
        print 'Updated mike queue on sheet with ' + str(mike_queue)

    def set_mike_resolved(self):
        """Update mike resolved cases of the the month on sheet"""
        mike_resolved = get_mike_resolved()
        send_to_sheet(self.cellForMikeResolved, mike_resolved)
        print 'Updated mike resolved cases of the day on sheet with ' + str(mike_resolved)

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
sheet.set_andres_queue()
sheet.set_andres_resolved()
sheet.set_oscar_queue()
sheet.set_oscar_resolved()
sheet.set_jaysen_queue()
sheet.set_jaysen_resolved()
sheet.set_boon_queue()
sheet.set_boon_resolved()
sheet.set_cg_queue()
sheet.set_cg_resolved()
sheet.set_mike_queue()
sheet.set_mike_resolved()
