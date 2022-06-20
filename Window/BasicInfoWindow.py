import wx

class BasicInfoWindow(wx.Dialog):
    x = 10
    y = 10
    width = 60
    height = 20

    def __init__(self,parent,id,ruler_list):
        wx.Frame.__init__(self,parent,id,'信任、同盟与敌对度', style=wx.CLOSE_BOX|wx.BORDER_NONE)

        self.ruler_list = ruler_list
        self.SetSize((len(ruler_list)+2)*self.width+2*self.x,(len(ruler_list)+3)*self.height+1*self.y)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Centre()
        self.Show()

    def OnPaint(self,e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("white")
        dc.SetBackground(brush)
        dc.Clear()


        ruler_num = len(self.ruler_list)
        for i in range(0,ruler_num+2):
            dc.DrawLine(self.x,self.y+i*self.height,self.x+(ruler_num+2)*self.width,self.y+i*self.height)
        for i in range(0, ruler_num + 3):
            dc.DrawLine(self.x+i*self.width,self.y,self.x+i*self.width,self.y+(ruler_num+1)*self.height)

        default_pen = wx.Pen(wx.Colour("black"))
        dc.SetPen(default_pen)

        dc.DrawLabel("信任度",wx.Rect(self.x+self.width, self.y, self.width, self.height),alignment=wx.ALIGN_CENTER)
        for i in range(0,ruler_num):
            dc.DrawLabel(self.ruler_list[i].RulerSelf.Name, wx.Rect(self.x, self.y + self.height * 1 + self.height * i, self.width, self.height), alignment=wx.ALIGN_CENTER)

        for i in range(0,ruler_num):
            dc.DrawLabel(self.ruler_list[i].RulerSelf.Name, wx.Rect(self.x + self.width * 2 + self.width * i, self.y, self.width, self.height), alignment=wx.ALIGN_CENTER)

        for i in range(0,ruler_num):
            dc.SetTextForeground(wx.Colour("black"))
            dc.DrawLabel(str(self.ruler_list[i].TrustRating), wx.Rect(self.x + self.width * 1, self.y + self.height * 1 + i * self.height, self.width, self.height), alignment=wx.ALIGN_CENTER)

            for j in range(0,ruler_num):
                info = self.ruler_list[i].RelationShips[self.ruler_list[j].No]
                jiemeng = ""
                if info[0]=="1":
                    jiemeng = "✓"
                    dc.SetTextForeground(wx.Colour("green"))
                else:
                    dc.SetTextForeground(wx.Colour("black"))

                if i!=j:
                    #dc.DrawLabel(jiemeng,wx.Rect(self.x + self.width * 2 + self.width * j, self.y+self.height*2+i*self.height, self.width/2, self.height),alignment=wx.ALIGN_CENTER)
                    dc.DrawLabel(str(info[1]), wx.Rect(self.x + self.width * 2 + self.width * j,self.y + self.height * 1 + i * self.height, self.width,self.height), alignment=wx.ALIGN_CENTER)