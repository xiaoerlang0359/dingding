import win32gui as wgui
import pyautogui as pgui
import os
from shutil import copyfile
import time


# mkdir
def mydown_load(num):
    path = "E:\\assignment\\"
    for i in range(1, num + 1):
        file_name = path + str(i)
        os.mkdir(file_name)
    # first
    for i in range(1, num + 1):
        pgui.click(1068, 452, interval=2)
        window = wgui.GetWindowText(wgui.FindWindow("DingImgViewWnd", None))
        left, top, right, bottom = wgui.GetWindowRect(wgui.FindWindow("DingImgViewWnd", None))
        down_load_pos = [right - 150, top + 25]
        next_pos = [right - 67, top + 55 + (bottom - (top + 55)) / 2]
        close_pos = [right - 20, top + 25]
        last = "0"
        ii = str(i)
        pre_addr = ["E:/assignment/", "\n"]
        addr = ii.join(pre_addr)
        while last != window:
            last = window
# 下载
            pgui.click(down_load_pos, interval=2.5)
# 输入地址
            left, top, right, bottom = wgui.GetWindowRect(wgui.FindWindow(None, "另存为"))
            addr_pos = [left + 391, top + 45]
            save_pos = [right - 179, bottom - 38]
            pgui.click(addr_pos, interval=0.5)
            pgui.typewrite(message=addr, interval=0.1)
# 保存
            pgui.click(save_pos, interval=0.8)
# next picture
            pgui.click(next_pos, interval=1.5)
            window = wgui.GetWindowText(wgui.FindWindow("DingImgViewWnd", None))
        pgui.click(close_pos, interval=1.5)
# next assignmet
        pgui.click(1209, 600, interval=1.5)


def up_load(num):
    path = "E:\\assignment\\"
    destpath = "E:\\upload\\"
    for i in range(1, num + 1):
        dir_name = path + str(i)
        length = 0
        mylist = []
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                if os.path.splitext(file)[1] == '.jpg':
                    mylist.append(os.path.join(root, file))
                    length = length + 1
# copy file
        for j in range(0, length):
            joinstr = [destpath, ".jpg"]
            destfile = str(j+1).join(joinstr)
            copyfile(mylist[j], destfile)
        pgui.click(1185, 685, interval=0.5)
# 点击批改
# 点击相册
        pgui.click(908, 546, interval=1)
        upmultfile = ""
        for j in range(1, length + 1):
            upfile = "\"" + str(j) + ".jpg\""
            if j != 1:
                upmultfile = upmultfile + " " + upfile
            else:
                upmultfile = upfile
        upmultfile = upmultfile + '\n'
        pgui.typewrite(message=upmultfile, interval=0.1)
        time.sleep(12)
        left, top, right, bottom = wgui.GetWindowRect(wgui.FindWindow("PopupFrame", None))
# 点击确定
        myyes_pos = [right-76, bottom-30]
        pgui.click(myyes_pos, interval=0.8)
# 点击提交g" "4.jp
        pgui.click(1185, 685, interval=1)
# 点击下一个
        pgui.click(1209, 600, interval=1.2)
# delete file
        deletepath = "E:\\upload"
        for k in os.listdir(deletepath):
            file_name = deletepath + "\\" + k
            os.remove(file_name)


up_load(19)



