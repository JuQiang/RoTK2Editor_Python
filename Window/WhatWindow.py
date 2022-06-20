import wx
import Entity
from Entity.RoTK2 import RoTK2

class WhatWindow(wx.Dialog):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1, size=(415,428),style=wx.CLOSE_BOX|wx.BORDER_NONE)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Centre()
        self.Show()

    def OnPaint(self,e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("black")
        dc.SetBackground(brush)
        dc.Clear()

        RoTK2.draw_what(dc, 0, 5, 5, 100, 100)