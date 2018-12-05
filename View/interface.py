#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter as tk
import os
from tkinter import messagebox
from Control.atm import ATM
from Control.card import Card
from View.frm_access import PageAccess
from View.frm_bill import PageBill
from View.frm_change import PageChange
from View.frm_count import PageCount
from View.frm_home import PageHome
from View.frm_chat import PageChat
from View.frm_opencount import PageOpenCount
from View.frm_transfer import PageTransfer



class MainWindow(object):
    """
    使用 win = MainWindow() 启动窗口
    使用 win.mainloop() 等待事件
    使用 win.open_page(page_name: str) 打开指定页面，页面名我一会加上
    """
    # 初始化数据
    card = Card(cardId="0", money=0)
    atm = ATM()

    # 控制窗口之间的切换
    def __init__(self, db):
        self.atm.init_db(db)
        self.main_window = tk.Tk()
        self.main_window.title("银行自助服务终端  by.凯哥御用制作团")
        self.main_window.geometry("940x660+250+100")
        self.config = self.get_config()  # 获取主界面配置

        # 建立、放置内外框架(外：940x660 内：700x600)
        self.outer_frm = MainFrame(self.main_window, config=self.config, height=700, width=940)  #
        self.outer_frm.pack()  # 放置外框架
        self.inner_frm = None

        # 导入图片  预留：读取配置
        self.img_bg = tk.PhotoImage(file="%spage_home_bg.png" % self.config["image_path"])  # 背景路径
        # self.img_button1 = tk.PhotoImage(file="assets/image/button1.png")



        # 打开主页面
        self.open_page("home")
        # self.open_page("count")

    @staticmethod
    def get_config():
        # 读取配置文件
        return {"font": ("宋体", 15), "main_frame_color": "silver", "image_path": "View/image/"}

    def event_login(self, cardId: str, passwd: str):
        res = self.atm.Check_login(cardId, passwd)
        if isinstance(res, int):
            self.card = Card(cardId=cardId, money=res)
            self.open_page("count")
        else:
            tk.messagebox.showinfo("警告", res)

    def event_add_account(self, userName: str, IDcard: str, Tel: str, passwd: str):
        res = self.atm.Add_Account(userName, IDcard, Tel, passwd)
        print(res, type(res))
        if isinstance(res, int):
            self.card = Card(cardId=res, money=0)
            tk.messagebox.showinfo("开卡成功！", "卡号为：\n%d" % res)
            self.open_page("count")
        else:
            tk.messagebox.showinfo("警告", res)

    def event_unlock_account(self, userName: str, IDcard: str, Tel: str, cardId: str):
        res = self.atm.Unlock_Account(userName, IDcard, Tel, cardId)
        if res == "解锁成功":
            tk.messagebox.showinfo("恭喜", res)
            self.open_page("home")
        else:
            tk.messagebox.showinfo("警告", res)

    def event_retrieve_password(self, UserName: str, IDcard: str, Tel: str, cardId: str):
        res = self.atm.Retrieve_passwd(UserName, IDcard, Tel, cardId).split(":")
        if res[0] == "1":
            tk.messagebox.showinfo("温馨提示：", res[1])
            self.open_page("home")
        else:
            tk.messagebox.showinfo("警告：", res[0])

    def event_access_money(self, cardId: str, money: str, operatingType: str):
        if operatingType == 1:
            res = self.atm.Deposit(cardId, money)
            if res == 1:
                tk.messagebox.showinfo("温馨提示", "存款成功！")
                self.card.money += eval(money)
                self.open_page("count")
            else:
                tk.messagebox.showinfo("温馨提示", res)
        elif operatingType == 2:
            res = self.atm.Withdrawal(cardId, money)
            if res == 1:
                tk.messagebox.showinfo("温馨提示", "取款成功!")
                self.card.money -= eval(money)
                self.open_page("count")
            else:
                tk.messagebox.showinfo("温馨提示", res)

    def event_transfer_money(self, cardId2: str, money: str):
        res = self.atm.Transfer_money(self.card.card_id, cardId2, money)
        if res == 1:
            tk.messagebox.showinfo("温馨提示", "转账成功！")
            self.card.money -= eval(money)
            self.open_page("count")
        else:
            tk.messagebox.showinfo("温馨提示", res)

    def event_change_passwd(self, passwd1: str, passwd2: str):
        res = self.atm.Change_passwd(self.card.card_id, passwd1, passwd2)
        if res == "修改成功":
            tk.messagebox.showinfo("温馨提示", res)
            self.open_page("count")
        else:
            tk.messagebox.showinfo("温馨提示", res)

    def event_lock_account(self, userName: str, IDcard: str, Tel: str, cardId: str):
        res = self.atm.Lock_Account(userName, IDcard, Tel, cardId)
        if isinstance(res, int):
            tk.messagebox.showinfo("温馨提示", "操作成功！")
            self.open_page("home")
        else:
            tk.messagebox.showinfo("温馨提示", res)

    def event_delete_account(self, userName: str, IDcard: str, Tel: str, cardId: str):
        res = self.atm.Delete_Account(userName, IDcard, Tel, cardId)
        if isinstance(res, int):
            tk.messagebox.showinfo("温馨提示", "已成功销户！")
            self.open_page("home")
        else:
            tk.messagebox.showinfo("温馨提示", res)

    def event_send_chat(self):
        pass

    # def event_drop_out(self):
    #     self.atm.Drop_out(self.card.card_id, **self.config)

    def open_page(self, page_name: str):
        # 打开指定页面 并设置页面参数
        def clear():
            # 清除按钮功能
            # self.outer_frm.bt_l1.unbind_all("<Button-1>")
            # self.outer_frm.bt_l2.unbind_all("<Button-1>")
            # self.outer_frm.bt_l3.unbind_all("<Button-1>")
            # self.outer_frm.bt_l4.unbind_all("<Button-1>")
            # self.outer_frm.bt_l5.unbind_all("<Button-1>")
            # self.outer_frm.bt_r1.unbind_all("<Button-1>")
            # self.outer_frm.bt_r2.unbind_all("<Button-1>")
            # self.outer_frm.bt_r3.unbind_all("<Button-1>")
            # self.outer_frm.bt_r4.unbind_all("<Button-1>")
            # self.outer_frm.bt_r5.unbind_all("<Button-1>")
            self.outer_frm.bt_l1.bind("<Button-1>", lambda event: 1)
            self.outer_frm.bt_l2.bind("<Button-1>", lambda event: 1)
            self.outer_frm.bt_l3.bind("<Button-1>", lambda event: 1)
            self.outer_frm.bt_l4.bind("<Button-1>", lambda event: 1)
            self.outer_frm.bt_l5.bind("<Button-1>", lambda event: 1)

            self.outer_frm.bt_r1.bind("<Button-1>", lambda event: 1)
            self.outer_frm.bt_r2.bind("<Button-1>", lambda event: 1)
            self.outer_frm.bt_r3.bind("<Button-1>", lambda event: 1)
            self.outer_frm.bt_r4.bind("<Button-1>", lambda event: 1)
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: 1)

            # 清除外框架按钮文字
            self.outer_frm.bt_l1_t.set("")
            self.outer_frm.bt_l2_t.set("")
            self.outer_frm.bt_l3_t.set("")
            self.outer_frm.bt_l4_t.set("")
            self.outer_frm.bt_l5_t.set("")
            self.outer_frm.bt_r1_t.set("")
            self.outer_frm.bt_r2_t.set("")
            self.outer_frm.bt_r3_t.set("")
            self.outer_frm.bt_r4_t.set("")
            self.outer_frm.bt_r5_t.set("")
        if page_name == "home":
            # 摧毁框架
            if self.inner_frm is not None:
                clear()
                self.inner_frm.destroy()
            # 建立内框架
            self.inner_frm = PageHome(self.outer_frm.container, config=self.config, height=590, width=690,
                                      card=self.card, fnc1=self.event_login)
            self.inner_frm.pack(padx=5, pady=5)
            # 设置外框架按钮
            self.outer_frm.bt_l1_t.set("开户")
            self.outer_frm.bt_l2_t.set("解锁")
            self.outer_frm.bt_r1_t.set("找回密码")
            self.outer_frm.bt_r2_t.set("退出系统")
            self.outer_frm.bt_l1.bind("<Button-1>", lambda event: self.open_page("opencount"))
            self.outer_frm.bt_l2.bind("<Button-1>", lambda event: self.open_page("unlock"))
            self.outer_frm.bt_r1.bind("<Button-1>", lambda event: self.open_page("resetpassword"))

            self.outer_frm.bt_r2.bind("<Button-1>", lambda event: self.main_window.destroy())
        elif page_name == "opencount":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("home"))
            # 建立内框架
            self.inner_frm = PageOpenCount(self.outer_frm.container, config=self.config, height=590, width=690,
                                           card=self.card, fnc1=self.event_add_account,optionType=1)
            self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "resetpassword":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("home"))
            # 建立内框架
            self.inner_frm = PageOpenCount(self.outer_frm.container, config=self.config, height=590, width=690,
                                                  card=self.card, fnc1=self.event_retrieve_password,optionType=2)
            self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "unlock":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("home"))
            # 建立内框架
            self.inner_frm = PageOpenCount(self.outer_frm.container, config=self.config, height=590, width=690,
                                        card=self.card, fnc1=self.event_unlock_account,optionType=3)
            self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "count":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 建立内框架
            self.inner_frm = PageCount(self.outer_frm.container, config=self.config, height=590, width=690, card=self.card)
            self.inner_frm.pack(padx=5, pady=5)
            # 设置外框架按钮
            self.outer_frm.bt_l1_t.set("取款")
            self.outer_frm.bt_l2_t.set("转账")
            self.outer_frm.bt_l3_t.set("锁卡")
            self.outer_frm.bt_l4_t.set("账单详情")
            self.outer_frm.bt_l5_t.set("销户")
            self.outer_frm.bt_r1_t.set("存款")
            self.outer_frm.bt_r2_t.set("改密")
            self.outer_frm.bt_r3_t.set("挂失")
            self.outer_frm.bt_r4_t.set("人工服务")
            self.outer_frm.bt_r5_t.set("退出登录")
            self.outer_frm.bt_l1.bind("<Button-1>", lambda event: self.open_page("withdrawal"))
            self.outer_frm.bt_l2.bind("<Button-1>", lambda event: self.open_page("transfer"))
            self.outer_frm.bt_l3.bind("<Button-1>", lambda event: self.open_page("lock"))
            self.outer_frm.bt_l4.bind("<Button-1>", lambda event: self.open_page("bill"))
            self.outer_frm.bt_l5.bind("<Button-1>", lambda event: self.open_page("delete"))
            self.outer_frm.bt_r1.bind("<Button-1>", lambda event: self.open_page("deposit"))
            self.outer_frm.bt_r2.bind("<Button-1>", lambda event: self.open_page("change"))
            self.outer_frm.bt_r3.bind("<Button-1>", lambda event: self.open_page("lock"))
            self.outer_frm.bt_r4.bind("<Button-1>", lambda event: self.open_page("chat"))
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("home"))
        elif page_name == "withdrawal":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("count"))
            # 建立内框架
            self.inner_frm = PageAccess(self.outer_frm.container, config=self.config, height=590, width=690,
                                        card=self.card, fnc1=self.event_access_money,OptionType=2)
            self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "deposit":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("count"))
            # 建立内框架
            self.inner_frm = PageAccess(self.outer_frm.container, config=self.config, height=590, width=690,
                                        card=self.card, fnc1=self.event_access_money,OptionType=1)
            self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "transfer":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("count"))
            # 建立内框架
            self.inner_frm = PageTransfer(self.outer_frm.container, config=self.config, height=590, width=690,
                                          card=self.card, fnc1=self.event_transfer_money)
            self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "chat":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("count"))
            # 建立内框架
            self.inner_frm = PageChat(self.outer_frm.container, config=self.config, height=590, width=690,
                                          card=self.card, fnc1=self.event_send_chat)
            self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "change":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("count"))
            # 建立内框架
            self.inner_frm = PageChange(self.outer_frm.container, config=self.config, height=590, width=690,
                                        card=self.card, fnc1=self.event_change_passwd)
            self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "bill":
            bill = self.atm.Bill_info(self.card.card_id)
            if bill is None:
                tk.messagebox.showinfo("温馨提示", "账单加载错误，请稍后再试。")
            else:
                # 摧毁框架
                self.inner_frm.destroy()
                clear()
                # 设置外框架按钮
                self.outer_frm.bt_r5_t.set("返回")
                self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("count"))
                # 建立内框架
                self.inner_frm = PageBill(self.outer_frm.container, config=self.config, height=590, width=690,
                                          card=self.card, bill=bill)
                self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "lock":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("count"))
            # 建立内框架
            self.inner_frm = PageOpenCount(self.outer_frm.container, config=self.config, height=590, width=690,
                                      card=self.card, fnc1=self.event_lock_account,optionType=2)
            self.inner_frm.pack(padx=5, pady=5)
        elif page_name == "delete":
            # 摧毁框架
            self.inner_frm.destroy()
            clear()
            # 设置外框架按钮
            self.outer_frm.bt_r5_t.set("返回")
            self.outer_frm.bt_r5.bind("<Button-1>", lambda event: self.open_page("count"))
            # 建立内框架
            self.inner_frm = PageOpenCount(self.outer_frm.container, config=self.config, height=590, width=690,
                                        card=self.card, fnc1=self.event_delete_account,optionType=2)
            self.inner_frm.pack(padx=5, pady=5)

    def mainloop(self):
        # 交付CPU控制权，等待事件
        self.main_window.mainloop()


class MainFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        # 建立框架本体
        super().__init__(master, height=kwargs["height"] if "height" in kwargs else None,
                         width=kwargs["width"] if "width" in kwargs else None)
        self.config = kwargs["config"]

        # 导入图片  预留：读取配置
        self.img_bg = tk.PhotoImage(file="%spage_home_bg.png" % kwargs["config"]["image_path"])  # 背景路径
        self.img_button1 = tk.PhotoImage(file="%sbutton1.png" % kwargs["config"]["image_path"])
        self.img_button2 = tk.PhotoImage(file="%sbutton2.png" % kwargs["config"]["image_path"])
        self.img_outer_button1 = tk.PhotoImage(file="%sbutton1.png" % kwargs["config"]["image_path"])
        self.img_outer_bg1 = tk.PhotoImage(file="%souter_bg1.png" % kwargs["config"]["image_path"])
        self.img_outer_bg2 = tk.PhotoImage(file="%souter_bg2.png" % kwargs["config"]["image_path"])
        self.img_button1 = tk.PhotoImage(file="%sbutton1.png" % kwargs["config"]["image_path"])

        # 初始化框架变量
        self.bt_l1_t = tk.StringVar()
        self.bt_l2_t = tk.StringVar()
        self.bt_l3_t = tk.StringVar()
        self.bt_l4_t = tk.StringVar()
        self.bt_l5_t = tk.StringVar()
        self.bt_r1_t = tk.StringVar()
        self.bt_r2_t = tk.StringVar()
        self.bt_r3_t = tk.StringVar()
        self.bt_r4_t = tk.StringVar()
        self.bt_r5_t = tk.StringVar()
        # self.bt_b1_t = tk.StringVar()  # 下边按钮(预留)

        # 建立及放置边框（下、左、右）
        frm_b = tk.Frame(self, bg=kwargs["config"]["main_frame_color"], height=60)
        frm_b_label1 = tk.Label(frm_b,compound=tk.CENTER,height=60, image=self.img_outer_bg1)
        frm_b_label1.pack(side=tk.BOTTOM,fill=tk.X)
        frm_b.pack(side=tk.BOTTOM, fill=tk.X)

        frm_l = tk.Frame(self, bg=kwargs["config"]["main_frame_color"], width=150)
        frm_l_label1 = tk.Label(frm_l, compound=tk.CENTER, width=150, image=self.img_outer_bg2)
        frm_l_label1.pack(side=tk.LEFT, fill=tk.Y)
        frm_l.pack(side=tk.LEFT, fill=tk.Y)

        frm_r = tk.Frame(self, bg=kwargs["config"]["main_frame_color"], width=150)
        frm_r_label1 = tk.Label(frm_r, compound=tk.CENTER, width=150, image=self.img_outer_bg2)
        frm_r_label1.pack(side=tk.RIGHT, fill=tk.Y)
        frm_r.pack(side=tk.RIGHT, fill=tk.Y)

        frm_t = tk.Frame(self, bg=kwargs["config"]["main_frame_color"], height=20)
        frm_t_label1 = tk.Label(frm_t, compound=tk.CENTER, height=20, image=self.img_outer_bg1)
        frm_t_label1.pack(side=tk.TOP, fill=tk.X)
        frm_t.pack(side=tk.TOP, fill=tk.X)

        # 下一层frame/控件容器  选用Lable或Canvas
        self.container = tk.Canvas(self, height=600, width=700, bg="black")
        self.container.pack(side=tk.TOP)
        # self.container.create_image(0, 0, image=self.img_bg)  # 放置图片 存在作用域问题。。。
        # self.container = tk.Label(self, height=600, width=700, compound=tk.CENTER, image=self.img_bg)
        # self.container.pack(side=tk.TOP)

        # 放置按钮
        self.bt_l1 = tk.Button(frm_l, textvariable=self.bt_l1_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1,)
        self.bt_l1.place(x=25, y=40)
        self.bt_l2 = tk.Button(frm_l, textvariable=self.bt_l2_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1)
        self.bt_l2.place(x=25, y=160)
        self.bt_l3 = tk.Button(frm_l, textvariable=self.bt_l3_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1)
        self.bt_l3.place(x=25, y=280)
        self.bt_l4 = tk.Button(frm_l, textvariable=self.bt_l4_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1)
        self.bt_l4.place(x=25, y=400)
        self.bt_l5 = tk.Button(frm_l, textvariable=self.bt_l5_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1)
        self.bt_l5.place(x=25, y=520)

        self.bt_r1 = tk.Button(frm_r, textvariable=self.bt_r1_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1)
        self.bt_r1.place(x=25, y=40)
        self.bt_r2 = tk.Button(frm_r, textvariable=self.bt_r2_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1)
        self.bt_r2.place(x=25, y=160)
        self.bt_r3 = tk.Button(frm_r, textvariable=self.bt_r3_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1)
        self.bt_r3.place(x=25, y=280)
        self.bt_r4 = tk.Button(frm_r, textvariable=self.bt_r4_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1)
        self.bt_r4.place(x=25, y=400)
        self.bt_r5 = tk.Button(frm_r, textvariable=self.bt_r5_t, width=100, height=45, font=self.config["font"],
                               compound=tk.CENTER, image=self.img_button1)
        self.bt_r5.place(x=25, y=520)

        lb1 = tk.Label(frm_b, text="All Rights Reserved @ BJ-Python-GP-1",
                       font=("宋体", 10),
                       compound=tk.CENTER, image=self.img_outer_bg1,
                       width=260,
                       height=14,
                       fg="red",
                       anchor="center")

        lb1.place(x=680, y=43)
        pass


class Massage(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        消息提示框

        :param master: 上层容器
        :param kwargs: config, height, width
        """
        # 建立框架本体
        super().__init__(master, height=kwargs["height"] if "height" in kwargs else None,
                         width=kwargs["width"] if "width" in kwargs else None)
        self.config = kwargs["config"]
        # 建立框架内容

