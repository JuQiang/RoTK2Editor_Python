import wx

class MapWindow(wx.Dialog):
    def __init__(self,parent,id,title,map_data):
        wx.Frame.__init__(self,parent,id,title, size=(415,428),style=wx.CLOSE_BOX|wx.BORDER_NONE)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.map_data = map_data
        self.Centre()
        self.Show()

    def OnPaint(self,e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("black")
        dc.SetBackground(brush)
        dc.Clear()

        x = 0
        y = 0
        start = 0
        for r in range(0, 12):
            for c in range(0, 13):
                fname = "Images/hex{0:02}.jpg".format(self.map_data[start])
                #print("City {0}, r={1} c={2}, file {3}".format(self.cur_city, r, c, fname))
                dc.DrawBitmap(wx.Bitmap(fname), x + c * 32, y + r * 32 + (c % 2) * 16, True)
                start += 1