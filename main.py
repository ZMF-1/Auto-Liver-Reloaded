"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
# 导入布局文件
from ui import Win as MainWin
# 导入窗口控制器
from control import Controller as MainUIController
import os, sys
import tkinter.messagebox
import requests
# 将窗口控制器 传递给UI
app = MainWin(MainUIController())
def restart():
  python = sys.executable
  os.execl(python, python, * sys.argv)
if __name__ == "__main__":
    # 启动
    if requests.get("https://alr.codete.top/info").text == "uploaded":
        tkinter.messagebox.showinfo("提示", "检测到软件更新，请前往https://alr.codete.top/download.html下载最新版本！")
    def setNote(path):
        with open(path + "note.txt", "w+", encoding="utf-8") as note:
            note.write("本目录由Auto Liver Reload生成，请勿手动修改或删除")
            note.close()
    if os.path.exists("C:/alr/"):
        if os.path.isdir("C:/alr/"):
            pass
        else:
            os.mkdir("C:/alr/")
    else:
        os.mkdir("C:/alr/")
    setNote("C:/alr/")
    app.mainloop()
    a = tkinter.messagebox.askyesno("退出", "确定要退出吗？")
    if a:
        sys.exit(0)
    else:
        restart()
