# -*- coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('bank.db')  #默认创建在当前目录
c = conn.cursor()
'''
定义的表：
'''

#创建用户信息表
'''
id: 主键，自动增长
name:姓名
tel:电话号码
Birthplace:籍贯 （下面信息由身份证号获得，不用用户输入）
BirthYearL年龄
BirthMDay:出生年月
RegisterTime:注册时间
'''
c.execute('''CREATE TABLE user
       (Id INTEGER PRIMARY  KEY     NOT NULL,
       Name           VARCHAR(20)   NOT NULL,
       Idcard         CHAR(18)  UNIQUE  NOT NULL,
       Tel            CHAR(11)      NOT NULL,
       Birthplace     varchar(20)  DEFAULT 0,
       BirthYear      CHAR(4)      DEFAULT 0,
       BirthMDay     CHAR(4)      DEFAULT 0,
       RegisterTime  datetime  DEFAULT (datetime('now','localtime')));

       ''')


# 创建银行卡信息表
c.execute('''CREATE TABLE card
       (Id INTEGER PRIMARY  KEY     NOT NULL,
       Passwd           VARCHAR(50) NOT NULL,
       Money            int       NOT NULL,
       Idcard           char(18)  NOT NULL ,
       Status           int      DEFAULT 3,
       RegisterTime     datetime  DEFAULT (datetime('now','localtime')));''')


#创建操作日志表
c.execute('''CREATE TABLE loginfo
       (Id INTEGER PRIMARY  KEY   NOT NULL,
        CardId           int      NOT NULL,
        OptionsType      int      NOT NULL,
        Money            int    NOT NULL,
        InsertTime      datetime  DEFAULT (datetime('now','localtime')));''')


# 插入测试数据
c.execute("INSERT INTO card (Id,Passwd,Money,Idcard) \
      VALUES ('100000', 123456,1000,100)")
conn.commit()


#******************************************************************************

print("执行完成")
conn.close()