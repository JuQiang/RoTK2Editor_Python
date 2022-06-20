from Entity.RoTK2 import RoTK2

class Officer(object):
    #region properties
    Offset = 0
    RulerNo = 0
    Name = ""
    Int = 0
    War = 0
    Chm= 0
    Soldiers= 0
    Arms= 0
    TrainingLevel= 0
    Age= 0
    Loyalty=0
    shiwei= 0
    IsSick= 0
    SickMonth = 0
    yili= 0
    rende= 0
    yewang= 0
    SpyBlongedToRuler= 0
    SpyInCityNo= 0
    xiangxing= 0
    WillDieInNextYear= 0
    CanMoveNow= 0
    MonthCannotMove= 0
    xueyuan= 0
    NextOfficerOffset= 0
    Portrait = 0
    IsUnClaimed=False
    IsFree=False
    # endregion properties

    OfficerList = []

    @staticmethod
    def GetName(name1, name2, name3, name4, name5, name6):
        name_list = {0xaba6: "劉", 0xab9f: "備", 0xFB92: "公", 0x309B: "孫", 0xBBAE: "瓚", 0xBCA1: "越", 0xEA9C: "馬",
                     0xD5AD: "騰",0xD0A4:"廖",0x46A8:"賢",0x669E:"淳",0xCDAC:"瓊",0x4A94:"仲",0xD7A5:"興",0xD998:"姜",0xC3A5:"維",0xF7A7:"誕",0x949E:"爽",
                     0x8D98: "候", 0xD8A9: "選", 0x32A1: "程", 0x6DA6: "銀",0xD2AA:"禅",0x509B:"師",
                     0x59AD: "關", 0xD094: "羽", 0xAE9D: "張", 0x9A9A: "飛",0x8B98:"信",
                     0X989F: "陶", 0X65AB: "謙", 0XF09C: "乾",
                     0X949F: "陳", 0XF3A0: "登", 0XDCAA: "糜", 0X3998: "竺",
                     0X5398: "芳",
                     0XAF9C: "袁", 0X4A9F: "術", 0X479A: "胤", 0XF899: "紀",
                     0XF0AE: "靈", 0X56A7: "樂", 0XF29F: "就", 0XB9A8: "動",
                     0X949F: "陳", 0X31AE: "蘭", 0XD695: "李", 0X58AC: "豐",
                     0X74A4: "雷", 0X41AB: "薄", 0X6E9D: "堅",
                     0X77A0: "普", 0X42A1: "策", 0X36A2: "黃", 0XE3A5: "蓋",

                     0XA6AB: "韓", 0X4BA3: "當", 0XD2D4: "闞", 0X41A9: "澤",
                     0XB694: "朱", 0XD897: "治", 0X399E: "曹", 0XE6A8: "操",
                     0X369B: "宮", 0X42A1: "策", 0XED9A: "夏", 0X8D98: "侯",
                     0X789E: "淵", 0XCF9D: "惇", 0X9C99: "洪", 0X9C97: "昂",
                     0XED92: "仁", 0XCFA1: "進", 0X619C: "純", 0X6C98: "表",

                     0X6AC6: "蒯", 0X5696: "良", 0X8AA2: "嵩",
                     0X36A2: "黃", 0X439C: "祖", 0XDAA7: "蔡", 0XA298: "冒",
                     0X9B95: "宋", 0X5697: "忠", 0X6EA8: "鄧", 0X99A3: "義",
                     0X6293: "文", 0X9DA3: "聘", 0XA3A7: "磐", 0X6495: "呂",
                     0XFB92: "公", 0X909E: "焉", 0X85AD: "嚴", 0X8EAC: "顏",
                     0X6295: "吳", 0X81AE: "懿", 0X4C94: "任", 0XB9A3: "董",
                     0XCE96: "和", 0XB7A1: "貴", 0X74A4: "雷", 0X6D94: "同",
                     0X88A7: "璋", 0X4695: "冷", 0X629A: "苞", 0XEC9C: "高", 0XEB95: "沛", 0XCDA2: "楊", 0XB4AC: "懷",
                     0XD49E: "紹", 0XEF93: "田", 0X76A5: "熙", 0XFDAC: "譚", 0XFD96: "尚", 0X879F: "郭", 0XB6A4: "圖",
                     0X8DA2: "幹",
                     0X39AE: "覽", 0XCFA0: "焦", 0XBCAD: "觸",
                     0XCFA6: "審", 0XD89C: "配", 0XE5CD: "嶷", 0XD397: "沮", 0XE59D: "受", 0X89A8: "震", 0X4D97: "延",
                     0X8CAB: "醜",
                     0X829F: "逢", 0XB696: "卓", 0XF1A3: "賈",
                     0X6AC3: "詡", 0XCB93: "布", 0X7AA1: "華", 0XF3A1: "雄", 0XAFA8: "儒", 0X64A1: "肅", 0X54A7: "樊",
                     0X81A3: "稠",
                     0X439A: "胡", 0XECBF: "軫",
                     0X579B: "徐", 0X39A5: "榮", 0XDAB0: "汜", 0X39B3: "旻", 0XA3AA: "濟", 0X33AC: "繍", 0XB5BC: "傕",
                     0XF0A3: "資",
                     0X4DA6: "趙", 0XA395: "岑", 0X7A93: "王",
                     0X979B: "朗", 0XBDA3: "虞", 0X38AC: "翻", 0XC5CE: "繇", 0X4A93: "太", 0XB793: "史", 0X96A2: "慈",
                     0X579A: "英",
                     0XBC97: "武",
                     0X97AC: "馥", 0X75A7: "潘", 0X9BA6: "鳳", 0X6C96: "辛", 0XA2A1: "評", 0X8A9A: "郃", 0XC09C: "豹",
                     0X4C93: "孔",
                     0XADA9: "融", 0X9994: "安", 0X6B9D: "國",
                     0X439E: "梁", 0XCA9A: "剛", 0XF7A1: "雲", 0XDF96: "奉", 0X8F9B: "晃", 0XF5AA: "翼", 0XDAA9: "遼",
                     0XC7A2: "楷",
                     0XD59C: "郝", 0X85A1: "萌", 0X589F: "許",
                     0X9CAC: "魏", 0XFCAD: "續", 0XA894: "成", 0XD3A8: "憲", 0X6BAC: "邈", 0XFAA1: "順", 0XA09C: "荀",
                     0XFCB6: "彧",
                     0XD295: "攸", 0XACA4: "嘉", 0X649B: "恩", 0X7199: "昱",
                     0XA796: "典", 0X959A: "韋", 0X81AA: "懋", 0XCBAA: "矯", 0XC7A6: "嬉", 0X95AB: "鐘", 0XAEA9: "衡",
                     0XBDA1: "超", 0X4DAE: "鐵", 0XA894: "成", 0XFA96: "宜", 0XF6A8: "橫", 0X3897: "岱", 0XB1AC: "龐",
                     0XE0A6: "德",
                     0X9CA9: "興", 0XF197: "玩", 0XF099: "秋", 0XB5A0: "湛",
                     0XF792: "允", 0XD196: "周", 0X4AA3: "瑜", 0XDFA5: "蒙", 0XD196: "周", 0XB89B: "泰", 0XA292: "丁",
                     0XDF96: "奉",
                     0XA6A8: "魯", 0XEEA9: "閻", 0XE69A: "圃", 0XEBA7: "衛",
                     0XCC93: "平", 0XB397: "松", 0X8A99: "柏", 0XB5A1: "費", 0XDCA3: "詩", 0X83AE: "權", 0XDA9E: "累",
                     0X5694: "全",
                     0X9FBE: "琮", 0XD2A0: "然", 0XAEA7: "範", 0X57AE: "顧",
                     0X70A4: "雍", 0X959F: "陸", 0XE3AA: "績", 0XAB9E: "巽", 0XE295: "步", 0XEDD6: "騭？", 0X9C9B: "桓",
                     0X959F: "陸", 0X57A6: "遜", 0XBABB: "翊", 0X97B8: "纮", 0X6B99: "昭",
                     0X92AE: "襲", 0XF898: "度", 0XE09B: "珪", 0XE6A0: "琦", 0XD29E: "統", 0XBE9A: "倉", 0XFBAB: "簡",
                     0XC49A: "淩",
                     0XD498: "奕", 0X64A5: "滿",
                     0XFCA5: "褚", 0XB293: "司", 0X4894: "休", 0X96D3: "顗", 0XB198: "南", 0XB9AC: "曠", 0X5AA1: "翔",
                     0X77C1: "楙",
                     0X53AE: "霸", 0X7893: "牛", 0X7698: "金", 0XB99A: "修", 0X4E9D: "商", 0XDA95: "杜", 0XA59D: "常",
                     0XF79B: "真", 0X739F: "通", 0XF998: "建", 0XAA9F: "傅", 0XBF92: "于", 0X77A3: "禁", 0XA49C: "虔",
                     0XD9A7: "蔣",
                     0XB1A0: "渠", 0X309E: "旋", 0X8EA8: "鞏", 0XB495: "志", 0X4C9A: "範", 0X78AA: "應",
                     0X4BAA: "鮑", 0X54AA: "龍", 0X7496: "刑", 0X42A4: "道", 0XE793: "玄", 0XE0AD: "齡", 0X7799: "柔",
                     0XF9A7: "諸",
                     0XB5A3: "葛", 0X8A98: "亮", 0XEB98: "封", 0XDCA6: "廣", 0X5A9C: "索", 0X36A0: "循", 0XA0BE: "琬",
                     0X6F9B: "拳", 0X8AA7: "瑾", 0XEB93: "甘", 0XCEA4: "寧", 0X3598: "秉", 0XF796: "宗", 0X7197: "承",
                     0XEAA2: "溫",
                     0X47AB: "薛", 0XB6A5: "綜", 0XEBD5: "騭", 0XE3A4: "彰", 0X8293: "丕", 0X99A0: "植", 0X9BA3: "群",
                     0X6F93: "毛", 0XACB3: "玠", 0XE398: "威", 0XEFA8: "曄", 0XC79B: "浩", 0XAB9D: "庶", 0X6794: "匡",
                     0X67B5: "毘",
                     0X9CC1: "歆", 0XF496: "孟", 0XBCAA: "獲", 0XB8D1: "闿", 0X56AA: "優",
                     0XB794: "朵", 0X3799: "思", 0X8098: "阿", 0XC3A2: "會", 0XBEAA: "環", 0X4EA1: "結", 0XF896: "定",
                     0X3695: "余",
                     0XC293: "奴", 0XB0BE: "畯", 0X69AB: "謝", 0X319E: "旌",
                     0XA5CA: "鲂", 0XB59E: "盛", 0X4294: "伉", 0XB29F: "凱", 0XDC9B: "班", 0X5498: "芝", 0XCD97: "法",
                     0XDE93: "正",
                     0XC3C5: "祎", 0XF6A9: "霍", 0X479B: "峻", 0X44A4: "達",
                     0XD0AC: "疆", 0XE0A4: "廖", 0X3693: "化", 0X879E: "淮", 0X43A0: "惠", 0X6ACF: "謖", 0XB0AC: "寵",
                     0XA194: "式",
                     0X37AF: "觀", 0X4494: "伊", 0XA5AD: "籍",
                     0XC892: "士", 0XAAAA: "濬", 0X6998: "虎", 0XA2A0: "欽", 0X9AC2: "粲", 0XCCA1: "逵", 0XF0AB: "禮",
                     0XAE95: "彤",
                     0XE592: "之", 0X78A4: "靖", 0X4B99: "恪",
                     0XDF93: "母", 0X8493: "丘", 0XA6A6: "儉", 0XE394: "艾", 0XC5CA: "叡", 0x4699: "恢", 0xE692: "尹", 0x52AA: "默",
                     0x5193: "巴",0xA0A6: "儀", 0x85AC: "双", 0x82A1: "著",0xE695:"沙",0xF6A6:"摩",0xAA93:"可",0xEFA7:"褒",0x43A4:"遂",0xEEA8:"暹"
                     }

        name1_1 = name1>>8
        name1_2 = name1 & 0xff
        name2_1 = name2>>8
        name2_2 = name2 & 0xff
        name3_1 = name3>>8
        name3_2 = name3 & 0xff
        name4_1 = name4 >> 8
        name4_2 = name4 & 0xff
        name5_1 = name5 >> 8
        name5_2 = name5 & 0xff
        name6_1 = name6 >> 8
        name6_2 = name6 & 0xff


        if name1+name2+name3+name4+name5+name6==0:
            return ""

        if  name1_1<0x80 and name1_2<0x80 and name2_1<0x80 and name2_2<0x80 and name3_1<0x80 and name3_2<0x80 and name4_1<0x80 and name4_2<0x80 and name5_1<0x80 and name5_2<0x80 and name6_1<0x80 and name6_2<0x80:
            name = chr(name1_2)+chr(name1_1)+chr(name2_2)+chr(name2_1)+chr(name3_2)+chr(name3_1)+chr(name4_2)+chr(name4_1)+chr(name5_2)+chr(name5_1)+chr(name6_2)+chr(name6_1)
            return name.replace("\0","")

        name = ""
        if name_list.__contains__(name1):
            name += name_list[name1]
        else:
            name += "0X{0:X}".format(name1)

        if name2 > 0:
            if name_list.__contains__(name2):
                name += name_list[name2]
            else:
                name += "0X{0:X}".format(name2)

        if name3 > 0:
            if name_list.__contains__(name3):
                name += name_list[name3]
            else:
                name += "0X{0:X}".format(name3)

        if name4 > 0:
            if name_list.__contains__(name4):
                name += name_list[name4]
            else:
                name += "0X{0:X}".format(name4)
        if name5 > 0:
            if name_list.__contains__(name5):
                name += name_list[name5]
            else:
                name += "0X{0:X}".format(name5)
        if name6 > 0:
            if name_list.__contains__(name6):
                name += name_list[name6]
            else:
                name += "0X{0:X}".format(name6)

        return name

    @staticmethod
    def GetList():
        pos = 0x20
        size = 0x2b

        gen_no = 0

        while True:
            tmp = Officer.GetOfficerFromBuffer(RoTK2.SaveData[pos + size * gen_no:pos + size * gen_no + size], gen_no, pos, size, RoTK2.SaveData[0x0d] * 256 + RoTK2.SaveData[0x0c])
            tmp.OfficerList.append(tmp)

            gen_no += 1
            if gen_no > RoTK2.MaxNumberOfGenerals:
                break

        empty_officer = Officer()
        empty_officer.Offset = -56
        empty_officer.name = ""

        empty_king = Officer()
        empty_king.Offset = 255
        empty_king.name = ""

        Officer.OfficerList.append(empty_officer)
        Officer.OfficerList.append(empty_king)

    @staticmethod
    def GetOfficerFromBuffer(buffer, gen_no, pos, size, year):
        o = Officer()
        o.Offset = pos + size * gen_no
        o.NextOfficerOffset = (buffer[0x01] << 8) + buffer[0x00] - 0x38
        o.RulerNo = buffer[0x0A]
        o.Name = o.GetName((buffer[0x1D] << 8) + buffer[0x1C], (buffer[0x1F] << 8) + buffer[0x1E], (buffer[0x21] << 8) + buffer[0x20],
                           (buffer[0x23] << 8) + buffer[0x22], (buffer[0x25] << 8) + buffer[0x24], (buffer[0x27] << 8) + buffer[0x26]
                           )
        o.Int = buffer[0x04]
        o.War = buffer[0x05]
        o.Chm = buffer[0x06]
        o.Loyalty = buffer[0x0B]
        o.Soldiers = (buffer[0x13] << 8) + buffer[0x12]
        o.Arms = (buffer[0x15] << 8) + buffer[0x14]
        o.TrainingLevel = buffer[0x16]
        o.Age = year - buffer[0x19] + 1
        o.shiwei = buffer[0x0C]
        o.IsSick = buffer[0x03]
        o.SickMonth = buffer[0x03] & 0x0f
        o.yili = buffer[0x07]
        o.rende = buffer[0x08]
        o.yewang = buffer[0x09]
        o.SpyBlongedToRuler = buffer[0x0D]
        o.SpyInCityNo = buffer[0x0E]
        o.xiangxing = buffer[0x0F]
        o.WillDieInNextYear = buffer[0x02] >> 4
        o.CanMoveNow = buffer[0x02] & 0x0f
        o.MonthCannotMove = buffer[0x03] >> 4
        o.xueyuan = (buffer[0x11] << 8) + buffer[0x10]
        o.Portrait = (buffer[0x1B] << 8) + buffer[0x1A] - 1
        return o

    @staticmethod
    def GetOfficerByOffset(offset):
        if len(Officer.OfficerList)==0:
            Officer.GetList()

        ret = None

        for o in Officer.OfficerList:
            if o.Offset == offset:
                ret = o
                break

        return ret

    @staticmethod
    def GetStoredOfficerList(seq):
        gamedata = bytearray(RoTK2.SCENARIO)
        size = 0x2b

        pos_list = [0x16,0x33c5,0x6774,0x9b23,0xced2,0x10281]
        year_list = [189,194,201,208,215,220]
        pos = pos_list[seq]
        #for pos in pos_list:
        gen_no = 0
        gen_list = []

        while True:
            gen = gamedata[pos + size * gen_no:pos + size * gen_no + size]
            tmp = Officer.GetOfficerFromBuffer(gen, gen_no, pos, size, year_list[seq])

            gen_no += 1

            if tmp.Int==0 and tmp.War==0 and tmp.Chm==0:
                break

            gen_list.append(tmp)

            gen_no += 1

        print("===============================================")

        return gen_list

    @staticmethod
    def get_taiki_gen_list():
        gamedata = RoTK2.TAIKI
        size = 0x2E

        pos = 0
        gen_no = 0
        gen_list = []

        while True:
            if pos + size * gen_no+9>len(gamedata):
                break
            gen = gamedata[pos + size * gen_no+3:pos + size * gen_no + size]
            tmp = Officer.GetOfficerFromBuffer(gen, gen_no, pos, size, 220)

            if tmp.Int==0 and tmp.War==0 and tmp.Chm==0:
                break

            gen_list.append(tmp)

            gen_no += 1

        print("===============================================")

        return gen_list