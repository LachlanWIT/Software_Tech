import wx
import wx.grid



class gui(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Traffic Analysis and Visualisation Tool', size=(1200, 1200))
        self.panel = wx.Panel(self)

        search = wx.Button(self.panel, -1, "Search Function", (10, 150), (140, -1))  # Button will call function search
        self.Bind(wx.EVT_BUTTON, self.keywordSearch, search)

        all = wx.Button(self.panel, -1, "All Data Function", (10, 180),(140, -1))  # Button  will call function All
        self.Bind(wx.EVT_BUTTON, self.DistributionBttn, all)

        keyword = wx.Button(self.panel, -1, "DCA code search", (10, 210), (140, -1))  # Button will call function keyword
        self.Bind(wx.EVT_BUTTON, self.PenaltyCases, keyword)

        CamVsRadar = wx.Button(self.panel, -1, "Analysis Function", (10, 240),(140, -1))  # Button will call function Analysis
        self.Bind(wx.EVT_BUTTON, self.CamVsRadar, CamVsRadar)
        self.cb1 = wx.CheckBox(self.panel, label='Camera', pos=(10, 10))
        self.cb2 = wx.CheckBox(self.panel, label='Radar', pos=(10, 40))
        self.cb3 = wx.CheckBox(self.panel, label='Both', pos=(10, 70))

        insight = wx.Button(self.panel, -1, "Insight Function", (10, 270),(140, -1))  # Button will call function Insight
        self.Bind(wx.EVT_BUTTON, self.insight, insight)

        insightextra = wx.Button(self.panel, -1, "Future functions", (10, 300),(140, -1)) # Aditional button for future addition
        self.Bind(wx.EVT_BUTTON, self.insight, insightextra)

        # extra1 = wx.Button(self.panel, -1, "extra1", (10, 330),(140, -1))  # Additional button for future addition

        # extra2 = wx.Button(self.panel, -1, "extra2", (10, 360),(140, -1))  # Additional button for future addition

        refresh = wx.Button(self.panel, -1, "clear", (10, 390), (140, -1))  # Button to clear screen

        kill = wx.Button(self.panel, -1, "Close", (10, 500), (140, -1))  # Button to Close program
        kill.Bind(wx.EVT_BUTTON, self.onClose)

    def keywordSearch(self, event):
        enter = wx.TextEntryDialog(None, "Enter keyword", "Search Input", "DCA_CODE")
        if enter.ShowModal() == wx.ID_OK:
            self.answer = enter.GetValue()
        self.userInput['Search'] = self.answer

    def DistributionBttn(self, event):
        enterkey = wx.TextEntryDialog(None, "Enter Keyword", "Title", "Pool")
        if enterkey.ShowModal() == wx.ID_OK:
            self.keyword = enterkey.GetValue()
        self.userInput['keywords'] = self.keyword

    def PenaltyCases(self, event):
        search_startperiod = wx.TextEntryDialog(None, "Select First Period", "Title", "1/09/2018")
        if search_startperiod.ShowModal() == wx.ID_OK:
            self.answerstartperiod = search_startperiod.GetValue()
        self.userInput['startDate'] = self.answerstartperiod

    def CamVsRadar(self, event):
        search_endperiod = wx.TextEntryDialog(None, "Select First Period", "Title", "1/09/2018")
        if search_endperiod.ShowModal() == wx.ID_OK:
            self.answerendperiod = search_endperiod.GetValue()
        self.userInput['endDate'] = self.answerendperiod

    def insight(self, event):
        result = wx.StaticText(self.panel, -1, str(self.userInput), (10, 600), (260, 50), wx.ALIGN_CENTER)
        # result.SetSize(1200,2000)
        result.SetForegroundColour('white')
        result.SetBackgroundColour('light blue')
        # print(self.userInput['suburbs'])

    def refresh(self, event):
        self.Refresh()

    def onClose(self, event):
         self.Close()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = gui(parent=None, id=1)
    frame.Show()
    app.MainLoop()
