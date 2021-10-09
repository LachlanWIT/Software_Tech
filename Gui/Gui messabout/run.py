import wx
import wx.grid


class gui(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Traffic Analysis and Visualisation Tool', size=(800, 800))
        self.panel = wx.Panel(self)

        # asthetic information
        # Title bar
        box = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(self.panel, -1, pos=(200, 80), style=wx.ALIGN_CENTER)
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        txt = "Traffic analysis tool"
        lbl.SetFont(font)
        lbl.SetLabel(txt)
        self.Centre()
        self.Show()

        # logo
        #img = wx.Image("logo.png", wx.BITMAP_TYPE_ANY)
        #self.image = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img), pos=(50, 50))

        # app icon  #this doesnt work and there is no reason it shouldn't.
        # path = wx.IconLocation(r'icon.ico', 0)
        # self.SetIcon(wx.Icon(path))

        # logo
        # alternate (simpler) way to load and display a jpg image from a file
        # actually you can load .jpg  .png  .bmp  or .gif files
        # logo = wx.Image('icon.ico', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # bitmap upper left corner is in the position tuple (x, y) = (5, 5)
        # wx.StaticBitmap(self, -1, logo, (10 + logo.GetWidth(), 5), (logo.GetWidth(), logo.GetHeight()))

        # creat button
        search = wx.Button(self.panel, -1, "Search Function", (10, 150), (140, -1))
        displayall = wx.Button(self.panel, -1, "All Data Function", (10, 180), (140, -1))
        keyword = wx.Button(self.panel, -1, "DCA code search", (10, 210), (140, -1))
        CamVsRadar = wx.Button(self.panel, -1, "CamVsRadar Function", (10, 240), (140, -1))
        insight = wx.Button(self.panel, -1, "Insight Function", (10, 270), (140, -1))
        insightextra = wx.Button(self.panel, -1, "Future functions", (10, 300), (140, -1))
        refresh = wx.Button(self.panel, -1, "clear", (10, 390), (140, -1))
        kill = wx.Button(self.panel, -1, "EXIT", (10, 725), (140, -1))

        # assign task
        self.Bind(wx.EVT_BUTTON, self.keywordSearch, search)
        self.Bind(wx.EVT_BUTTON, self.DistributionBttn, displayall)
        self.Bind(wx.EVT_BUTTON, self.PenaltyCases, keyword)
        self.Bind(wx.EVT_BUTTON, self.CamVsRadar, CamVsRadar)
        self.Bind(wx.EVT_BUTTON, self.insight, insight)
        self.Bind(wx.EVT_BUTTON, self.insight, insightextra)
        kill.Bind(wx.EVT_BUTTON, self.onClose)

        # date-range
        self.label = wx.StaticText(self.panel, label="Enter start date", pos=(430, 70))
        self.field1 = wx.TextCtrl(self.panel, value="", size=(100, 20), pos=(430, 90))
        start = None

        self.label = wx.StaticText(self.panel, label="Enter end date", pos=(540, 70))
        self.field2 = wx.TextCtrl(self.panel, value="", size=(100, 20), pos=(540, 90))
        end = None

        # keyword search
        self.label = wx.StaticText(self.panel, label="Enter Keyword", pos=(650, 70))
        self.keyword = wx.TextCtrl(self.panel, value="", size=(100, 20), pos=(650, 90))
        self.keyword = None

        # commit to variables
        self.okbttn = wx.Button(self.panel, label="Commit", id=wx.ID_OK, pos=(675, 115))

    # date range
    def onOK(self, event):
        start = self.field1.GetValue()
        end = self.field2.GetValue()
        self.Destroy()

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

    def CamVsRadar(self, event, ):
        # how to display the output
        result = wx.ScrolledCanvas(self.panel)
        # self.cb1 = wx.CheckBox(self.panel, label='Camera', pos=(10, 10))
        # self.cb2 = wx.CheckBox(self.panel, label='Radar', pos=(10, 40))

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
