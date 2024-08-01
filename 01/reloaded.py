import os
import sys
import tkinter.simpledialog, tkinter.messagebox
import configparser
import shutil
import urllib.request

confTXT = "[mw]\naccount = \npassword = \n\n[yx]\nuid = \n\n[credentials]\naccount = \npassword = \n\n[cs]\nuni_web_token = \ncookie_token_v2 = \nltoken_v2 = \ncookie_token = \nltoken = \ncombo_token = \naccount_mid_v2 = \n\n"
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
if os.path.exists("C:/alr/cnm.cfg"):
    pass
else:
    with open("C:/alr/cnm.cfg", "w+", encoding="utf-8") as conf:
        conf.write(confTXT)
        conf.close()
config = configparser.ConfigParser()
config.read('C:/alr/cnm.cfg', encoding='utf-8')
if config["mw"]["account"] == "":
    while True:
        acc = tkinter.simpledialog.askstring("提示", "请输入你登录云原神用的手机号")
        if acc == None:
            sys.exit(0)
        try:
            int(acc)
        except:
            tkinter.messagebox.showerror("错误", "请输入正确格式的手机号")
        else:
            if len(acc) == 11:
                break
            else:
                tkinter.messagebox.showerror("错误", "请输入正确格式的手机号")
    config.set("mw", "account", acc)
    with open('C:/alr/cnm.cfg', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

if config["mw"]["password"] == "":
    pwd = tkinter.simpledialog.askstring("提示", "请输入你登录云原神用的密码")
    if pwd == None:
        sys.exit(0)
    config.set("mw", "password", pwd)
    with open('C:/alr/cnm.cfg', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

if config["yx"]["uid"] == "":
    mid = tkinter.simpledialog.askstring("提示", "请输入你的米游社通行证ID\n不知道怎么搞?去 https://alr.codete.top/help/ 看看吧~")
    if mid == None:
        sys.exit(0)
    config.set("yx", "uid", mid)
    with open('C:/alr/cnm.cfg', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

if os.path.exists("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/ysautorun.exe"):
    pass
else:
    urllib.request.urlretrieve("https://alr.codete.top/sources/ysautorun.exe", "ysautorun.exe")
    shutil.move("ysautorun.exe", "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/ysautorun.exe")
if os.path.exists("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/pubkey.pem"):
    pass
else:
    urllib.request.urlretrieve("https://alr.codete.top/sources/pubkey.pem", "pubkey.pem")
    shutil.move("pubkey.pem", "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/pubkey.pem")
tkinter.messagebox.showinfo("提示", "电脑启动项已添加完成!")
os.chdir("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp")
os.system("\"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/ysautorun.exe\"")