"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import os
import random
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import urllib.request

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_lzawnls8 = self.__tk_label_lzawnls8(self)
        self.sb1 = self.tk_select_box_lzawspad = self.__tk_select_box_lzawspad(self)
        self.tk_button_lzawt4z3 = self.__tk_button_lzawt4z3(self)
    def __win(self):
        self.title("Auto Liver Reloaded By 蜜蜂不想蜇人了")
        # 设置窗口大小、居中
        width = 400
        height = 300
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_label_lzawnls8(self,parent):
        label = Label(parent,text="签到类型选择",anchor="center", )
        label.place(x=165, y=5, width=87, height=50)
        return label
    def __tk_select_box_lzawspad(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("米游社每日签到奖励","云原神每日签到奖励","森空岛每日签到奖励"," 库街区每日签到奖励")
        cb.place(x=73, y=73, width=267, height=30)
        return cb
    def __tk_button_lzawt4z3(self,parent):
        btn = Button(parent, text="确认！！！！", takefocus=False, command=self.cmd)
        btn.place(x=102, y=142, width=226, height=108)
        return btn

    def cmd(self):
        user = self.sb1.get()
        if user == "云原神每日签到奖励":
            if os.path.exists("C:/alr/ysset.exe"):
                pass
            else:
                tkinter.messagebox.showinfo("提示", "即将下载云原神每日签到奖励脚本，按确定后请稍等！")
                urllib.request.urlretrieve("https://alr.codete.top/sources/ysset.exe", "C:/alr/ysset.exe")
            os.system("start C:/alr/ysset.exe")
        else:
            tkinter.messagebox.showinfo("提示", "功能尚未开发完整，请关注bilibili@蜜蜂不想蜇人了")

class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.config(menu=self.create_menu())
        self.ctl.init(self)
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_command(label="About",command=self.ctl.win_about)
        menu.add_command(label="EXIT",command=self.ctl.win_exit)
        return menu
    def __event_bind(self):
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()