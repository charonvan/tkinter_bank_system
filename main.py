# -*- coding:utf-8 -*-
import sqlite3
import re
from Model.options import SqlOptions
from Control.atm import ATM
from Control.myfunctions import MyFunctions
from View.interface import MainWindow


if __name__ == '__main__':
    conn = sqlite3.connect('Model/bank.db')  # 默认创建在当前目录


    db = SqlOptions(conn)
    win = MainWindow(db)

    win.mainloop()

    conn.close()
