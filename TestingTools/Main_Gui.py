#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @FileName  :Main_Gui.py
# @Time      :2024/08/07 23:03:47
# @Author    :Styx

import tkinter

class mainGui(object):
    def __init__(self, init_window_name) -> None:
        self.init_window_name = init_window_name
    
    def set_GUi(self):
        self.init_window_name.title('Test Tools')  ##设置标题
        self.init_window_name.geometry('1240x800+200+200')  ##设置窗口默认大小


if __name__ == "__main__":
    main_GUI = tkinter.Tk()  ##实例化窗口
    set_Tools_GUI = mainGui(main_GUI)  ##对实例进行通用GUI的设置
    set_Tools_GUI.set_GUi()
    main_GUI.mainloop()  ##运行窗口事件

    