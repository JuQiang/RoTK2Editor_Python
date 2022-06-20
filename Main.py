import wx
import wx.lib.wordwrap
import wx.lib.scrolledpanel
from Entity.Province import Province
from Entity.RoTK2 import RoTK2
from Entity.Officer import Officer
from Entity.Ruler import Ruler
from Window.SettingsWindow import SettingsWindow
from Window.GeneralWindow import GeneralWindow
from Window.BasicInfoWindow import BasicInfoWindow
from Window.MapWindow import MapWindow
from Window.SelectKingWindow import SelectKingWindow
from Window.WhatWindow import WhatWindow
from Window.WorldMapWindow import WorldMapWindow

class MainWindow(wx.Frame):
    year = 0
    month = 0
    num_zhuhou = 0

    doc = ""
    cur_city = -1
    cur_general = -1
    initializing = True
    path = ""

    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, style=wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.BORDER_NONE)
        self.SetMaxSize((885+188, 850))
        # self.SetMinSize((885, 850))
        self.SetInitialSize(wx.Size(885+188,850))

        #self.font = wx.Font(16,wx.FONTFAMILY_DEFAULT,wx.NORMAL,wx.NORMAL)
        self.Bind(wx.EVT_PAINT, self.OnEntryPaint)
        self.InitUI()

        if RoTK2.HasGamePath() is False:
            while True:
                s = SettingsWindow()
                s.ShowModal()
                if RoTK2.HasGamePath() is True:
                    break
                else:
                    wx.MessageBox("请指定一个包含三国志2游戏文件的目录","目录无效")

        RoTK2.Init()

    def OnEntryPaint(self,e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("white")
        dc.SetBackground(brush)
        dc.Clear()

        if self.initializing is True:
            font = wx.Font(48, wx.ROMAN, wx.NORMAL, wx.NORMAL)
            dc.SetFont(font)
            dc.SetTextForeground(wx.Colour("black"))
            new_text = wx.lib.wordwrap.wordwrap("点击工具栏的【打开】，开启三国志2的存档修改之旅。复杂功能，请点选相关菜单。",self.ClientSize.Width,dc)
            dc.DrawLabel(new_text, wx.Rect(0,0,self.ClientSize.Width,self.ClientSize.Height), alignment=wx.ALIGN_CENTER)

    def InitUI_Menu(self):
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()

        fileMenu.Append(wx.MenuItem(fileMenu, 0x1001, text="打开存档\tctrl+O", kind=wx.ITEM_NORMAL))
        fileMenu.Append(wx.MenuItem(fileMenu, 0x1002, text="保存存档\tctrl+S", kind=wx.ITEM_NORMAL))
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.MenuItem(fileMenu, 0x1004, text="设置", kind=wx.ITEM_NORMAL))
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.MenuItem(fileMenu, 0x1003, text="关于", kind=wx.ITEM_NORMAL))

        countryMenu = wx.Menu()
        countryMenu.Append(wx.MenuItem(countryMenu, 0x2001, text="大势", kind=wx.ITEM_NORMAL))
        countryMenu.Append(wx.MenuItem(countryMenu, 0x2002, text="优化国家经济", kind=wx.ITEM_NORMAL))
        countryMenu.Append(wx.MenuItem(countryMenu, 0x2003, text="优化国家军事", kind=wx.ITEM_NORMAL))

        cityMenu = wx.Menu()
        cityMenu.Append(wx.MenuItem(cityMenu, 0x3001, text="优化郡经济", kind=wx.ITEM_NORMAL))
        cityMenu.Append(wx.MenuItem(cityMenu, 0x3002, text="优化郡军事", kind=wx.ITEM_NORMAL))
        cityMenu.AppendSeparator()
        cityMenu.Append(wx.MenuItem(cityMenu, 0x3003, text="设置主公", kind=wx.ITEM_NORMAL))
        cityMenu.AppendSeparator()
        cityMenu.Append(wx.MenuItem(cityMenu, 0x3004, text="查看地图", kind=wx.ITEM_NORMAL))

        generalMenu = wx.Menu()
        generalMenu.Append(wx.MenuItem(generalMenu, 0x4001, text="优化将领", kind=wx.ITEM_NORMAL))

        infoMenu = wx.Menu()
        infoMenu.Append(wx.MenuItem(infoMenu, 0x5001, text="血缘", kind=wx.ITEM_NORMAL))
        infoMenu.Append(wx.MenuItem(infoMenu, 0x5002, text="新武将", kind=wx.ITEM_NORMAL))
        infoMenu.Append(wx.MenuItem(infoMenu, 0x5003, text="在野武将", kind=wx.ITEM_NORMAL))
        infoMenu.Append(wx.MenuItem(infoMenu, 0x500B, text="TAIKI", kind=wx.ITEM_NORMAL))
        infoMenu.AppendSeparator()
        infoMenu.Append(wx.MenuItem(infoMenu, 0x5004, text="世界地图", kind=wx.ITEM_NORMAL))
        infoMenu.Append(wx.MenuItem(infoMenu, 0x500C, text="WHAT地图", kind=wx.ITEM_NORMAL))
        infoMenu.AppendSeparator()
        infoMenu.Append(wx.MenuItem(infoMenu, 0x5005, text="默认剧本 - 董卓洛阳  189年", kind=wx.ITEM_NORMAL))
        infoMenu.Append(wx.MenuItem(infoMenu, 0x5006, text="默认剧本 - 夺权竞争  194年", kind=wx.ITEM_NORMAL))
        infoMenu.Append(wx.MenuItem(infoMenu, 0x5007, text="默认剧本 - 刘备时期  201年", kind=wx.ITEM_NORMAL))
        infoMenu.Append(wx.MenuItem(infoMenu, 0x5008, text="默认剧本 - 曹操篡位  208年", kind=wx.ITEM_NORMAL))
        infoMenu.Append(wx.MenuItem(infoMenu, 0x5009, text="默认剧本 - 三国鼎立  215年", kind=wx.ITEM_NORMAL))
        infoMenu.Append(wx.MenuItem(infoMenu, 0x500A, text="默认剧本 - 三方竞争  220年", kind=wx.ITEM_NORMAL))

        menubar.Append(fileMenu,"文件")
        menubar.Append(countryMenu, "国家")
        menubar.Append(cityMenu, "郡")
        menubar.Append(generalMenu, "将")
        menubar.Append(infoMenu, "其他信息")

        menubar.Bind(wx.EVT_MENU, self.menuhandler)
        self.MenuBar = menubar

    def menuhandler(self, event):
        id = event.GetId()
        if id == 0x1001:
            self.LoadData()
        elif id == 0x1002:
            self.SaveData()
        elif id == 0x1004:
            self.Settings()
        elif id==0x2001:
            self.ViewCountryInfo()
        elif id==0x2002:
            self.OptimizeCountryEconomy()
        elif id==0x2003:
            self.OptimizeCountryGenerals()
        elif id==0x3001:
            self.OptimizeCityEconomy(self.cur_city)
        elif id == 0x3002:
            self.OptimizeCityGenerals(self.cur_city)
        elif id == 0x3003:
            self.ChangeKing(self.cur_city)
        elif id == 0x3004:
            self.ViewMap()
        elif id == 0x4001:
            self.OptimizeOfficer(self.cur_city,self.cur_general)
        elif id == 0x5004:
            self.ViewWorldMap()
        elif id == 0x500C:
            self.ViewWhatMap()
        elif id >= 0x5005 and id<=0x500A :
            self.ShowStoredGenerals(id-0x5005)
        elif id==0x500B:
            self.ShowTaiki()

        self.bind_data()
        if self.cur_city > -1:
            self.city_list.Select(self.cur_city)
        if self.cur_general > -1:
            self.general_list.Select(self.cur_general)

    def InitUI_Toolbar(self):
        tb = wx.ToolBar(self, -1, style=wx.TB_NOICONS | wx.TB_TEXT)
        self.ToolBar = tb

        tb.AddTool(101, "打开", wx.NullBitmap)
        tb.AddTool(102, "保存", wx.NullBitmap)
        tb.AddSeparator()
        tb.AddTool(203, "城市", wx.NullBitmap)
        tb.AddTool(301, "武将", wx.NullBitmap)

        tb.Bind(wx.EVT_TOOL, self.OnToolbarClicked)
        tb.Realize()

    def OnToolbarClicked(self,event):
        id = event.GetId()
        if id==101:
            self.LoadData()
        elif id==102:
            self.SaveData()
            pass
        elif id==203:
            self.OptimizeCityEconomy(self.cur_city)
        elif id==301:
            self.OptimizeOfficer(self.cur_city,self.cur_general)
        else:
            pass

        self.bind_data()
        if self.cur_city>-1:
            self.city_list.Select(self.cur_city)
        if self.cur_general>-1:
            self.general_list.Select(self.cur_general)

    def InitUI(self):
        self.SetBackgroundColour(wx.WHITE)

        self.InitUI_Menu()
        self.InitUI_Toolbar()
        self.InitUI_Main()

        self.Centre()
        self.Show(True)

    def InitUI_Main(self):
        self.panel_left = wx.Panel(self)
        self.panel_right = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        self.city_list = wx.ListCtrl(self.panel_left, -1, style=wx.LC_REPORT | wx.LC_SINGLE_SEL,size=(640, 810))
        self.city_list.InsertColumn(0, "編號", wx.LIST_FORMAT_CENTER, width=40)
        self.city_list.InsertColumn(1, "郡", wx.LIST_FORMAT_CENTER, width=40)
        self.city_list.InsertColumn(2, "諸侯", wx.LIST_FORMAT_CENTER, width=60)
        self.city_list.InsertColumn(3, "太守", wx.LIST_FORMAT_CENTER, width=60)
        self.city_list.InsertColumn(4, "忠诚度", wx.LIST_FORMAT_CENTER, width=40)
        self.city_list.InsertColumn(5, "將領數", wx.LIST_FORMAT_RIGHT, width=40)
        self.city_list.InsertColumn(6, "黃金", wx.LIST_FORMAT_RIGHT, width=60)
        self.city_list.InsertColumn(7, "糧食", wx.LIST_FORMAT_RIGHT, width=100)
        self.city_list.InsertColumn(8, "米價", wx.LIST_FORMAT_RIGHT, width=40)
        self.city_list.InsertColumn(9, "代理", wx.LIST_FORMAT_RIGHT, width=40)
        self.city_list.InsertColumn(10, "运输郡", wx.LIST_FORMAT_RIGHT, width=60)
        self.city_list.InsertColumn(11, "战争郡", wx.LIST_FORMAT_RIGHT, width=60)

        box_city = wx.BoxSizer(wx.VERTICAL)
        self.panel_city = wx.Panel(self.panel_right, size=(450, 250))
        self.panel_city.Bind(wx.EVT_PAINT, self.OnCityPaint)
        self.general_list = wx.ListCtrl(self.panel_right, -1, style=wx.LC_REPORT | wx.BORDER_SIMPLE | wx.LC_SINGLE_SEL,
                                        size=(430, 390))
        self.general_list.InsertColumn(0, "將領", width=60)
        self.general_list.InsertColumn(1, "忠誠", wx.LIST_FORMAT_RIGHT, width=60)
        self.general_list.InsertColumn(2, "才智", wx.LIST_FORMAT_RIGHT, width=40)
        self.general_list.InsertColumn(3, "戰力", wx.LIST_FORMAT_RIGHT, width=40)
        self.general_list.InsertColumn(4, "號召", wx.LIST_FORMAT_RIGHT, width=40)
        self.general_list.InsertColumn(5, "士兵", wx.LIST_FORMAT_RIGHT, width=60)
        self.general_list.InsertColumn(6, "訓練", wx.LIST_FORMAT_RIGHT, width=40)
        self.general_list.InsertColumn(7, "武器", wx.LIST_FORMAT_RIGHT, width=60)
        self.panel_general = wx.Panel(self.panel_right, size=(430, 60))
        self.panel_general.Bind(wx.EVT_PAINT, self.OnGeneralPaint)
        box_city.Add(self.panel_city, 0)
        box_city.Add(self.general_list, 1)
        box_city.AddSpacer(5)
        box_city.Add(self.panel_general, 2)
        box_city.AddSpacer(5)
        self.panel_right.SetSizer(box_city)
        self.panel_right.Fit()

        box.Add(self.panel_left, -1, wx.ALIGN_LEFT)
        box.Add(self.panel_right, -1, wx.ALIGN_LEFT)
        self.SetSizer(box)

        self.city_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnCitySelected)
        self.general_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnGeneralSelected)
        self.panel_left.Hide()
        self.panel_right.Hide()
        self.Fit()

    def LoadData(self):
        dlg = wx.FileDialog(self, "打开三国志2存档文件",RoTK2.GamePath)
        if dlg.ShowModal() == wx.ID_OK:
            self.initializing = False
            self.doc = dlg.Path
            items = dlg.Path.split("/")
            path = ""
            for i in range(0, len(items) - 1):
                path += items[i]
                path += "/"
            self.path = path
            f = open(self.doc, "rb")
            tmp_buf = f.read(30752)
            f.close()
            RoTK2.SaveData = bytearray(tmp_buf)


            Ruler.RulerList = []
            Province.CityList = []

            self.year = RoTK2.SaveData[0x0d] * 256 + RoTK2.SaveData[0x0c]
            self.month = RoTK2.SaveData[0x0e]
            self.num_zhuhou = RoTK2.SaveData[0x0f]

            self.bind_data()

            self.cur_city = 0

            self.city_list.Select(0)

            self.panel_left.Show()
            self.panel_right.Show()
            self.Fit()

        dlg.Destroy()

    def SaveData(self):
        if RoTK2.SaveData is None:
            wx.MessageBox("请先打开一个存档文件")
            return

        f = open(self.doc,"wb")
        f.write(RoTK2.SaveData)
        f.close()

    def Settings(self):
        s = SettingsWindow()
        s.ShowModal()

    def bind_data(self):
        if self.doc=="":
            return

        Ruler.RulerList = []
        Province.CityList = []

        Ruler.GetList()

        row = 0
        self.city_list.DeleteAllItems()
        for c in Province.GetList():
            index = self.city_list.InsertItem(row, str(c.No))
            items = Province.Name.split("-")
            self.city_list.SetItem(index,1,items[0])

            self.city_list.SetItem(index, 2, Ruler.GetRulerByNo(c.RulerNo).RulerSelf.Name)
            self.city_list.SetItem(index, 3, Officer.GetOfficerByOffset(c.Governor).Name)
            self.city_list.SetItem(index, 4, str(Officer.GetOfficerByOffset(c.Governor).Loyalty))
            self.city_list.SetItem(index, 5, str(len(c.OfficerList)))
            self.city_list.SetItem(index, 6, str(c.Gold))
            self.city_list.SetItem(index, 7, str(c.Rice))
            self.city_list.SetItem(index, 8, str(c.RicePrice))
            self.city_list.SetItem(index, 9, c.DelegateControl)
            self.city_list.SetItem(index, 10, c.ProvinceSendGoods)
            self.city_list.SetItem(index, 11, c.ProvinceInvade)
            row += 1

    def OptimizeCountryEconomy(self):
        if RoTK2.SaveData is None:
            wx.MessageBox("请先打开一个存档文件")
            return

        selected_ruler = self.select_ruler()
        if selected_ruler is None:
            return

        for c in selected_ruler.GetCityList() :
            self.OptimizeCityEconomy(c.No-1)

    def select_ruler(self):
        if self.doc=="":
            return -1
        ruler_offset = Province.GetList()[self.cur_city].RulerNo
        test = SelectKingWindow(Ruler.GetList(), Ruler.GetRulerByNo(ruler_offset).RulerSelf.Name)
        test.ShowModal()

        selected_ruler = test.selected_ruler

        test.Destroy()

        return selected_ruler

    def OptimizeCountryGenerals(self):
        if RoTK2.SaveData is None:
            wx.MessageBox("请先打开一个存档文件")
            return

        selected_ruler = self.select_ruler()
        if selected_ruler is None:
            return

        for c in selected_ruler.GetCityList():
            self.OptimizeCityGenerals(c.No-1)

    def ChangeKing(self,city):
        if RoTK2.SaveData is None:
            wx.MessageBox("请先打开一个存档文件")
            return

        c = Province.GetList()[city]
        selected_ruler = self.select_ruler()
        if selected_ruler is None:
            return

        last_city_offset = selected_ruler.GetCityList()[-1].Offset
        RoTK2.SaveData[last_city_offset + 0x00] = (c.Offset + 0x38) & 0xff
        RoTK2.SaveData[last_city_offset + 0x01] = (c.Offset + 0x38) >> 8
        RoTK2.SaveData[c.Offset + 0x10] = selected_ruler.No
        RoTK2.SaveData[c.Offset + 0x00] = 0x00
        RoTK2.SaveData[c.Offset + 0x01] = 0x00

    def ViewCountryInfo(self):
        if RoTK2.SaveData is None:
            wx.MessageBox("请先打开一个存档文件")
            return

        info = BasicInfoWindow(self, 9998, Ruler.GetList())
        info.ShowModal()

    def ShowStoredGenerals(self,seq):
        gen_list = Officer.GetStoredOfficerList(seq)
        gen_win = GeneralWindow(self,-1,self.MenuBar.GetLabel(seq+0x5005),gen_list)
        gen_win.ShowModal()

    def ShowTaiki(self):
        gen_list = Officer.get_taiki_gen_list()
        gen_win = GeneralWindow(self, -1, self.MenuBar.GetLabel(0x500B), gen_list)
        gen_win.ShowModal()

    def ViewMap(self):
        if RoTK2.SaveData is None:
            wx.MessageBox("请先打开一个存档文件")
            return

        if self.cur_city<0:
            return

        start = 0x33b9+156*self.cur_city
        map_data = RoTK2.SaveData[start:start + 12 * 13]

        test = MapWindow(self, 9999, Province.GetList()[self.cur_city].Name, map_data)
        test.ShowModal()

    def ViewWhatMap(self):
        test = WhatWindow(self)
        test.ShowModal()

    def ViewWorldMap(self):
        # worldmap_data = []
        # for i in range(0,41):
        #     start = 0x33b9+156*i
        #     map_data = sg2.gamedata[start:start+12*13]
        #     worldmap_data.append(map_data)

        test = WorldMapWindow(self, 9997)
        test.ShowModal()

    def OptimizeCityEconomy(self,city):

        if RoTK2.SaveData is None:
            wx.MessageBox("请先打开一个存档文件")
            return

        c = Province.GetList()[city]
        if c is None:
            return

        start = c.Offset
        RoTK2.SaveData[start + 0x08] = 0x30
        RoTK2.SaveData[start + 0x09] = 0x75

        RoTK2.SaveData[start + 0x0A] = 0xC0
        RoTK2.SaveData[start + 0x0B] = 0xC6
        RoTK2.SaveData[start + 0x0C] = 0x2D
        RoTK2.SaveData[start + 0x0D] = 0x00

        RoTK2.SaveData[start + 0x0E] = 0x30
        RoTK2.SaveData[start + 0x0F] = 0x75
        RoTK2.SaveData[start + 0x16] = 0x64
        RoTK2.SaveData[start + 0x17] = 0x64
        RoTK2.SaveData[start + 0x18] = 0x64
        RoTK2.SaveData[start + 0x19] = 0x64
        RoTK2.SaveData[start + 0x1B] = 0x64

    def OptimizeCityGenerals(self,city):
        if RoTK2.SaveData is None:
            wx.MessageBox("请先打开一个存档文件")
            return

        c = Province.GetList()[city]
        if c is None:
            return

        index = 0
        for gen in c.OfficerList:
            self.OptimizeOfficer(city,index)
            index += 1

    def OptimizeOfficer(self, city,o_no):
        if RoTK2.SaveData is None:
            wx.MessageBox("请先打开一个存档文件")
            return

        c = Province.GetList()[city]
        o = c.OfficerList[o_no]
        if o is None or o.Offset<0x20:
            return

        RoTK2.SaveData[o.Offset + 0x04] = 0x64
        RoTK2.SaveData[o.Offset + 0x04] = 0x64
        RoTK2.SaveData[o.Offset + 0x05] = 0x64
        RoTK2.SaveData[o.Offset + 0x06] = 0x64
        RoTK2.SaveData[o.Offset + 0x07] = 0x64
        RoTK2.SaveData[o.Offset + 0x08] = 0x64
        RoTK2.SaveData[o.Offset + 0x09] = 0x64
        RoTK2.SaveData[o.Offset + 0x0B] = 0x64
        RoTK2.SaveData[o.Offset + 0x12] = 0x10
        RoTK2.SaveData[o.Offset + 0x13] = 0x27
        RoTK2.SaveData[o.Offset + 0x14] = 0x10
        RoTK2.SaveData[o.Offset + 0x15] = 0x27
        RoTK2.SaveData[o.Offset + 0x16] = 0x64

        return

    def OnGeneralSelected(self,event):
        self.cur_general = event.Index

        self.panel_general.Refresh()

    def OnCitySelected(self,event):
        if self.cur_city<0:
            return

        row = 0
        p = Province.GetList()[event.Index]
        self.general_list.DeleteAllItems()

        for gen in p.OfficerList:
            index = self.general_list.InsertItem(row, gen.Name)
            if gen.IsUnClaimed is True:
                self.general_list.SetItemTextColour(index,wx.Colour("purple"))
            elif gen.IsFree is True:
                self.general_list.SetItemTextColour(index,wx.Colour("SEA GREEN"))
            else:
                self.general_list.SetItemTextColour(index,wx.Colour("black"))
            self.general_list.SetItem(index, 1, str(gen.Loyalty))
            self.general_list.SetItem(index, 2, str(gen.Int))
            self.general_list.SetItem(index, 3, str(gen.War))
            self.general_list.SetItem(index, 4, str(gen.Chm))
            self.general_list.SetItem(index, 5, str(gen.Soldiers))
            self.general_list.SetItem(index, 6, str(gen.TrainingLevel))
            self.general_list.SetItem(index, 7, str(gen.Arms))

            row += 1

        self.cur_city = event.Index
        self.cur_general = -1
        if self.general_list.GetItemCount()>0:
            self.general_list.Select(0)
            self.cur_general = 0

        self.panel_city.Refresh()
        self.panel_general.Refresh()
        #self.panel_main.Refresh()
        return

    def OnGeneralPaint(self, e):
        dc = wx.PaintDC(self.panel_general)
        brush = wx.Brush("black")
        dc.SetBackground(brush)
        dc.Clear()

        if self.doc=="" or self.cur_city<0 or self.cur_general<0:
            return

        general = Province.GetList()[self.cur_city].OfficerList[self.cur_general]

        index = general.Portrait
        if index > RoTK2.MaxNumberOfGenerals:
            RoTK2.DrawGenericFace(dc, index + 1, 20, 45, 80, 96)
        else:
            RoTK2.DrawFace(dc, index, 20, 45, 80, 96)

        font = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        dc.SetFont(font)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.Name), wx.Rect(20, 10, 80, 30), alignment=wx.ALIGN_CENTER)

        start = 130
        starty = 10

        font = wx.Font(14, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        dc.SetFont(font)
        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("年齡", start, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.Age), wx.Rect(start + 50, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("生病", start+100, starty)
        dc.SetTextForeground(wx.Colour("white"))
        shengbing = "否"
        if general.IsSick==1:
            shengbing = "是"
        dc.DrawLabel(shengbing, wx.Rect(start+150, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("侍衛", start+200, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.shiwei), wx.Rect(start+250, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        starty += 40
        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("義理", start, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.yili), wx.Rect(start + 50, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("仁德", start + 100, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.rende), wx.Rect(start + 150, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("野望", start + 200, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.yewang), wx.Rect(start + 250, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        starty += 40
        dc.SetTextForeground(wx.Colour("cyan"))
        dc.DrawText("相性", start, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.xiangxing), wx.Rect(start + 50, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("cyan"))
        dc.DrawText("兇兆", start + 100, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.WillDieInNextYear), wx.Rect(start + 150, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("cyan"))
        dc.DrawText("血緣", start + 200, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.xueyuan), wx.Rect(start + 250, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        starty += 35
        dc.SetTextForeground(wx.Colour("purple"))
        dc.DrawText("埋伏諸侯", start, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.SpyBlongedToRuler), wx.Rect(start + 50, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("purple"))
        dc.DrawText("埋伏城市", start + 100, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.SpyInCityNo), wx.Rect(start + 150, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("purple"))
        dc.DrawText("內應月數", start + 200, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(general.MonthCannotMove), wx.Rect(start + 250, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        return

    def OnCityPaint(self,e):
        if self.doc=="" or self.cur_city<0:
            return

        c = Province.GetList()[self.cur_city]# self.chengshi_liebiao[0x2d8c + 0x23 * self.cur_city]

        dc = wx.PaintDC(self.panel_city)
        brush = wx.Brush("white")
        dc.SetBackground(brush)
        dc.Clear()

        pen = wx.Pen(wx.Colour("red"))
        dc.SetPen(pen)
        dc.DrawRectangle(1,5,430,110)
        font = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        dc.SetFont(font)
        dc.DrawText(c.Name, 10, 30)


        if c.RulerNo==0xff:
            dc.DrawText("（空地）",60,30)
        else:
            r = Ruler.GetRulerByNo(c.RulerNo)
            trust = r.TrustRating

            dc.SetTextForeground(wx.Colour("red"))
            dc.DrawText("諸侯：", 150, 30)
            dc.SetTextForeground(wx.Colour("black"))
            dc.DrawText("{0}（信任度  {1}）".format(r.RulerSelf.Name, trust), 200, 30)

            dc.SetTextForeground(wx.Colour("blue"))
            dc.DrawText("太守：", 150, 80)
            dc.SetTextForeground(wx.Colour("black"))
            dc.DrawText(Officer.GetOfficerByOffset(c.Governor).Name, 200, 80)

            # city_off = (sg2.gamedata[0x2afc + 0x29 * ruler_offset + 3] << 8) + (
            #     sg2.gamedata[0x2afc + 0x29 * ruler_offset + 2]) - 0x38
            # if city_off == c.offset:
            #     junshi_off = (sg2.gamedata[0x2afc + 0x29 * ruler_offset + 5] << 8) + (
            #         sg2.gamedata[0x2afc + 0x29 * ruler_offset + 4]) - 0x38
            if r.Advisor is not None and r.HomeCity.Offset == c.Offset:
                dc.SetTextForeground(wx.Colour("purple"))
                dc.DrawText("軍師：", 260, 80)
                dc.SetTextForeground(wx.Colour("black"))
                #dc.DrawText(general.get_general_by_offset(junshi_off).name, 300, 80)
                dc.DrawText(r.Advisor.Name, 310, 80)

            index = Officer.GetOfficerByOffset(c.Governor).Portrait
            if index > 218:
                RoTK2.DrawGenericFace(dc, index + 1, 375, 30, 51, 64)
            else:
                RoTK2.DrawFace(dc, index, 375, 30, 51, 64)

        pen = wx.Pen("black")
        dc.SetPen(pen)
        brush = wx.Brush("black")
        dc.SetBrush(brush)
        dc.DrawRectangle(1,120,430,125)
        dc.SetTextForeground(wx.Colour("cyan"))
        dc.DrawText("人口", 10, 130)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(c.Population), wx.Rect(70, 130, 50, 30), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("cyan"))
        dc.DrawText("士兵", 10, 160)
        shibing = 0
        gens = 0
        for gen in c.OfficerList:
            if gen.IsUnClaimed is False and gen.IsFree is False:
                shibing += gen.Soldiers
                gens += 1
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(shibing), wx.Rect(70, 160, 50, 30), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("purple"))
        dc.DrawText("在職將領", 10, 190)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gens), wx.Rect(70, 190, 50, 30), alignment=wx.ALIGN_RIGHT)
        #dc.DrawText(str(gens), 100, 190)

        zaiye = 0
        for gen in c.OfficerList:
            if gen.IsUnClaimed is True:
                zaiye += 1
        dc.SetTextForeground(wx.Colour("purple"))
        dc.DrawText("在野將領", 10, 220)
        if zaiye>0:
            dc.DrawLabel(str(zaiye), wx.Rect(40, 220, 80, 30), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("黄金", 150, 130)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(c.Gold), wx.Rect(200, 130, 70, 30), alignment=wx.ALIGN_RIGHT)


        #民忠誠度地價治水度城堡
        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("糧食", 150, 160)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(c.Rice), wx.Rect(200, 160, 70, 30), alignment=wx.ALIGN_RIGHT)


        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("米價", 150, 190)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(c.RicePrice), wx.Rect(200, 190, 70, 30), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("良駒", 150, 220)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(c.Horses), wx.Rect(200, 220, 70, 30), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("民忠誠度", 290, 130)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(c.PeopleLoyalty), wx.Rect(370, 130, 50, 30), alignment=wx.ALIGN_RIGHT)

        #
        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("地價", 290, 160)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(c.Land), wx.Rect(370, 160, 50, 30), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("治水度", 290, 190)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(c.FloodControl), wx.Rect(370, 190, 50, 30), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("城堡", 290, 220)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(c.Cost), wx.Rect(370, 220, 50, 30), alignment=wx.ALIGN_RIGHT)

def main():

    #诸侯姓名，如果是汉字，则从0x7778开始，每28个字节代表一个汉字。
    #索引则是从D8F0开始减。

    # 勢力 0 顏色	03	藍紫	曹操、曹丕
    # 勢力 1 顏色	06	綠色	劉備
    # 勢力 2 顏色	0a	紅色	孫堅、孫策、孫權
    # 勢力 3 顏色	01	黃色	袁紹、孟獲
    # 勢力 4 顏色	04	粉紅	袁術、公孫淵
    # 勢力 5 顏色	05	靛色	馬騰
    # 勢力 6 顏色	0b	深紫	劉焉、劉璋
    # 勢力 7 顏色	08	淡藍	劉表
    # 勢力 8 顏色	00	灰色	董卓、呂布
    # 勢力 9 顏色	0f	橘色	公孫瓚
    # 勢力 a 顏色	02	土橘	陶謙、張魯
    # 勢力 b 顏色	0e	深綠	韓馥、金旋
    # 勢力 c 顏色	0c	膚色	孔融、韓玄
    # 勢力 d 顏色	09	藍色	王朗、趙範
    # 勢力 e 顏色	0d	土黃	劉繇、劉度
    # 勢力 f 顏色	07	水藍	新諸侯
    #0c，0d，年
    #0e，月，从0开始算

#     編號	血緣	編號	同盟	編號	州名
# 00 00	無	00 00	無	00	幽州
# 01 00	曹操	01 00	與勢力 01 同盟	01	并州
# 02 00	劉備	02 00	與勢力 02 同盟	02	冀州
# 04 00	孫堅	04 00	與勢力 03 同盟	03	青州
# 08 00	袁紹	08 00	與勢力 04 同盟	04	兗州
# 10 00	袁術	10 00	與勢力 05 同盟	05	司州
# 20 00	馬騰	20 00	與勢力 06 同盟	06	雍州
# 40 00	劉焉	40 00	與勢力 07 同盟	07	涼州
# 80 00	劉表	80 00	與勢力 08 同盟	08	徐州
# 00 01	董卓	00 01	與勢力 09 同盟	09	予州
# 00 02	公孫瓚	00 02	與勢力 10 同盟	0a	荊州
# 00 04	張魯	00 04	與勢力 11 同盟	0b	揚州
# 00 08	孟獲	00 08	與勢力 12 同盟	0c	益州
# 00 10	血緣 13	00 10	與勢力 13 同盟	0d	交州
# 00 20	血緣 14	00 20	與勢力 14 同盟
# 00 40	血緣 15	00 40	與勢力 15 同盟
# 00 80	新諸侯	00 80	與勢力 16 同盟
# ff ff	全血緣	ff ff	與全國勢力同盟

    ex = wx.App()
    MainWindow(None, '三國誌2存檔修改器')
    ex.MainLoop()

if __name__=="__main__":
    main()

# buf = [0x39,0x9e,0xe6,0xa8]
# for alias_key in encodings.aliases.aliases:
#     key = encodings.aliases.aliases[alias_key]
#     try:
#         print("{0},{1}".format(key,b'\x39\x9e'.decode(key)))
#     except Exception as e:
#         pass