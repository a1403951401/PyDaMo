def debug_P(txt, debug, more = ""):
    if debug:
        if more:
            print(f"[{more}] {txt}")
        else:
            print(txt)

def DeBugMod(func):
    def DeBug(*arg, **kwargs):
        req = func(*arg, **kwargs)
        debug_P(req, arg[0].debug, func.__name__)
        return req
    return DeBug
