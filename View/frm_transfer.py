#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter as tk
"""
program name :
last modification time :
changelog :
"""


class PageTransfer(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        转账页面

        :param master: 上层容器
        :param kwargs: config, height, width
        """
        # 建立框架本体
        super().__init__(master, height=kwargs["height"] if "height" in kwargs else None,
                         width=kwargs["width"] if "width" in kwargs else None)
        self.config = kwargs["config"]
        # 建立框架内容
        # 导入图片  预留：读取配置
        self.page_home_bg = tk.PhotoImage(file="%spage_count_bg.png" % self.config["image_path"])  # 背景路径
        self.image_button1 = tk.PhotoImage(file="%sbutton2.png" % self.config["image_path"])
        self.image_label = tk.PhotoImage(file="%scount_label_bg.png" % self.config["image_path"])
        # 图片载体 框架靠此Label控制大小位置
        self.stage = tk.Label(self, height=kwargs["height"], width=kwargs["width"],
                              compound=tk.CENTER, image=self.page_home_bg)
        self.stage.pack()

        lb1 = tk.Label(self.stage,
                       text="卡号：%s     账户余额 ¥：%.2f" % (kwargs["card"].card_id, kwargs["card"].money),
                       compound=tk.CENTER, image=self.image_label,
                       font=("宋体", 18),
                       width=690,
                       height=30,
                       fg="red",
                       anchor="center")
        lb1.place(x=0, y=20)

        lb2 = tk.Label(self.stage,
                       text="对方卡号",
                       compound=tk.CENTER, image=self.image_button1,
                       font=self.config["font"],
                       fg="white",
                       width=80,
                       height=30,
                       anchor="center")
        lb2.place(x=160, y=100)

        e1 = tk.Entry(self.stage, font=self.config["font"], bd=4, width=20)
        e1.place(x=260, y=105)

        lb3 = tk.Label(self.stage,
                       text="输入金额：",
                       compound=tk.CENTER, image=self.image_button1,
                       font=self.config["font"],
                       fg="white",
                       width=80,
                       height=30,
                       anchor="center")
        lb3.place(x=160, y=200)

        e2 = tk.Entry(self.stage, font=self.config["font"],bd=4,width=20)
        e2.place(x=260, y=205)


        bt1 = tk.Button(self.stage,
                        text="确认转账", width=170, height=30,fg="white", font=self.config["font"],
                        compound=tk.CENTER, image=self.image_button1)
        bt1.place(x=270, y=300)
        bt1.bind("<Button-1>",
                 lambda event: kwargs["fnc1"](e1.get(), e2.get()))


