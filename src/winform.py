#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

import histsimilar
import screencapture

win = tk.Tk()
win.title("ScreenCapture")    # 添加标题

def clickMe():   # 当acction被点击时,该函数则生效
    screencapture.main()

action = ttk.Button(win, text="抓图", command=clickMe)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=0, row=0)

def clickMe2():   # 当acction被点击时,该函数则生效
    histsimilar.handleImage()

action = ttk.Button(win, text="处理", command=clickMe2)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=0)

win.mainloop()      # 当调用mainloop()时,窗口才会显示出来

