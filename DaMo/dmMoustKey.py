from DaMo.func import debug_P, DeBugMod

# 系统相关
class System:
    dm = None
    hwnd = None
    """
    鼠标点击指定坐标
        坐标    x, y
        鼠标类型  0 鼠标左键  1 鼠标右键  2 鼠标中键  type1
        点击类型  0 单击      1 按下      2 弹起      type2
    """
    @DeBugMod
    def MouseClick(self, x, y, type1=0, type2=0):
        mouse = {
            "00":self.dm.LeftClick, "01":self.dm.LeftDown, "02":self.dm.LeftUp,
            "10":self.dm.RightClick, "11":self.dm.RightDown, "12":self.dm.RightUp,
            "20":self.dm.MiddleClick, "21":self.dm.MiddleDown, "22":self.dm.MiddleUp,
        }
        type = f"{type1}{type2}"
        if type in mouse:
            self.dm.MoveTo(x, y)
            return mouse[type]()
        return False

    """
    按下鼠标并且拖动
    """
    @DeBugMod
    def MouseDrag(self, x1, y1, x2, y2):
        self.dm.MoveTo(x1, y1)
        self.dm.LeftDown()
        self.dm.MoveTo(x2, y2)
        self.dm.LeftUp()

    # 键盘点击事件
    # 点击类型  0 单击      1 按下      2 弹起       type
    @DeBugMod
    def KeyClick(self, keynumber, type):
        key = {
            0:self.dm.KeyPress,
            1:self.dm.KeyDown,
            2:self.dm.KeyUp,
        }
        if type in key:
            return key[type](keynumber)
        return False

    # 大漠方法下的 输入文本
    @DeBugMod
    def SendString(self, String, hwnd = None):
        if not hwnd:
            hwnd = self.hwnd
        return self.dm.SendString(hwnd, String)