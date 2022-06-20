import wx

class SelectKingWindow(wx.Dialog):
    def __init__(self, ruler_list,cur_zhuhou):
        wx.Dialog.__init__(self,None,-1,'选择诸侯', style=wx.CLOSE_BOX|wx.BORDER_NONE)
        # self.ruler_offset = -1
        # self.ruler_no = 0xff
        self.ruler_list = ruler_list

        id = 1001
        index = 0
        rb_list = []
        self.selected_ruler = None

        index2 = 0

        for name in ruler_list:
            rb = wx.RadioButton(self, id + index, label=ruler_list[index].RulerSelf.Name, pos=(30, 10 + 30 * index))
            if ruler_list[index].RulerSelf.Name==cur_zhuhou:
                rb.SetValue(True)
                self.selected_ruler = ruler_list[index]
                #self.ruler_offset = self.ruler_list[index].ruler_self.offset
            index += 1

        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)

        self.btnOk = wx.Button(self,201,label="OK",pos=(30,10+30*index))
        self.btnOk.Bind(wx.EVT_BUTTON,self.OnButtonClicked)

        self.SetSize(size=(150,10+30*index+50+10))

        self.name_list = ruler_list
        self.Centre()


    def OnRadiogroup(self,e):
        self.selected_ruler= self.ruler_list[e.Id - 1001]

    def OnButtonClicked(self,e):
        self.Close()