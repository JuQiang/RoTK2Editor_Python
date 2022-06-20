import wx
from Entity.RoTK2 import RoTK2

class GeneralWindow(wx.Dialog):
    x = 10
    y = 10
    width = 60
    height = 20

    def __init__(self,parent,id,period,gen_list):
        wx.Frame.__init__(self,parent,id,period,size=(1000,1000), style=wx.CLOSE_BOX|wx.BORDER_NONE)

        self.gen_list = gen_list
        #self.SetSize((len(ruler_list)+2)*self.width+2*self.x,(len(ruler_list)+3)*self.height+1*self.y)
        #self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        box_city = wx.BoxSizer(wx.VERTICAL)
        self.panel_general = wx.Panel(self, size=(430, 150))
        self.panel_general.Bind(wx.EVT_PAINT, self.OnGeneralPaint)

        self.general_list = wx.ListCtrl(self, -1, style=wx.LC_REPORT  | wx.LC_SINGLE_SEL,size=(430, 390))
        self.general_list.InsertColumn(0, "將領", width=60)
        self.general_list.InsertColumn(1, "忠誠", wx.LIST_FORMAT_RIGHT, width=60)
        self.general_list.InsertColumn(2, "才智", wx.LIST_FORMAT_RIGHT, width=40)
        self.general_list.InsertColumn(3, "戰力", wx.LIST_FORMAT_RIGHT, width=40)
        self.general_list.InsertColumn(4, "號召", wx.LIST_FORMAT_RIGHT, width=40)
        self.general_list.InsertColumn(5, "士兵", wx.LIST_FORMAT_RIGHT, width=60)
        self.general_list.InsertColumn(6, "訓練", wx.LIST_FORMAT_RIGHT, width=40)
        self.general_list.InsertColumn(7, "武器", wx.LIST_FORMAT_RIGHT, width=60)


        row = 0
        for gen in self.gen_list:
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

        box_city.Add(self.panel_general, 0)
        box_city.AddSpacer(5)
        box_city.Add(self.general_list, 1)
        box_city.AddSpacer(5)
        self.SetSizer(box_city)
        self.Fit()

        self.general_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnGeneralSelected)

        self.cur_general = 0
        self.general_list.Focus(self.cur_general)
        self.general_list.Select(self.cur_general)


    def OnGeneralPaint(self,e):
        dc = wx.PaintDC(self.panel_general)
        brush = wx.Brush("black")
        dc.SetBackground(brush)
        dc.Clear()

        gen = self.gen_list[self.cur_general]

        index = gen.Portrait
        if index > 218: # RoTK2.MaxNumberOfGenerals:
            RoTK2.DrawGenericFace(dc, index + 1, 20, 45, 80, 96)
        else:
            RoTK2.DrawFace(dc, index, 20, 45, 80, 96)

        font = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        dc.SetFont(font)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.Name), wx.Rect(20, 10, 80, 30), alignment=wx.ALIGN_CENTER)

        start = 130
        starty = 10

        font = wx.Font(14, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        dc.SetFont(font)
        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("年齡", start, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.Age), wx.Rect(start + 50, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("生病", start + 100, starty)
        dc.SetTextForeground(wx.Colour("white"))
        shengbing = "否"
        if gen.IsSick == 1:
            shengbing = "是"
        dc.DrawLabel(shengbing, wx.Rect(start + 150, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("green"))
        dc.DrawText("侍衛", start + 200, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.shiwei), wx.Rect(start + 250, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        starty += 40
        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("義理", start, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.yili), wx.Rect(start + 50, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("仁德", start + 100, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.rende), wx.Rect(start + 150, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("yellow"))
        dc.DrawText("野望", start + 200, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.yewang), wx.Rect(start + 250, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        starty += 40
        dc.SetTextForeground(wx.Colour("cyan"))
        dc.DrawText("相性", start, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.xiangxing), wx.Rect(start + 50, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("cyan"))
        dc.DrawText("兇兆", start + 100, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.WillDieInNextYear), wx.Rect(start + 150, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("cyan"))
        dc.DrawText("血緣", start + 200, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.xueyuan), wx.Rect(start + 250, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        starty += 35
        dc.SetTextForeground(wx.Colour("purple"))
        dc.DrawText("埋伏諸侯", start, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.SpyBlongedToRuler), wx.Rect(start + 50, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("purple"))
        dc.DrawText("埋伏城市", start + 100, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.SpyInCityNo), wx.Rect(start + 150, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        dc.SetTextForeground(wx.Colour("purple"))
        dc.DrawText("內應月數", start + 200, starty)
        dc.SetTextForeground(wx.Colour("white"))
        dc.DrawLabel(str(gen.MonthCannotMove), wx.Rect(start + 250, starty, 30, 20), alignment=wx.ALIGN_RIGHT)

        return

    def OnGeneralSelected(self,e):
        self.cur_general = e.Index

        self.panel_general.Refresh()