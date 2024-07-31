"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import sys

# 示例下载 https://www.pytk.net/blog/1702564569.html
import ui
import tkinter.messagebox
class Controller:
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO的 组件初始化 赋值操作
    def win_about(self):
        tkinter.messagebox.showinfo("关于", "Auto Liver Reloaded\n作者: 蜜蜂不想蜇人了\n本软件开源，遵循GPLv3协议\n如有bug，请反馈至github或发送邮件至CodeteMail@163.com\n本软件禁止用于任何非法或商业用途！")
    def win_exit(self):
        a = tkinter.messagebox.askyesno("退出", "确定要退出吗？")
        if a:
            sys.exit(0)
