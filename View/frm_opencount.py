#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter as tk
"""
program name :
last modification time :
changelog :
"""


class PageOpenCount(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        开户页面
        功能：提交开户数据

        :param master: 上层容器
        :param kwargs: config, height, width
        """
        # 建立框架本体
        super().__init__(master, height=kwargs["height"] if "height" in kwargs else None,
                         width=kwargs["width"] if "width" in kwargs else None)
        self.config = kwargs["config"]
        self.label_text1 = tk.StringVar()
        if kwargs["optionType"] == 1:
            self.label_text1.set("您的密码")
        else:
            self.label_text1.set("您的卡号")
        # 建立框架内容
        # 导入图片  预留：读取配置
        self.page_home_bg = tk.PhotoImage(file="%spage_home_bg.png" % self.config["image_path"])  # 背景路径
        self.image_label = None  # tk.PhotoImage(file="assets/image/button1.png")
        self.image_button1 = tk.PhotoImage(file="%sbutton2.png" % self.config["image_path"])
        # 图片载体
        self.stage = tk.Label(self, height=kwargs["height"], width=kwargs["width"], compound=tk.CENTER,
                              image=self.page_home_bg)
        self.stage.pack()


        lb2 = tk.Label(self.stage,
                       text="您的姓名",
                       compound=tk.CENTER, image=self.image_button1,
                       font=self.config["font"],
                       width=80,
                       height=25,
                       fg="white",
                       anchor="center")
        lb2.place(x=330, y=150)

        e1 = tk.Entry(self.stage, font=self.config["font"],bd=4,width=15,fg="orange")
        e1.place(x=440, y=150)

        lb3 = tk.Label(self.stage,
                       text="身份证号",
                       compound=tk.CENTER, image=self.image_button1,
                       font=self.config["font"],
                       width=80,
                       height=25,
                       fg="white",
                       anchor="center")
        lb3.place(x=330, y=220)

        e2 = tk.Entry(self.stage, font=self.config["font"],bd=4,width=15,fg="orange")
        e2.place(x=440, y=220)

        lb4 = tk.Label(self.stage,
                       text="手机号码",
                       compound=tk.CENTER, image=self.image_button1,
                       font=self.config["font"],
                       width=80,
                       height=25,
                       fg="white",
                       anchor="center")
        lb4.place(x=330, y=290)

        e3 = tk.Entry(self.stage, font=self.config["font"],bd=4,width=15,fg="orange")
        e3.place(x=440, y=290)

        lb5 = tk.Label(self.stage,
                       text=self.label_text1.get(),
                       compound=tk.CENTER, image=self.image_button1,
                       font=self.config["font"],
                       width=80,
                       height=25,
                       fg="white",
                       anchor="center")
        lb5.place(x=330, y=360)

        e4 = tk.Entry(self.stage, font=self.config["font"],bd=4,width=15,fg="orange")
        e4.place(x=440, y=360)

        bt1 = tk.Button(self.stage, text="提交信息",fg="white", width=150, height=30, font=self.config["font"],
                        compound=tk.CENTER, image=self.image_button1)
        bt1.place(x=440, y=450)
        bt1.bind("<Button-1>",
                 lambda event: kwargs["fnc1"](e1.get(), e2.get(), e3.get(), e4.get()))


