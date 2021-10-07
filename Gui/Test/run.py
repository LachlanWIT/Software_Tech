import wx
import wx.grid
import pandas as pd
import csv
from datetime import datetime


class gui (wx.Frame) :

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'System Analysis and Visualisation Tool', size=(1200, 1200))
        self.panel = wx.Panel(self)

        getname = wx.TextEntryDialog(None,"What's you Name", "Title", 'Enter Name')
        if getname.ShowModal()==wx.ID_OK:
            gottenname = getname.GetValue()

        self.userInput = {}

        customise = wx.StaticText(self.panel, -1, gottenname, (10,50), (260,50), wx.ALIGN_CENTER)
        customise.SetSize(1200,20)
        customise.SetForegroundColour('white')
        customise.SetBackgroundColour('light blue')

        enter_Suburb =  wx.Button(self.panel, -1, "Enter Suburb",(10,130), (140,-1))
        self.Bind(wx.EVT_BUTTON, self.entersuburbbutton, enter_Suburb)


        enter_keyword = wx.Button(self.panel, -1, "Enter Keyword", (10, 190), (140, -1))
        self.Bind(wx.EVT_BUTTON, self.enterkeywordbutton, enter_keyword)

        search_startperiod = wx.Button(self.panel, -1, "Select Start Period", (550, 130), (140, -1))
        self.Bind(wx.EVT_BUTTON, self.startperiodbutton, search_startperiod)

        search_endperiod = wx.Button(self.panel, -1, "Select End Period", (850, 130), (140, -1))
        self.Bind(wx.EVT_BUTTON, self.endperiodbutton, search_endperiod)

        search = wx.Button(self.panel,-1, "Search", (300, 410), (500, -1))
        self.Bind(wx.EVT_BUTTON, self.search, search)

        searchagain = wx.Button(self.panel, -1, "Search Again", (300, 440), (500, -1))
        self.Bind(wx.EVT_BUTTON, self.searchagain, searchagain)

        showprice = wx.Button(self.panel, -1, "Show Price Distribution", (300, 470), (500, -1))

        popularproperties = wx.Button(self.panel, -1, "Show Popular Properties", (300, 500), (500, -1))

        cleanliness = wx.Button(self.panel, -1, "See Cleanliness Comments", (300, 530), (500, -1))



    def entersuburbbutton(self,event):
        enter = wx.TextEntryDialog(None, "Enter Suburb", "Title", "Ashgrove")
        if enter.ShowModal()==wx.ID_OK:
            self.answer = enter.GetValue()
        self.userInput['suburbs'] = self.answer

    def enterkeywordbutton(self, event):
        enterkey = wx.TextEntryDialog(None, "Enter Keyword", "Title", "Pool")
        if enterkey.ShowModal() == wx.ID_OK:
            self.keyword = enterkey.GetValue()
        self.userInput['keywords'] = self.keyword

    def startperiodbutton(self, event):
        search_startperiod = wx.TextEntryDialog(None, "Select First Period", "Title", "1/09/2018")
        if search_startperiod.ShowModal() == wx.ID_OK:
            self.answerstartperiod = search_startperiod.GetValue()
        self.userInput['startDate'] = self.answerstartperiod

    def endperiodbutton(self, event):
        search_endperiod = wx.TextEntryDialog(None, "Select First Period", "Title", "1/09/2018")
        if search_endperiod.ShowModal() == wx.ID_OK:
            self.answerendperiod = search_endperiod.GetValue()
        self.userInput['endDate'] = self.answerendperiod

    def search(self, event):
        result = wx.StaticText(self.panel, -1, str(self.userInput), (10,600), (260,50), wx.ALIGN_CENTER)
        # result.SetSize(1200,2000)
        result.SetForegroundColour('white')
        result.SetBackgroundColour('light blue')
        # print(self.userInput['suburbs'])

    def searchagain(self,event):
        self.Refresh()

        
#lachlan test function 1
#import data
data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)

#assign variable name for if statement from global button variable in GUI
startdate = search_startperiod
enddate = search_endperiod 


#print to console all cases based on camera or radar

camera = (data[data.stack().str.contains("Camera Detected").any(level=0)])
radar = (data[data.stack().str.contains("Radar").any(level=0)])

#apply date range filter

for row in camera:
    if camera["OFFENCE_MONTH"] >= startdate and camera["OFFENCE_MONTH"]<= enddate:
        print(row)

for row in radar:
    if radar["OFFENCE_MONTH"] >= startdate and radar["OFFENCE_MONTH"]<= enddate:
        print(row)

#need statement to trigger this if user selects correct button option - will work with jack at uni
        



if __name__ == '__main__':
     app = wx.PySimpleApp()
     frame = gui(parent=None, id=1)
     frame.Show()
     app.MainLoop()
