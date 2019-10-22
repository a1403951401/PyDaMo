from DaMo import DaMo

if __name__ == '__main__':
    dm = DaMo(
        dmReg='C:/源码/Script/DLL/DmReg.dll',             # 免注册dll
        dmdll = 'C:/源码/Script/DLL/dm.dll',              # 大漠dll 本体
        VIP='key的内容',                                  # 是否注册 VIP
        debug = True                                      # 是否开启 debug 模式
    )
    dm.Ver()
    dm.CheckFontSmooth()
    dm.Capture(r"C:\Users\Martin\Desktop\1.bmp")