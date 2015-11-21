#!/usr/bin/python
from apiCalls import *
from sheetConnector import *


class Desk:
    def __init__(self):
        self.WaCu = getWatingOnCustomerCases()
        self.AsDev = getAssignedToDevCases()
        self.AsCSM = getAssginedToCSMCases()
        self.AsSu = getAgginedToSupport()
        self.Op = getOpenCases()
        self.Cl = getCloseCases()

    def deskBacklog(self):
        backlog = self.WaCu + self.AsCSM + self.AsSu + self.Op + self.Cl
        return backlog

    def deskUnassignedCases(self):
        unassigned = getUnassignedCases()
        return unassigned

    def deskOpenThisMonth(self):
        openThisMonth = getCreatedCasesOfMonth()
        return openThisMonth

    def deskCloseThisMonth(self):
        closeThisMonth = getResolvedCasesOfMonth()
        return closeThisMonth

    def deskOpenToday(self):
        openToday = getCreatedCasesOfToday()
        return openToday

    def deskCloseToday(self):
        closeToday = getResolvedCasesOfToday()
        return closeToday

    def deskAndresQueue(self):
        andresQueue = getAndresQueue()
        return andresQueue

    def deskAndresResolved(self):
        andresResolved = getAndresResolved()
        return andresResolved

    def deskOscarQueue(self):
        oscarQueue = getOscarQueue()
        return oscarQueue

    def deskOscarResolved(self):
        oscarResolved = getOscarResolved()
        return oscarResolved

    def deskJaimeQueue(self):
        jaimeQueue = getJaimeQueue()
        return jaimeQueue

    def deskJaimeResolved(self):
        jaimeResolved = getJaimeResolved()
        return jaimeResolved

    def deskBoonQueue(self):
        boonQueue = getBoonQueue()
        return boonQueue

    def deskBoonResolved(self):
        boonResolved = getBoonResolved()
        return boonResolved

    def deskCGQueue(self):
        cgQueue = getCGQueue()
        return cgQueue

    def deskCGResolved(self):
        cgResolved = getCGResolved()
        return cgResolved


class Sheet:
    def __init__(self):
        self.cellForBacklog = 'E2'
        self.cellForUnassigned = 'D2'
        self.cellForOpenThisMonth = 'Q2'
        self.cellForCloseThisMonth = 'R2'
        self.cellForAssignedToDev = 'N2'
        self.cellForWatingOnCustomer = 'N3'
        self.cellForAssignedToSupport = 'N4'
        self.cellForAssignedToCSM = 'N5'
        self.cellForOpenToday = 'O2'
        self.cellForCloseToday = 'P2'
        self.cellForAndresQueue = 'G8'
        self.cellForAndresResolved = 'G9'
        self.cellForOscarQueue = 'G18'
        self.cellForOscarResolved = 'G19'
        self.cellForJaimeQueue = 'G13'
        self.cellForJaimeResolved = 'G14'
        self.cellForBoonQueue = 'G23'
        self.cellForBoonResolved = 'G24'
        self.cellForCGQueue = 'G28'
        self.cellForCGResolved = 'G29'

    def setBacklog(self, Desk):
        """Update backlog on sheet"""
        backlog = Desk.deskBacklog()
        sendToSheet(self.cellForBacklog, backlog)
        print 'Updated backlog on data sheet with ' + str(backlog)

    def setUnassignedCases(self, Desk):
        """Update unassign cases on sheet"""
        unassigned = Desk.deskUnassignedCases()
        sendToSheet(self.cellForUnassigned, unassigned)
        print 'Updated unassign cases on sheet with ' + str(unassigned)

    def setOpenThisMonth(self, Desk):
        """Update open cases of the month on sheet"""
        openThisMonth = Desk.deskOpenThisMonth()
        sendToSheet(self.cellForOpenThisMonth, openThisMonth)
        print 'Updated open cases of the month on sheet with ' + str(openThisMonth)

    def setCloseThisMonth(self, Desk):
        """Update close cases of the month on sheet"""
        closeThisMonth = Desk.deskCloseThisMonth()
        sendToSheet(self.cellForCloseThisMonth, closeThisMonth)
        print 'Updated close cases of the month on sheet with ' + str(closeThisMonth)

    def setWatingOnCustomer(self, Desk):
        """Update waiting on customer cases on sheet"""
        waitingOnCustomer = Desk.WaCu
        sendToSheet(self.cellForWatingOnCustomer, waitingOnCustomer)
        print 'Updated waiting on customer cases on sheet with ' + str(waitingOnCustomer)

    def setAssignedToDev(self, Desk):
        """Update assigned to dev cases on sheet"""
        assignedToDev = Desk.AsDev
        sendToSheet(self.cellForAssignedToDev, assignedToDev)
        print 'Updated assigned to dev cases on sheet with ' + str(assignedToDev)

    def setAssignedToSupport(self, Desk):
        """Update assigned to support cases on sheet"""
        assignedToSupport = Desk.AsSu
        sendToSheet(self.cellForAssignedToSupport, assignedToSupport)
        print 'Updated assigned to support cases on sheet with ' + str(assignedToSupport)

    def setAssignedToCSM(self, Desk):
        """Update assigned to CSM cases on sheet"""
        assignedToCSM = Desk.AsCSM
        sendToSheet(self.cellForAssignedToCSM, assignedToCSM)
        print 'Updated assigned to CSM cases on sheet with ' + str(assignedToCSM)

    def setOpenToday(self, Desk):
        """Update open cases of today on sheet"""
        openToday = Desk.deskOpenToday()
        sendToSheet(self.cellForOpenToday, openToday)
        print 'Update open cases of today on sheet with ' + str(openToday)

    def setCloseToday(self, Desk):
        """Update close cases of today on sheet"""
        closeToday = Desk.deskCloseToday()
        sendToSheet(self.cellForCloseToday, closeToday)
        print 'Update close cases of today on sheet with ' + str(closeToday)

    def setAndresQueue(self, Desk):
        """Update andres queue on sheet"""
        andresQueue = Desk.deskAndresQueue()
        sendToSheet(self.cellForAndresQueue, andresQueue)
        print 'Updated andres queue on sheet with ' + str(andresQueue)

    def setAndresResolved(self, Desk):
        """Update andres resolved cases of the the month on sheet"""
        andresResolved = Desk.deskAndresResolved()
        sendToSheet(self.cellForAndresResolved, andresResolved)
        print 'Updated andres resolved cases of the month on sheet with ' + str(andresResolved)

    def setOscarQueue(self, Desk):
        """Update oscar queue on sheet"""
        oscarQueue = Desk.deskOscarQueue()
        sendToSheet(self.cellForOscarQueue, oscarQueue)
        print 'Updated oscar queue on sheet with ' + str(oscarQueue)

    def setOscarResolved(self, Desk):
        """Update oscar resolved cases of the the month on sheet"""
        oscarResolved = Desk.deskOscarResolved()
        sendToSheet(self.cellForOscarResolved, oscarResolved)
        print 'Updated oscar resolved cases of the month on sheet with ' + str(oscarResolved)

    def setJaimeQueue(self, Desk):
        """Update jaime queue on sheet"""
        jaimeQueue = Desk.deskJaimeQueue()
        sendToSheet(self.cellForJaimeQueue, jaimeQueue)
        print 'Updated jaime queue on sheet with ' + str(jaimeQueue)

    def setJaimeResolved(self, Desk):
        """Update jaime resolved cases of the the month on sheet"""
        jaimeResolved = Desk.deskJaimeResolved()
        sendToSheet(self.cellForJaimeResolved, jaimeResolved)
        print 'Updated jaime resolved cases of the month on sheet with ' + str(jaimeResolved)

    def setBoonQueue(self, Desk):
        """Update boon queue on sheet"""
        boonQueue = Desk.deskBoonQueue()
        sendToSheet(self.cellForBoonQueue, boonQueue)
        print 'Updated boon queue on sheet with ' + str(boonQueue)

    def setBoonResolved(self, Desk):
        """Update boon resolved cases of the the month on sheet"""
        boonResolved = Desk.deskBoonResolved()
        sendToSheet(self.cellForBoonResolved, boonResolved)
        print 'Updated boon resolved cases of the month on sheet with ' + str(boonResolved)

    def setCGQueue(self, Desk):
        """Update cg queue on sheet"""
        cgQueue = Desk.deskCGQueue()
        sendToSheet(self.cellForCGQueue, cgQueue)
        print 'Updated cg queue on sheet with ' + str(cgQueue)

    def setCGResolved(self, Desk):
        """Update cg resolved cases of the the month on sheet"""
        cgResolved = Desk.deskCGResolved()
        sendToSheet(self.cellForCGResolved, cgResolved)
        print 'Updated cg resolved cases of the month on sheet with ' + str(cgResolved)


desk = Desk()
sheet = Sheet()
sheet.setBacklog(desk)
sheet.setUnassignedCases(desk)
sheet.setOpenThisMonth(desk)
sheet.setCloseThisMonth(desk)
sheet.setWatingOnCustomer(desk)
sheet.setAssignedToDev(desk)
sheet.setAssignedToSupport(desk)
sheet.setAssignedToCSM(desk)
sheet.setOpenToday(desk)
sheet.setAndresQueue(desk)
sheet.setAndresResolved(desk)
sheet.setOscarQueue(desk)
sheet.setOscarResolved(desk)
sheet.setJaimeQueue(desk)
sheet.setJaimeResolved(desk)
sheet.setBoonQueue(desk)
sheet.setBoonResolved(desk)
sheet.setCGResolved(desk)
sheet.setCGQueue(desk)
