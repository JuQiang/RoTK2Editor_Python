from Entity.Officer import Officer
from Entity.RoTK2 import RoTK2
import struct

class Province(object):
    # region properties
    No = 0#从1开始
    Offset = 0
    NextProvince = 0
    RulerNo  = 0
    WarRulerNo = 0
    Governor = 0
    UnClaimedOfficer = 0
    FreeOfficer = 0
    DelegateControl = ""
    ProvinceSendGoods= ""
    ProvinceInvade= ""
    Gold = 0
    Rice = 0
    Population = 0
    Land = 0
    PeopleLoyalty = 0
    FloodControl = 0
    Horses = 0
    Cost = 0
    RicePrice = 0
    Name= ""
    # endregion properties

    CityList = []
    OfficerList = []

    @staticmethod
    def GetList():
        if len(Province.CityList)>0:
            return Province.CityList

        Officer.OfficerList = []
        start = 0x2d8c
        size = 0x23

        city_names = ["幽州", "幷州", "冀州", "青州", "兗州", "司州", "雍州", "涼州", "徐州", "予州", "荊州", "揚州", "益州", "交州"]

        for i in range(0, 41):
            tmp = Province()
            tmp.OfficerList = []
            city_data = RoTK2.SaveData[start + i * size:start + i * size + size]

            next_city, jiang, zaiye, xinren, jin, liang, ren, zhuhou, zhanzheng, daili, zhanzhengjun, yunshujun, dijia, minzhong, zhishui, liangju, chengbao, mijia, x, y, name_index = struct.unpack(
                "<HHHHHLHBBBxBBBBBBBBxxxxBBB", city_data)

            tmp.No = RoTK2.MapIndex[y][x]
            tmp.Name = city_names[name_index] + "-" + str(tmp.No)
            tmp.Offset = start + i * size
            tmp.NextProvince = next_city
            tmp.RulerNo = zhuhou

            tmp.WarRulerNo = zhanzheng

            tmp.Governor = jiang - 0x38
            tmp.UnClaimedOfficer = zaiye - 0x38
            tmp.FreeOfficer = xinren - 0x38

            daili_mappings = {0: "",3:"未知", 4: "全权", 5: "内政", 6: "军事", 7: "人事"}
            if daili < 8:
                tmp.DelegateControl = daili_mappings[daili]

            if yunshujun < 41:
                name_index = RoTK2.SaveData[start + size * yunshujun + size - 1]
                tmp.ProvinceSendGoods = city_names[name_index] + "-" + str(yunshujun + 1)
            if zhanzhengjun < 41:
                name_index = RoTK2.SaveData[start + size * zhanzhengjun + size - 1]
                tmp.ProvinceInvade = city_names[zhanzhengjun] + "-" + str(zhanzhengjun + 1)

            tmp.Gold = jin
            tmp.Rice = liang
            tmp.Population = ren * 100
            tmp.Land = dijia
            tmp.PeopleLoyalty = minzhong
            tmp.FloodControl = zhishui
            tmp.Horses = liangju
            tmp.Cost = chengbao
            tmp.RicePrice = mijia

            next = jiang - 0x38
            while next > 0:
                gen = Officer.GetOfficerByOffset(next)
                tmp.OfficerList.append(gen)
                next = gen.NextOfficerOffset

            if tmp.UnClaimedOfficer>0:
                gen = Officer.GetOfficerByOffset(tmp.UnClaimedOfficer)
                gen.IsUnClaimed = True
                tmp.OfficerList.append(gen)
                next = gen.NextOfficerOffset
                while next>0:
                    gen = Officer.GetOfficerByOffset(next)
                    gen.IsUnClaimed = True
                    tmp.OfficerList.append(gen)
                    next = gen.NextOfficerOffset

            if tmp.FreeOfficer>0:
                gen = Officer.GetOfficerByOffset(tmp.FreeOfficer)
                gen.IsFree = True
                tmp.OfficerList.append(gen)

                next = gen.NextOfficerOffset
                while next > 0:
                    gen = Officer.GetOfficerByOffset(next)
                    gen.IsFree = True
                    tmp.OfficerList.append(gen)
                    next = gen.NextOfficerOffset

            Province.CityList.append(tmp)

        return Province.CityList

    @staticmethod
    def GetCityByOffset(offset):
        ret = None

        for c in Province.GetList():
            if c.Offset == offset:
                ret = c
                break

        return ret