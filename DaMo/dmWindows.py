from DaMo.func import debug_P, DeBugMod

# 窗口相关
class Windows:
    dm = None

    # 根据标题查找句柄
    @DeBugMod
    def FindWindow(self, Class = "", Title = "", Parent = 0):
        return self.dm.FindWindowEx(Parent, Class, Title)

    # 根据句柄绑定窗口      并将句柄保存到类中
    @DeBugMod
    def BindWindow(self, hwnd, display = "gdi", mouse = "windows", keypad = "windows", mode = 0):
        self.hwnd = hwnd
        return self.dm.BindWindow(hwnd, display, mouse, keypad, mode)