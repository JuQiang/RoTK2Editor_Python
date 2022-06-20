from Entity.Province import Province
from Entity.RoTK2 import RoTK2
from Entity.Officer import Officer

class Ruler(object):
    #region properties
    RulerSelf = None
    HomeCity = None
    Advisor = None
    No = 0xff
    TrustRating = 0
    RelationShips = {}
    # region properties

    RulerList = []
    CityList = []

    @staticmethod
    def GetList():
        if len(Ruler.RulerList)>0:
            return Ruler.RulerList

        Province.CityList = []
        ruler_num = RoTK2.SaveData[0x0f]
        start = 0x2afc
        size = 0x29

        for i in range(0,16):
            ruler_offset = (RoTK2.SaveData[start + i * size + 1] << 8) + RoTK2.SaveData[start + i * size + 0] - 0x38
            if ruler_offset<0:
                continue
            ruler_city_offset = (RoTK2.SaveData[start + i * size + 3] << 8) + RoTK2.SaveData[start + i * size + 2] - 0x38
            aa_offset = (RoTK2.SaveData[start + i * size + 5] << 8) + RoTK2.SaveData[start + i * size + 4] - 0x38
            relationships_data = "{0:b}".format(RoTK2.SaveData[start + i * size + 0x0A]).zfill(8)[::-1] + "{0:b}".format(RoTK2.SaveData[start + i * size + 0x0B]).zfill(8)[::-1]

            k = Ruler()
            k.No = i
            k.RulerSelf = Officer.GetOfficerByOffset(ruler_offset)
            if ruler_city_offset>-1:#君主可能流浪了
                k.HomeCity = Province.GetCityByOffset(ruler_city_offset)
            if aa_offset>-1:#君主可能流浪了
                k.Advisor = Officer.GetOfficerByOffset(aa_offset)
            k.TrustRating = RoTK2.SaveData[start + i * size + 6]

            k.RelationShips = {}
            for j in range(0, 16):
                #key:   Alliance
                #value: Hostility
                k.RelationShips[j] =[relationships_data[j], RoTK2.SaveData[start + j * size + 0x0e + i]]

            Ruler.RulerList.append(k)

        return Ruler.RulerList

    @staticmethod
    def GetRulerByNo(no):
        if no==0xff:
            k = Ruler()
            k.RulerSelf = Officer()
            k.No = no
            k.RulerSelf.name = ""

            return k

        ret = None
        for k in Ruler.RulerList:
            if k.No == no:
                ret = k
                break

        return ret

    def GetCityList(self):
        self.CityList.clear()

        for c in Province.GetList():
            if c.RulerNo == self.No:
                self.CityList.append(c)

        return self.CityList