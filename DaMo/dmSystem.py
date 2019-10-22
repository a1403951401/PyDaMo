from DaMo.func import debug_P, DeBugMod

# 系统相关
class System:
    dm = None

    """
        检测系统是否开启平滑字体
        True    系统没开启平滑字体
        False   系统有开启平滑字体
    """
    @DeBugMod
    def CheckFontSmooth(self):
        return self.dm.CheckFontSmooth()
