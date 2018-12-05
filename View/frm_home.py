#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter as tk
"""
program name :
last modification time :
changelog :
"""


class PageHome(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        开机后的主界面
        功能：(登录)、(解锁)、(开户)、(重置密码) 括号代表另一界面

        :param master: 上层容器
        :param kwargs: config, height, width
        """
        # 建立框架本体
        super().__init__(master, height=kwargs["height"] if "height" in kwargs else None,
                         width=kwargs["width"] if "width" in kwargs else None)
        self.config = kwargs["config"]
        # 建立框架内容
        # 导入图片  预留：读取配置
        self.page_home_bg = tk.PhotoImage(file="%spage_home_bg.png" % self.config["image_path"])  # 背景路径
        self.image_button2 = tk.PhotoImage(file="%sbutton2.png" % self.config["image_path"])
        # 框架载体 框架靠此Label控制大小位置
        self.stage = tk.Label(self, height=kwargs["height"], width=kwargs["width"],
                              compound=tk.CENTER, image=self.page_home_bg)
        self.stage.pack()
        # 框架内容
        lb1 = tk.Label(self.stage,
                       text="卡号",
                       font=self.config["font"],
                       image=self.image_button2,
                       width=50,
                       height=20,
                       fg = "white",
                       compound=tk.CENTER,
                       anchor="center"

                       )
        lb1.place(x=330, y=200)
        e1 = tk.Entry(self.stage, font=self.config["font"],bd=4,width=20,fg="orange")
        e1.place(x=400, y=200)
        lb2 = tk.Label(self.stage,
                       text="密码",
                       font=self.config["font"],
                       image=self.image_button2,
                       width=50,
                       height=20,
                       fg="white",
                       compound=tk.CENTER,
                       anchor="center")
        lb2.place(x=330, y=270)
        e2 = tk.Entry(self.stage, font=self.config["font"],bd=4,width=20,fg="orange",show="*")
        e2.place(x=400, y=270)

        bt1 = tk.Button(self.stage,
                        text="登录系统",
                        fg = "white",
                        image=self.image_button2, compound=tk.CENTER,
                        font=self.config["font"],
                        width=170, height=35)
        bt1.place(x=410, y=370)
        bt1.bind("<Button-1>",
                 lambda event: kwargs["fnc1"](e1.get(), e2.get()))

