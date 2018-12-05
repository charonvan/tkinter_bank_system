#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter as tk
"""
program name :
last modification time :
changelog :
"""


class PageAccess(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        存取款页面

        :param master: 上层容器
        :param kwargs: config, height, width
        """
        # 建立框架本体
        super().__init__(master, height=kwargs["height"] if "height" in kwargs else None,
                         width=kwargs["width"] if "width" in kwargs else None)
        self.config = kwargs["config"]

        self.entry_text1 = tk.Variable()
        # 建立框架内容
        # 导入图片  预留：读取配置
        self.OptionType = kwargs["OptionType"]
        self.Button_text1 = tk.StringVar() #根据OptionTYpe判断显示的文字
        if self.OptionType == 1:
            self.Button_text1.set("确认存款")
        else:
            self.Button_text1.set("确认取款")
        self.page_home_bg = tk.PhotoImage(file="%spage_count_bg.png" % self.config["image_path"])  # 背景路径
        self.image_label =  tk.PhotoImage(file="%scount_label_bg.png" % self.config["image_path"])
        self.image_button1 = tk.PhotoImage(file="%sbutton2.png" % self.config["image_path"])
        # 图片载体 框架靠此Label控制大小位置
        self.stage = tk.Label(self, height=kwargs["height"], width=kwargs["width"],
                              compound=tk.CENTER, image=self.page_home_bg)
        self.stage.pack()

        lb1 = tk.Label(self.stage,
                       text="卡号：%s     账户余额 ¥：%.2f" % (kwargs["card"].card_id, kwargs["card"].money),
                       compound=tk.CENTER, image=self.image_label,
                       font=("宋体",18),
                       width = 690,
                       height = 30,
                       fg="red",
                       anchor="center")
        lb1.place(x=0, y=20)

        lb2 = tk.Label(self.stage,
                       text="输入金额:",
                       compound=tk.CENTER, image=self.image_button1,
                       font=self.config["font"],
                       width=85,
                       height=30,
                       fg = "white",
                       anchor="center")
        lb2.place(x=115, y=80)

        e1 = tk.Entry(self.stage,textvariable=self.entry_text1, font=self.config["font"],bd=5,width=26)
        e1.place(x=220, y=85)

        btc1 = tk.Button(self.stage,text="1",
                        compound=tk.CENTER, image=self.image_button1,
                        font=self.config["font"],
                        fg="white",
                        width=50, height=50)
        btc2 = tk.Button(self.stage, text="2",
                         compound=tk.CENTER, image=self.image_button1,
                         font=self.config["font"],
                         fg="white",
                         width=50, height=50)
        btc3 = tk.Button(self.stage, text="3",
                         compound=tk.CENTER, image=self.image_button1,
                         font=self.config["font"],
                         fg="white",
                         width=50, height=50)
        btc4 = tk.Button(self.stage, text="删除",
                         compound=tk.CENTER, image=self.image_button1,
                         font=("宋体", 12),
                         fg="white",
                         width=50, height=50)
        btc5 = tk.Button(self.stage, text="4",
                         compound=tk.CENTER, image=self.image_button1,
                         font=self.config["font"],
                         fg="white",
                         width=50, height=50)
        btc6 = tk.Button(self.stage, text="5",
                         compound=tk.CENTER, image=self.image_button1,
                         font=self.config["font"],
                         fg="white",
                         width=50, height=50)
        btc7 = tk.Button(self.stage, text="6",
                         compound=tk.CENTER, image=self.image_button1,
                         font=self.config["font"],
                         fg="white",
                         width=50, height=50)
        btc8 = tk.Button(self.stage, text="0",
                         compound=tk.CENTER, image=self.image_button1,
                         font=self.config["font"],
                         fg="white",
                         width=50, height=50)
        btc9 = tk.Button(self.stage, text="7",
                         compound=tk.CENTER, image=self.image_button1,
                         font=self.config["font"],
                         fg="white",
                         width=50, height=50)
        btc10 = tk.Button(self.stage, text="8",
                         compound=tk.CENTER, image=self.image_button1,
                         font=self.config["font"],
                         fg="white",
                         width=50, height=50)
        btc11 = tk.Button(self.stage, text="9",
                         compound=tk.CENTER, image=self.image_button1,
                         font=self.config["font"],
                         fg="white",
                         width=50, height=50)
        btc12 = tk.Button(self.stage, text="全删",fg="white",
                         compound=tk.CENTER, image=self.image_button1,
                         font=("宋体",12),
                         width=50, height=50)




        btc1.place(x=250, y=160)
        btc2.place(x=300, y=160)
        btc3.place(x=350, y=160)
        btc4.place(x=400, y=160)

        btc5.place(x=250, y=210)
        btc6.place(x=300, y=210)
        btc7.place(x=350, y=210)
        btc8.place(x=400, y=210)

        btc9.place(x=250, y=260)
        btc10.place(x=300, y=260)
        btc11.place(x=350, y=260)
        btc12.place(x=400, y=260)




        bt1 = tk.Button(self.stage,
                        text=self.Button_text1.get(),
                        compound=tk.CENTER, image=self.image_button1,
                        font=self.config["font"],
                        width=200, height=30,fg="white")
        bt1.place(x=250, y=350)

        btc1.bind("<Button-1>",lambda event: self.entry_text1.set(self.entry_text1.get()+"1"))
        btc2.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get() + "2"))
        btc3.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get() + "3"))
        btc4.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get()[:-1]))
        btc5.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get() + "4"))
        btc6.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get() + "5"))
        btc7.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get() + "6"))
        btc8.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get() + "0"))
        btc9.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get() + "7"))
        btc10.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get() + "8"))
        btc11.bind("<Button-1>", lambda event: self.entry_text1.set(self.entry_text1.get() + "9"))
        btc12.bind("<Button-1>", lambda event: self.entry_text1.set(""))

        if self.OptionType == 1:  #绑定存款事件，绑定存款事件
            bt1.bind("<Button-1>",
                     lambda event: kwargs["fnc1"](kwargs["card"].card_id, e1.get(), 1))
        else:
            bt1.bind("<Button-1>",
                     lambda event: kwargs["fnc1"](kwargs["card"].card_id, e1.get(), 2))





