import configparser
import os
import wx

class RoTK2(object):
    GamePath = ""
    SaveData = None
    KAODATA = None
    MONTAGE = None
    HEXDATA = None
    GRPDATA = None
    TAIKI = None
    SCENARIO = None
    MaxNumberOfGenerals = 255

    SettingsFileName = "settings.txt"

    @staticmethod
    def HasGamePath():
        ret = True

        conf = configparser.ConfigParser()
        conf.read(RoTK2.SettingsFileName, encoding="utf-8")
        if conf.has_section("General") is False:
            return False

        RoTK2.GamePath = conf.get("General", "GamePath")

        flist = ["KAODATA.DAT","MONTAGE.DAT","HEXDATA.DAT","GRPDATA.DAT","TAIKI.DAT","SCENARIO.DAT"]
        for f in flist:
            if os.path.exists(RoTK2.GamePath+f) is False:
                ret = False
                break

        return ret

    @staticmethod
    def Init():
        f = open(RoTK2.GamePath + "kaodata.dat", "rb")
        tmp_buf = f.read(210240)
        f.close()
        RoTK2.KAODATA = bytearray(tmp_buf)

        f = open(RoTK2.GamePath + "montage.dat", "rb")
        tmp_buf = f.read(50688)
        f.close()
        RoTK2.MONTAGE = bytearray(tmp_buf)

        f = open(RoTK2.GamePath+"scenario.dat", "rb")
        tmp_buf = f.read(79386)
        f.close()
        RoTK2.SCENARIO = bytearray(tmp_buf)

        f=open(RoTK2.GamePath+"taiki.dat","rb")
        f.seek(0x06)
        tmp_buf = f.read(19326)
        f.close()
        RoTK2.TAIKI = bytearray(tmp_buf)

        f = open(RoTK2.GamePath+"hexdata.dat", "rb")
        tmp_buf = f.read(15108)
        f.close()
        RoTK2.HEXDATA = bytearray(tmp_buf)

        f = open(RoTK2.GamePath+"grpdata.dat", "rb")
        tmp_buf = f.read(46715)
        f.close()
        RoTK2.GRPDATA = bytearray(tmp_buf)
    #RulerNumber = sg2.gamedata[0x0f]
    MapIndex = [[0, 0, 0, 0, 0, 2, 1, 0],
                [0, 0, 0, 4, 3, 6, 0, 0],
                [0, 0, 0, 5, 7, 9, 8, 0],
                [15, 0, 0, 11, 10, 17, 16, 24],
                [14, 13, 12, 20, 19, 28, 18, 25],
                [0, 30, 29, 31, 21, 22, 27, 26],
                [0, 33, 32, 40, 23, 38, 37,0],
                [0, 35, 34, 41, 39, 0, 0, 0],
                [0, 0, 36, 0, 0, 0, 0, 0]]

    @staticmethod
    def draw_what(dc,index,x,y,new_width,new_height):
        face_buf = []
        start = 0x37b2
        width = 0x128
        height = 0xc8
        size = int(width*height/8*3)
        face = RoTK2.GRPDATA[start + index * size:start + (index + 1) * size]


        for i in range(0,len(face),3):
            a = "{0:b}".format(face[i+0]).zfill(8)
            b = "{0:b}".format(face[i+1]).zfill(8)
            c = "{0:b}".format(face[i+2]).zfill(8)
            for j in range(0,8):
                face_buf.append(int(a[j]+b[j]+c[j],2))

        #http://xycq.online/forum/redirect.php?tid=34607&goto=lastpost&highlight=
        #上面link的描述严重错误！顺序是RBG，而不是BGR，更不是RGB！
        colors = [wx.Colour("#000000"), wx.Colour("#50ff50"), wx.Colour("#ff5050"), wx.Colour("#ffff50"),
                  wx.Colour("#5050f8"), wx.Colour("#50fff8"), wx.Colour("#ff50f8"), wx.Colour("#fffff8")]

        loc = 0
        img = wx.Image(width,height,8)
        for i in range(0,height):
            for j in range(0,width):
                if face_buf[width*i+j]==0:
                    continue
                true_color = colors[face_buf[width*i+j]]
                #img.SetRGB(j,i,true_color.red,true_color.green,true_color.blue)
                img.SetRGB(loc%width, loc/width, true_color.red, true_color.green, true_color.blue)
                loc += 1

        img.Rescale(width*2,height*2)
        dc.DrawBitmap(img.ConvertToBitmap(),x,y)
    @staticmethod
    def DrawFace(dc, index, x, y, new_width, new_height):
        face_buf = []
        face = RoTK2.KAODATA[index * 960:index * 960 + 960]
        for i in range(0,len(face),3):
            a = "{0:b}".format(face[i+0]).zfill(8)
            b = "{0:b}".format(face[i+1]).zfill(8)
            c = "{0:b}".format(face[i+2]).zfill(8)
            for j in range(0,8):
                face_buf.append(int(a[j]+b[j]+c[j],2))

        #http://xycq.online/forum/redirect.php?tid=34607&goto=lastpost&highlight=
        #上面link的描述严重错误！顺序是RBG，而不是BGR，更不是RGB！
        colors = [wx.Colour("#000000"), wx.Colour("#50ff50"), wx.Colour("#ff5050"), wx.Colour("#ffff50"),
                  wx.Colour("#5050f8"), wx.Colour("#50fff8"), wx.Colour("#ff50f8"), wx.Colour("#fffff8")]

        img = wx.Image(64,40,8)
        for i in range(0,40):
            for j in range(0,64):
                #if face_buf[64*i+j]>7:
                #print("{0},{1}".format(i,j))
                true_color = colors[face_buf[64*i+j]]
                img.SetRGB(j,i,true_color.red,true_color.green,true_color.blue)

        img.Rescale(new_width,new_height)
        dc.DrawBitmap(img.ConvertToBitmap(),x,y)

    @staticmethod
    def DrawGenericFace(dc, index, x, y, new_width, new_height):
        info = "{0:b}".format(index).zfill(16)
        wenxu = int(info[0:3],2)#100武将，110文官
        kou = int(info[3:5],2)
        bi = int(info[5:7],2)
        yan = int(info[7:9],2)
        shang = int(info[9:11],2)
        xia = int(info[11:13],2)
        group = int(info[13:16], 2)

        width = 64
        size = int(width*(18*4+22*4+8*4+10*4+8*4)*3/8)

        height_list = [18,22,8,10,8]
        face_data=[]
        face = RoTK2.MONTAGE[group * size:group * size + size]

        pos = 0
        for h in height_list:
            for k in range(0,4):
                block_size = int(width*h*3/8)

                face_buf=[]
                for i in range(0, block_size, 3):
                    a = "{0:b}".format(face[i + 0+pos]).zfill(8)
                    b = "{0:b}".format(face[i + 1+pos]).zfill(8)
                    c = "{0:b}".format(face[i + 2+pos]).zfill(8)
                    for j in range(0, 8):
                        face_buf.append(int(a[j] + b[j] + c[j], 2))

                face_data.append(face_buf)
                pos += block_size

        colors = [wx.Colour("#000000"), wx.Colour("#50ff50"), wx.Colour("#ff5050"), wx.Colour("#ffff50"),
                  wx.Colour("#5050f8"), wx.Colour("#50fff8"), wx.Colour("#ff50f8"), wx.Colour("#fffff8")]


        img = wx.Image(64, 40, 8)
        pos_list = [shang,4+xia,8+kou,12+bi,16+yan]
        s = 0
        # for i in range(0, 66):
        #     for k in range(0,len(height_list)):
        #         for j in range(0, height_list[k]):
        #             print("{}:{},{},{},{},{}".format(i+s,s,i,k,j,len(height_list)))
        #             true_color = colors[face_data[pos_list[k]][height_list[k] * i + j]]
        #             img.SetRGB(j+s, i, true_color.red, true_color.green, true_color.blue)
        #
        #         s += height_list[k]

        for i in range(0,18):
            for j in range(0, 64):
                true_color = colors[face_data[shang][64 * i + j]]
                img.SetRGB(j, i, true_color.red, true_color.green, true_color.blue)

        for i in range(0,22):
            for j in range(0, 64):
                true_color = colors[face_data[4+xia][64 * i + j]]
                img.SetRGB(j, i+18, true_color.red, true_color.green, true_color.blue)

        for i in range(0,8):
            for j in range(0, 64):
                true_color = colors[face_data[8+yan][64 * i + j]]
                if true_color.red == 0 and true_color.green == 0 and true_color.blue == 0:
                    continue
                img.SetRGB(j, i+10, true_color.red, true_color.green, true_color.blue)

        for i in range(0,8):
            for j in range(0, 64):
                true_color = colors[face_data[16+bi][64 * i + j]]
                if true_color.red==0 and true_color.green==0 and true_color.blue==0:
                    continue
                img.SetRGB(j, i+16, true_color.red, true_color.green, true_color.blue)

        for i in range(0,10):
            for j in range(0, 64):
                true_color = colors[face_data[12+kou][64 * i + j]]
                if true_color.red == 0 and true_color.green == 0 and true_color.blue == 0:
                    continue
                img.SetRGB(j, i+22, true_color.red, true_color.green, true_color.blue)

        img.Rescale(new_width,new_height)
        dc.DrawBitmap(img.ConvertToBitmap(), x, y)
        return