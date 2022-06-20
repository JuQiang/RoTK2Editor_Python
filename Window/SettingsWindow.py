import wx
import configparser
from Entity.RoTK2 import RoTK2

class SettingsWindow(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self,None,-1,'设置', style=wx.CLOSE_BOX|wx.BORDER_NONE,size=(400,100))

        self.conf = configparser.ConfigParser()
        self.conf.read(RoTK2.SettingsFileName,encoding="utf-8")
        if self.conf.has_section("General") is False:
            self.conf.add_section("General")
            self.conf.set("General", "GamePath", "")
        RoTK2.GamePath = self.conf.get("General", "GamePath")

        self.labelPath = wx.StaticText(self,label="游戏目录：",pos=(10,12))
        self.textPath = wx.TextCtrl(self, value = RoTK2.GamePath, pos=(80, 10), size=(200, 24))
        self.btnBrowse = wx.Button(self, label="...", pos=(290, 10),size=(32,24))
        self.btnOk = wx.Button(self,label="OK",pos=(10,50))
        self.btnCancel = wx.Button(self, label="Cancel", pos=(110, 50))

        self.btnBrowse.Bind(wx.EVT_BUTTON,self.OnBrowseDirector)
        self.btnOk.Bind(wx.EVT_BUTTON,self.OnOkClicked)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnCancelClicked)

        self.Centre()

    def OnBrowseDirector(self,e):
        dlg = wx.DirDialog(self,"选择三国志2游戏所在目录",self.textPath.Value)
        #id = dlg.ShowModal()
        if dlg.ShowModal() == wx.ID_OK:
            self.textPath.Value = dlg.Path
            if self.textPath.Value[-1] != "/":
                self.textPath.Value += "/"


    def OnOkClicked(self,e):
        self.conf.set("General","GamePath",self.textPath.Value)
        self.conf.write(open(RoTK2.SettingsFileName,"w",encoding="utf-8"))
        self.Close()
    def OnCancelClicked(self,e):
        self.Close()