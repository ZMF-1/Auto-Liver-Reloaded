import hmac
import hashlib
import tkinter.messagebox
import datetime
import os
import sys
import tkinter.simpledialog
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import requests
import configparser
import re
import json
import tkinter.messagebox

if os.path.exists("C:/alr/cnm.cfg"):
    pass
else:
    tkinter.messagebox.showerror("错误", "用户配置文件不存在")

today = str(datetime.date.today()) + "\n"

if os.path.exists("C:/alr/lived.alr"):
    pass
else:
    with open("C:/alr/lived.alr", "w", encoding="utf-8") as f:
        f.close()
with open("C:/alr/lived.alr", "r", encoding="utf-8") as f:
    dates = f.readlines()
    if today in dates:
        sys.exit(0)

def generate_hmac_sha256(x,uid):
    ey = "d0d3a7342df2026a70f650b907800111"
    key = bytes(ey, 'utf-8')
    message = "app_id=4&channel_id=1&combo_token=" + x + "&open_id=" + uid
    message = bytes(message, 'utf-8')
    hmac_obj = hmac.new(key, message, hashlib.sha256)
    hmac_digest = hmac_obj.digest()
    return hmac_digest.hex()

def request(uid,x,y):
    url = 'https://api-cloudgame.mihoyo.com/hk4e_cg_cn/wallet/wallet/get'

    headers = {
        'X-Rpc-Combo_token': 'ai=4;ci=1;oi='+uid+';ct='+x+';si='+y+';bi=hk4e_cn'
    }
    response = requests.get(url, headers=headers)
    data = response.text
    return data

config = configparser.ConfigParser()
config.read('C:/alr/cnm.cfg',encoding='utf-8')

def jm(z, m):
    with open("pubkey.pem", "rb") as key_file:
        pem_public_key = key_file.read()
    public_key = serialization.load_pem_public_key(pem_public_key)

    message_bytes = z.encode('utf-8')
    message_bytes1 = m.encode('utf-8')

    ciphertext = public_key.encrypt(
        message_bytes,
        padding.PKCS1v15()
    )
    ciphertext1 = public_key.encrypt(
        message_bytes1,
        padding.PKCS1v15()
    )

    base64_encoded = base64.b64encode(ciphertext)
    base64_encoded1 = base64.b64encode(ciphertext1)

    return base64_encoded.decode(), base64_encoded1.decode()

canshu = {}
z = config['mw']['account']
m = config['mw']['password']
canshu['account'] = jm(z, m)[0]
canshu['password'] = jm(z, m)[1]
for key, value in canshu.items():
    config.set('credentials', key, value)
with open('C:/alr/cnm.cfg', 'w', encoding='utf-8') as configfile:
    config.write(configfile)

def login(x, y):
    url = 'https://passport-api.mihoyo.com/account/ma-cn-passport/web/loginByPassword'

    headers = {
        'Host': 'passport-api.mihoyo.com',
        'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'X-Rpc-Device_model': 'Microsoft%20Edge%20124.0.0.0',
        'X-Rpc-Lifecycle_id': '3431892fb5',
        'X-Rpc-Device_os': 'Windows%2010%2064-bit',
        'X-Rpc-Sdk_version': '2.26.0',
        'X-Rpc-Device_name': 'Microsoft%20Edge',
        'X-Rpc-Device_fp': '38d7fa4137750',
        'X-Rpc-Client_type': '22',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'X-Rpc-Game_biz': 'hk4e_cn',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'Content-Type': 'application/json',
        'X-Rpc-Device_id': '003b5c8a-ae14-40c9-8b56-fa7d956d4802',
        'Accept': 'application/json, text/plain, /',
        'X-Rpc-Source': 'v2.webLogin',
        'X-Rpc-App_id': 'c76ync6mutq8'
    }

    data = {
        "account": x,
        "password": y
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.headers['Set-Cookie']
    canshu = ['uni_web_token', 'cookie_token_v2', 'ltoken_v2', 'cookie_token', 'ltoken', 'account_mid_v2']
    cfg = {}
    for key in canshu:
        match = re.search(rf'{key}=([^;]+)', data)
        if match:
            cfg[key] = match.group(1)
    return cfg

account = config['credentials']['account']
password = config['credentials']['password']
q = login(account, password)
for key, value in q.items():
    config.set('cs', key, value)
with open('C:/alr/cnm.cfg', 'w', encoding='utf-8') as configfile:
    config.write(configfile)

def login(uni_web_token, cookie_token_v2, mid, uid, ltoken_v2, cookie_token, ltoken):
    url = 'https://hk4e-sdk.mihoyo.com/hk4e_cn/combo/granter/login/webLogin'

    headers = {
        'Host': 'hk4e-sdk.mihoyo.com',
        'Cookie': 'uni_web_token=' + uni_web_token + '; cookie_token_v2=' + cookie_token_v2 + '; account_mid_v2=' + mid + '; account_id_v2=' + uid + '; ltoken_v2=' + ltoken_v2 + '; ltmid_v2=' + mid + '; ltuid_v2=' + uid + '; cookie_token=' + cookie_token + '; account_id=' + uid + '; ltoken=' + ltoken + '; ltuid=' + uid,
        'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'X-Rpc-Device_model': 'Microsoft%20Edge%20124.0.0.0',
        'X-Rpc-Channel_id': '1',
        'X-Rpc-Device_os': 'Windows%2010%2064-bit',
        'X-Rpc-Mdk_version': '2.24.0',
        'X-Rpc-Device_name': 'Microsoft%20Edge',
        'X-Rpc-Device_fp': '38d7fa4137750',
        'X-Rpc-Client_type': '22',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'X-Rpc-Language': 'zh-cn',
        'X-Rpc-Game_biz': 'hk4e_cn',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'X-Rpc-Device_id': '003b5c8a-ae14-40c9-8b56-fa7d956d4802',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://ys.mihoyo.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ys.mihoyo.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Priority': 'u=1, i',
        'Connection': 'close'
    }

    data = {"app_id": 4, "channel_id": 1}

    response = requests.post(url, headers=headers, json=data)
    data = response.text
    response_data = json.loads(data)
    try:
        combo_token = response_data['data']['combo_token']
    except TypeError:
        combo_token = "0"
    return combo_token

uni_web_token = config['cs']['uni_web_token']
cookie_token_v2 = config['cs']['cookie_token_v2']
ltoken_v2 = config['cs']['ltoken_v2']
cookie_token = config['cs']['cookie_token']
ltoken = config['cs']['ltoken']
mid = config['cs']['account_mid_v2']
uid = config['yx']['uid']
y = 'combo_token'
x = login(uni_web_token, cookie_token_v2, mid, uid, ltoken_v2, cookie_token, ltoken)
if x == "0":
    ret = "\"message\":\"登录已失效，请重新登录\""
else:
    config.set('cs', y, x)
    with open('C:/alr/cnm.cfg', 'w', encoding='utf-8') as configfile:
        config.write(configfile)
    x = config['cs']['combo_token']
    uid = config['yx']['uid']
    y = generate_hmac_sha256(x,uid)
    ret = request(uid,x,y)
if "\"message\":\"OK\"" in ret:
    tkinter.messagebox.showinfo("Auto Liver Reload", "今日已签到!")
    with open("C:/alr/lived.alr", "a", encoding="utf-8") as f:
        f.write(today)
        f.close()
elif "\"message\":\"登录已失效，请重新登录\"" in ret:
    tkinter.messagebox.showerror("Auto Liver Reload", "用户名、密码或米游社通行证ID错误，请重新输入！")
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
    pwd = tkinter.simpledialog.askstring("提示", "请输入你登录云原神用的密码")
    if pwd == None:
        sys.exit(0)
    config.set("mw", "password", pwd)
    with open('C:/alr/cnm.cfg', 'w', encoding='utf-8') as configfile:
        config.write(configfile)
    mid = tkinter.simpledialog.askstring("提示",
                                         "请输入你的米游社通行证ID\n不知道怎么搞?去 https://alr.codete.top/help/01/ 看看吧~")
    if mid == None:
        sys.exit(0)
    config.set("yx", "uid", mid)
    with open('C:/alr/cnm.cfg', 'w', encoding='utf-8') as configfile:
        config.write(configfile)
    python = sys.executable
    os.execl(python, python, *sys.argv)
