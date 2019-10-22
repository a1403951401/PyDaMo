from DaMo.func import debug_P, DeBugMod

# 图色相关
class Pic:
    dm = None

    # 截图
    @DeBugMod
    def Capture(self, file, x1=0, y1=0, x2=2000, y2=2000):
        return self.dm.Capture(x1, y1, x2, y2, file)

    """ 在指定区域查找图片
    sim           相似度
    delta_color   色偏
    dir           查找方向
    查找成功返回 x, y 坐标 ，失败返回 False
    """
    @DeBugMod
    def FindPic(self, pic_name, x1 = 0, y1 = 0, x2 = 2000, y2 = 2000, sim=0.9, delta_color="", dir = 0):
        x, y = None, None
        pic = self.dm.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, x, y)
        if pic[0] == -1:
            return False
        else:
            return pic[1], pic[2]

    """
    找图并点击
    sim           相似度
    delta_color   色偏
    dir           查找方向
    查找成功返回 x, y 坐标 ，失败返回 False
    """
    @DeBugMod
    def FindPicClick(self, pic_name, x1 = 0, y1 = 0, x2 = 2000, y2 = 2000, sim=0.9, delta_color="", dir = 0):
        pic = self.dm.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir, None, None)
        if pic:
            self.MouseClick(pic[0], pic[1])
            return True
        return False