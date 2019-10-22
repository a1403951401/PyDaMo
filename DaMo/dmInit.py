from time import time
from ctypes import WinDLL
from win32com.client import Dispatch

from DaMo.err import VIP_Err
from DaMo.func import debug_P, DeBugMod

# 各种不同的包
from DaMo.dmWindows import Windows
from DaMo.dmSystem import System
from DaMo.dmPic import Pic

class DaMo(Windows, System, Pic):
    # 需要传入 大漠dll 以及 大漠免注册
    def __init__(self, dmdll, dmReg, VIP = "", debug = False):
        self.VIP = False
        self.debug = debug
        if debug:
            now = time()
        # 注册 大漠 DLL
        self.__Reg(dmdll, dmReg)
        # 注册 大漠 VIP
        self.__VIP(VIP)
        if debug:
            debug_P(f"大漠 初始化完成，总耗时 {round(time() - now, 2)} 秒",self.debug)

    # 注册大漠的方法
    def __Reg(self, dmdll, dmReg, dmclassname = 'dm.dmsoft'):
        dll = WinDLL(dmReg)
        dll.SetDllPathW(dmdll, 0)
        self.dm = Dispatch(dmclassname)
        debug_P("注册 大漠 成功",self.debug)

    # 注册大漠VIP的方法
    def __VIP(self, VIP):
        if VIP:
            req = self.dm.Reg(VIP, "")
            if req == (1 or 3):
                self.VIP = True
            else:
                raise VIP_Err(req)
        debug_P("注册 大漠VIP 成功",self.debug)

    # 获取大漠版本编号
    @DeBugMod
    def Ver(self):
        return self.dm.Ver()

