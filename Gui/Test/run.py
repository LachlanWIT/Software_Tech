import wx
import wx.grid
import pandas as pd
import csv
from datetime import datetime


class gui(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Traffic Analysis and Visualisation Tool', size=(1200, 1200))
        self.panel = wx.Panel(self)

        search = wx.Button(self.panel, -1, "Search Function", (10, 150), (140, -1))  # Button will call function search
        self.Bind(wx.EVT_BUTTON, self.entersuburbbutton, search)

        all = wx.Button(self.panel, -1, "All Data Function", (10, 180),(140, -1))  # Button  will call function All
        self.Bind(wx.EVT_BUTTON, self.enterkeywordbutton, all)

        keyword = wx.Button(self.panel, -1, "DCA code search", (10, 210), (140, -1))  # Button will call functionkeyword
        self.Bind(wx.EVT_BUTTON, self.startperiodbutton, keyword)

        analysis = wx.Button(self.panel, -1, "Analysis Function", (10, 240),(140, -1))  # Button will call function Analysis
        self.Bind(wx.EVT_BUTTON, self.endperiodbutton, analysis)

        insight = wx.Button(self.panel, -1, "Insight Function", (10, 270),(140, -1))  # Button will call function Insight
        self.Bind(wx.EVT_BUTTON, self.search, insight)

        extra = wx.Button(self.panel, -1, "Future functions", (10, 300),(140, -1))  # Aditional button for future addition
        self.Bind(wx.EVT_BUTTON, self.searchagain, extra)

        extra1 = wx.Button(self.panel, -1, "extra1", (10, 330),(140, -1))  # Aditional button for future addition

        extra3 = wx.Button(self.panel, -1, "extra2", (10, 360),(140, -1))  # Button to close application

        clear = wx.Button(self.panel, -1, "clear", (10, 390), (140, -1))  # Button to clear screen
        kill = wx.Button(self.panel, -1, "Close", (10, 500), (140, -1))  # Button to Close program
        kill.Bind(wx.EVT_BUTTON, self.onClose)

    def entersuburbbutton(self, event):
        enter = wx.TextEntryDialog(None, "Enter Suburb", "Title", "Ashgrove")
        if enter.ShowModal() == wx.ID_OK:
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
        result = wx.StaticText(self.panel, -1, str(self.userInput), (10, 600), (260, 50), wx.ALIGN_CENTER)
        # result.SetSize(1200,2000)
        result.SetForegroundColour('white')
        result.SetBackgroundColour('light blue')
        # print(self.userInput['suburbs'])

    def searchagain(self, event):
        self.Refresh()

    def onClose(self, event):
         self.Close()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = gui(parent=None, id=1)
    frame.Show()
    app.MainLoop()
