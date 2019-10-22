# 请求错误的类型
class VIP_Err(Exception):
    code = {
        -1: "无法连接网络, (可能防火墙拦截, 如果可以正常访问大漠插件网站，那就可以肯定是被防火墙拦截)",
        -2: "进程没有以管理员方式运行.(出现在win7 win8 vista 2008.建议关闭uac)",
        0: "失败(未知错误)",
        1: "大漠注册成功",
        2: "余额不足",
        3: "绑定了本机器，但是账户余额不足50元.",
        4: "注册码错误",
        5: "你的机器或者IP在黑名单列表中或者不在白名单列表中",
        6: "非法使用插件",
        7: "你的帐号因为非法使用被封禁. （如果是在虚拟机中使用插件，必须使用Reg或者RegEx，不能使用RegNoMac或者RegExNoMac, 否则可能会造成封号，或者封禁机器）",
        8: "ver_info不在你设置的附加白名单中",
        77: "机器码或者IP因为非法使用，而被封禁. （如果是在虚拟机中使用插件，必须使用Reg或者RegEx，不能使用RegNoMac或者RegExNoMac, 否则可能会造成封号，或者封禁机器）封禁是全局的，如果使用了别人的软件导致77，也一样会导致所有注册码均无法注册。解决办法是更换IP，更换MAC",
        -8: "版本附加信息长度超过了20",
        -9: "版本附加信息里包含了非法字母",
    }

    def __init__(self, messge):
        if messge in self.code:
            self.leng = self.code[messge]
        else:
            self.leng = messge

    def __str__(self):
        return self.leng
