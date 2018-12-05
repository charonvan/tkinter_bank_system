#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import ttk
import datetime
import time
import re
"""
program name :
last modification time :
changelog :
"""
# t1 = datetime.datetime.now()
# print(t1, type(t1))
# t2 = time.time()
# print(t2, type(t2))
# t3 = time.localtime(t2)
# print(t3.tm_mday, type(t3))


class PageBill(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        账单页面
        查看账户历史账单

        :param master: 上层容器
        :param kwargs: config, height, width
        """
        # 建立框架本体
        super().__init__(master, height=kwargs["height"] if "height" in kwargs else None,
                         width=kwargs["width"] if "width" in kwargs else None)
        self.config = kwargs["config"]
        self.bill = kwargs["bill"]
        # 建立框架内容
        # 导入图片  预留：读取配置
        self.page_home_bg = tk.PhotoImage(file="%spage_count_bg.png" % self.config["image_path"])  # 背景路径
        self.image_label = tk.PhotoImage(file="%scount_label_bg.png" % self.config["image_path"])
        self.image_button1 = tk.PhotoImage(file="%sbutton2.png" % self.config["image_path"])
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
                       text="账单详情",
                       compound=tk.CENTER, image=self.image_button1,
                       font=("宋体", 18),
                       width=250,
                       height=30,
                       fg="white",
                       anchor="center")
        lb2.place(x=200, y=150)

        # 生成表格
        tree = ttk.Treeview(self.stage)
        tree.place(x=10, y=260)
        # 插入列
        tree["columns"] = ("type", "money")
        # tree.column("time")  # , width=100
        tree.column("type")
        tree.column("money")
        # 添加表头
        tree.heading("type", text="操作类型")
        tree.heading("money", text="涉及金额")
        # 插入信息
        last = [0, None, 0, "时间"]
        for index, item in enumerate(self.bill):
            op_time = time.strptime(item[0], "%Y-%m-%d %H:%M:%S")  # 2018-08-18 12:57:21
            date = "%s-%s" % (op_time.tm_year, op_time.tm_mon)
            if date == last[3]:
                if item[1] == 1:
                    v1 = "取款"
                elif item[1] == 2:
                    v1 = "存款"
                elif item[1] == 3:
                    v1 = "转账"
                else:
                    v1 = "转入"
                tree.insert(last[1], last[2],
                            text="%s号%s:%s:%s" % (op_time.tm_mday, op_time.tm_hour, op_time.tm_min, op_time.tm_sec),
                            value=(v1, item[2]))
                last[2] += 1
            else:
                last[3] = date
                last[1] = tree.insert("", last[0], text=date)
                last[0] += 1


