# coding:utf-8

import pyHook
import pythoncom
from PIL import ImageGrab
import os,ctypes

global num
num = 0
Lcontrol_press = False
Q_press = False



def onMouseLeftDownEvent(event):
    saveImage()
    return True

def onMouseLeftDblEvent(event):
    saveImage()
    return True

def onMouseWheelEvent(event):
    saveImage()
    return True

def onMouseRightDownEvent(event):
    saveImage()
    return True

def onMouseRightDblEvent(event):
    saveImage()
    return True

def onMouseMiddleDownEvent(event):
    ctypes.windll.user32.PostQuitMessage(0)
    return True

def onKeyboardEvent(event):
    global Lcontrol_press
    global Q_press
    saveImage()
    return True

def saveImage():
    global num
    im = ImageGrab.grab()
    im.save("image/"+str(num) + ".jpg")
    print("图片："+ str(num) + ".jpg保存成功")
    num = num + 1

def main():
    createPath()

    # 创建一个：钩子“管理对象
    hm = pyHook.HookManager()

    # 监听鼠标左键单击事件
    hm.MouseLeftDown = onMouseLeftDownEvent
    # 监听鼠标左键双击事件
    hm.MouseLeftDbl = onMouseLeftDblEvent
    # 监听鼠标右键单击事件
    hm.MouseRightDown = onMouseRightDownEvent
    # 监听鼠标右键双击事件
    hm.MouseRightDbl = onMouseRightDblEvent
    # 监听鼠标滚轮事件
    hm.MouseWheel = onMouseWheelEvent
    # 监听鼠标滚轮点击事件
    hm.MouseMiddleDown = onMouseMiddleDownEvent

    # 设置鼠标钩子
    hm.HookMouse()

    # 监听所有的键盘事件
    hm.KeyDown = onKeyboardEvent
    #设置键盘”钩子“
    hm.HookKeyboard()

    # 进入循环侦听，需要手动进行关闭，否则程序将一直处于监听的状态。可以直接设置而空而使用默认值
    pythoncom.PumpMessages()

    hm.UnhookMouse()
    hm.UnhookKeyboard()

    print("")
    print("The end of Mouse and KBD test!")
    print("")

def createPath():
    if(os.path.exists(os.getcwd()+'/image') == False):
        os.mkdir(os.getcwd()+'/image')

if __name__ == "__main__":
    main()
