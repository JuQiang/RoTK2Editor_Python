import wx
from Entity.RoTK2 import RoTK2

class WorldMapWindow(wx.Dialog):
    def __init__(self,parent,id):
        wx.Dialog.__init__(self,parent,id,"世界地图", size=(int(13*32*8/(32/8)),int(12*32*9/(32/8))+32),style=wx.CLOSE_BOX|wx.BORDER_NONE)
        #self.map_panel = wx.lib.scrolledpanel.ScrolledPanel(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.worldmap_data = []

        for i in range(0, 41):
            map_data = RoTK2.HEXDATA[156 * i:156 * i + 12 * 13]
            self.worldmap_data.append(map_data)

        self.Centre()
        self.Show()

    def OnPaint(self,e):
        new_dc = wx.PaintDC(self)
        #brush = wx.Brush("black")
        #new_dc.SetBackground(brush)
        #new_dc.Clear()

        x = 0
        y = 0
        width = 8
        height = 8

        dc = wx.MemoryDC()

        whole_picture = wx.Bitmap(13*32*8,12*32*9)
        dc.SelectObject(whole_picture)
        cached_images = {}
        indexes = [0,1,2,3,4,5,6,9,99]

        for index in indexes:
            fname = "images/hex{0:02}.jpg".format(index)
            bmp = wx.Image(fname)
            bmp.Rescale(width, height)
            cached_images[index] = bmp.ConvertToBitmap()

        for i in range(0,9):
            for j in range(0,8):
                if RoTK2.MapIndex[i][j]==0:
                    continue

                start = 0
                map_data = self.worldmap_data[RoTK2.MapIndex[i][j] - 1]
                for r in range(0, 12):
                    for c in range(0, 13):
                        dc.DrawBitmap(cached_images[map_data[start]],13*width*j+ x + c * width, 12*height*i+ y+int((j%2)*12*height/2) + r * height + int((c % 2) * height/2), True)
                        start += 1

        new_dc.Blit(0,0,whole_picture.Width,whole_picture.Height,dc,0,0)
        #whole_picture.SaveFile("worldmap.bmp",wx.BITMAP_TYPE_BMP)