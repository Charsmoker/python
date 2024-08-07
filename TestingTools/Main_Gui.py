#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @FileName  :Main_Gui.py
# @Time      :2024/08/07 23:03:47
# @Author    :Styx

import tkinter

class mainGui(object):
    def __init__(self, name) -> None:
        self.name = name
    
    def set_GUi(self):
        self.geometry = '800x500-100+200'


if __name__ == "__main__":
    main_GUI = tkinter.Tk()
    mainGui(main_GUI)
    main_GUI.mainloop()

    