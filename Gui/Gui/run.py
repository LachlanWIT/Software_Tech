import wx
import wx.grid
import pandas as pd
import unittest
from matplotlib import pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
import datetime
from numpy.core.defchararray import lower



data = pd.read_csv('penalty_data_set_2.csv', low_memory=False)


class gui(wx.Frame):

    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, 'Traffic Analysis and Visualisation Tool', size=(800, 800))
        self.panel = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        displayBox = wx.StaticBox(self.panel, label="", pos=(200, 150), size=(520, 550), name="Display")

        box = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(self.panel, -1, pos=(200, 80), style=wx.ALIGN_CENTER)
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        txt = "Traffic analysis tool"
        lbl.SetFont(font)
        lbl.SetLabel(txt)
        self.Centre()
        self.Show()

        # logo
        # img = wx.Image("logo.png", wx.BITMAP_TYPE_ANY)
        # self.image = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img), pos=(50, 50))

        # app icon  #this doesnt work and there is no reason it shouldn't.
        # path = wx.IconLocation(r'icon.ico', 0)
        # self.SetIcon(wx.Icon(path))

        # logo
        # logo = wx.Image('icon.ico', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # wx.StaticBitmap(self, -1, logo, (10 + logo.GetWidth(), 5), (logo.GetWidth(), logo.GetHeight()))

        # creat button
        search = wx.Button(self.panel, -1, "Search Function", (10, 150), (140, -1))
        displayall = wx.Button(self.panel, -1, "All Data Function", (10, 180), (140, -1))
        keyword = wx.Button(self.panel, -1, "DCA code search", (10, 210), (140, -1))
        CamVsRadar = wx.Button(self.panel, -1, "CamVsRadar Function", (10, 240), (140, -1))
        insight = wx.Button(self.panel, -1, "Insight Function", (10, 270), (140, -1))

        kill = wx.Button(self.panel, -1, "EXIT", (10, 725), (140, -1))
        comit = wx.Button(self.panel, label="Commit", id=wx.ID_OK, pos=(675, 115))

        # assign task
        self.Bind(wx.EVT_BUTTON, self.keywordSearch, search)
        self.Bind(wx.EVT_BUTTON, self.DistributionBttn, displayall)
        self.Bind(wx.EVT_BUTTON, self.PenaltyCases, keyword)
        self.Bind(wx.EVT_BUTTON, self.CamVsRadar, CamVsRadar)
        self.Bind(wx.EVT_BUTTON, self.insight, insight)

        self.Bind(wx.EVT_BUTTON, self.onClose, kill)
        self.Bind(wx.EVT_BUTTON, self.comit, comit)

        # date-range
        self.label = wx.StaticText(self.panel, label="Enter start date", pos=(430, 70))
        self.label = wx.StaticText(self.panel, label="Enter end date", pos=(540, 70))
        self.start = wx.TextCtrl(self.panel, value="", size=(100, 20), pos=(430, 90))
        self.end = wx.TextCtrl(self.panel, value="", size=(100, 20), pos=(540, 90))

        # keyword search
        self.label = wx.StaticText(self.panel, label="Enter Keyword", pos=(650, 70))
        self.keyword = wx.TextCtrl(self.panel, value="", size=(100, 20), pos=(650, 90))

        self.userInput = {}
        self.cb1 = wx.CheckBox(self.panel, label='Camera', pos=(430, 115))
        self.cb2 = wx.CheckBox(self.panel, label='Radar', pos=(530, 115))
        self.cvmopt = []

        self.begin = None
        self.stop = None

    # date range

    def keywordSearch(self, event):
        # this doesnt display as gui integration was unsuccessful.
        for row in data:
            if data['OFFENCE_MONTH'] >= self.begin and data["OFFENCE_MONTH"] <= self.stop:
                print(row)

    def comit(self, event):
        cb1 = self.cb1.GetValue()
        cb2 = self.cb2.GetValue()
        camera = (data[data.stack().str.contains("Camera Detected").any(level=0)])
        radar = (data[data.stack().str.contains("Radar").any(level=0)])
        self.begin = self.start.GetValue()
        self.stop = self.end.GetValue()
        print(self.stop, self.begin)

        if cb1 == True and cb2 == True:
            for row in camera:
                if self.begin <= camera["OFFENCE_MONTH"] <= self.stop:
                    print(row)
            for row in radar:
                if self.begin <= radar["OFFENCE_MONTH"] <= self.stop:
                    print(row)
        elif cb1 == False and cb2 == True:
            for row in radar:
                if self.begin <= radar["OFFENCE_MONTH"] <= self.stop:
                    print(row)
        elif cb1 == True and cb2 == False:
            for row in camera:
                if self.begin <= camera["OFFENCE_MONTH"] <= self.stop:
                    print(row)
        elif cb1 == False and cb2 == False:
            # display static text invalid input please refresh.
            print("Please try again")

    def DistributionBttn(self, event):
        # This function did not run within the gui it can be seen running in file named meesum.py
        print()

    #     pd.set_option('max_column', 100)
    #     pd.set_option('max_row', 250)
    #     pd.set_option('display.float_format', lambda x: '%.3f' % x)
    #
    #     df = pd.read_csv(
    #         'penalty_data_set_2.csv',
    #         parse_dates=['OFFENCE_MONTH'], date_parser=lambda x: pd.datetime.strptime(x, '%d/%m/%Y'))
    #
    #     fig, ax = plt.subplots(1, figsize=(22, 6), )
    #     monthly_fine_dist = df.groupby('OFFENCE_MONTH').agg({'TOTAL_VALUE': 'count', }).reset_index()
    #     plt.plot('OFFENCE_MONTH', 'TOTAL_VALUE', data=monthly_fine_dist, linewidth=10)
    #     months = MonthLocator(range(1, 13), bymonthday=1, interval=3)
    #     monthsFmt = DateFormatter("%b '%y")
    #     ax.xaxis.set_major_locator(months)
    #     ax.xaxis.setmajorformatter(monthsFmt)
    #         = plt.xticks(rotation=45)
    #         = plt.tickparams(axis='both', which='major', labelsize=10)
    #         = plt.title('Monthly Number Cases', size=21)

    def PenaltyCases(self, event):
        search_startperiod = wx.TextEntryDialog(None, "Select First Period", "Title", "1/09/2018")
        if search_startperiod.ShowModal() == wx.ID_OK:
            self.answerstartperiod = search_startperiod.GetValue()
        self.userInput['startDate'] = self.answerstartperiod

    def CamVsRadar(self, event):
        # this is due to intergration issues was unable to be run, the code appears under the commit function.
        print()

    def insight(self, event):
        # This doesnt work in the Gui
        camera = (data[data.stack().str.contains("Fixed Digital Speed Camera").any(level=0)])
        radar = (data[data.stack().str.contains("Radar").any(level=0)])
        mcamera = (data[data.stack().str.contains("Mobile Digital Speed Camera").any(level=0)])
        rcamera = (data[data.stack().str.contains("Red Light / Speed Camera").any(level=0)])

        for row in camera:
            if self.start <= camera["OFFENCE_MONTH"] <= self.end:
                print(row)

        for row in radar:
            if self.start <= radar["OFFENCE_MONTH"] <= self.end:
                print(row)

        for row in mcamera:
            if self.start <= mcamera["OFFENCE_MONTH"] <= self.end:
                print(row)

        for row in rcamera:
            if self.start <= rcamera["OFFENCE_MONTH"] <= self.end:
                print(row)

    def onClose(self, event):
        # This works lol
        self.Close()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = gui(parent=None, id=1)
    frame.Show()
    app.MainLoop()
