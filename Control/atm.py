#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Control.myfunctions import MyFunctions
import hmac
import random
'''
定义ATM机
   属性：钱数、账号、密码、是否可用
   行为：检验卡信息、取款、存款、转账、改密、锁卡、解锁、挂失、销户、开户

'''

class ATM(object):
    #初始化***********************************************************
    def __init__(self):
        self.money = 0
        self.isActive = True
        self.db = None

    def init_db(self, db):
        self.db = db

# 1.检查登陆
    def Check_login(self, cardId: str, passwd: str):
        '''

        :param cardId: 账户名
        :param passwd: 密码
        :return: 成功登录返回银行卡余额，否则返回错误信息
        '''
        cardId = str(cardId).strip()
        passwd = str(passwd).strip()
        if MyFunctions.Check_args(cardId, passwd):
            # 检查cardId是否存在
            sql1 = "select Passwd,Money,Status from card where Id = %s" % cardId
            res = self.db.SqlSelect(sql1)
            if res != -1:
                if len(res) != 0:
                    if res[0][2] > 0:
                        passwd = hmac.new("sunck".encode("utf-8"), passwd.encode("utf-8"), digestmod="MD5").hexdigest()
                        if res[0][0] == passwd:
                            return  res[0][1]  #int类型
                        #减少一次用户的状态码
                        sql2 = "update  card set Status = Status-1 where Id='%s'" % cardId
                        self.db.SqlCommit(sql2)
                        return "密码错误,还有%d次输入机会"%(res[0][2]-1)
                    return "卡被锁定"
                return "卡号不存在"
            return "执行错误"
        return "输入不能为空"

    # 2.开卡
    def Add_Account(self, userName: str, IDcard: str, Tel: str, passwd: str):
        '''
        :param userName:用户名
        :param IDcard: 身份证号
        :param Tel: 手机号
        :param passwd: 密码
        :return: 成功返回卡号，否则返回错误信息
        '''
        userName = str(userName).strip()
        IDcard = str(IDcard).strip()
        Tel = str(Tel).strip()
        passwd = str(passwd).strip()
        if MyFunctions.Check_args(userName,IDcard,Tel,passwd):
        #     #检查身份证号
        #     res1 = MyFunctions.Check_IDcard(IDcard)
        #     if res1 == 1:
                #查询是否开过户
                sql1 = "select count() from user where Idcard = %s"%IDcard
                res2 = self.db.SqlSelect(sql1)
                if res2 == -1:
                    return "查询执行错误"
                if res2[0][0] == 0: #账户不存在先开户
                     sq2 = "insert into user (name,Idcard,tel) values('%s','%s','%s')" % (userName, IDcard, Tel)
                     if  self.db.SqlCommit(sq2) == -1:
                         return "开户存储错误"

                passwd = hmac.new("sunck".encode("utf-8"), passwd.encode("utf-8"), digestmod="MD5").hexdigest()  # userName为key,password为s

                sql3 = "insert into card(Passwd,Money,Idcard) values ('%s',0,'%s')"%(passwd,IDcard)
                if self.db.SqlCommit(sql3) == -1:
                    return "开户存储失败"
                sql4 = "select Id from card where Idcard = %s ORDER BY Id desc limit 1"%IDcard
                res3 = self.db.SqlSelect(sql4)
                return res3[0][0] #返回卡号
            # return res1
        return "输入不能为空"

    # 3.解锁
    def Unlock_Account(self, userName: str, IDcard: str, Tel: str, cardId: str):
        '''

        :param userName:用户名
        :param IDcard: 身份证号
        :param Tel: 手机号
        :param cardId: 要解锁的卡号
        :return: 返回执行结果信息
        '''
        userName = str(userName).strip()
        IDcard = str(IDcard).strip()
        Tel = str(Tel).strip()
        cardId = str(cardId).strip()
        if MyFunctions.Check_args(userName, IDcard, Tel, cardId):
            #     #检查身份证号
            # res1 = MyFunctions.Check_IDcard(IDcard)
            # if res1 == 1:
                # 核验信息
                sql1 = "select Name,Tel from user where Idcard = %s" % IDcard
                res1 = self.db.SqlSelect(sql1)
                if res1 != -1:
                    if len(res1) != 0:
                        if res1[0][0] == userName and res1[0][1] == Tel:
                            sql2 = "update card set Status=3 where Id=%s" % cardId
                            if self.db.SqlCommit(sql2) != -1:
                                return "解锁成功"
                            return "解锁失败"
                        return "信息验证失败，无法解锁"
                    return "身份信息不存在"
                return "执行错误"
            # return res1
        return "输入不能为空"

    # 4.找回密码
    def Retrieve_passwd(self, userName: str, IDcard: str, Tel: str, cardId: str):
        userName = str(userName).strip()
        IDcard = str(IDcard).strip()
        Tel = str(Tel).strip()
        cardId = str(cardId).strip()
        if MyFunctions.Check_args(userName, IDcard, Tel, cardId):
            #     #检查身份证号
            # res1 = MyFunctions.Check_IDcard(IDcard)
            # if res1 == 1:
                # 核验信息
                sql1 = "select Name,Tel from user where Idcard = %s" % IDcard
                res1 = self.db.SqlSelect(sql1)
                if res1 != -1:
                    if len(res1) != 0:
                        if res1[0][0] == userName and res1[0][1] == Tel:
                            passwd = ""
                            for i in range(6):
                                passwd += str(random.randint(0,9))
                                passwd_hmac = hmac.new("sunck".encode("utf-8"), passwd.encode("utf-8"), digestmod="MD5").hexdigest()
                            sql2 = "update card set Passwd='%s' where Id='%s'" % (passwd_hmac,cardId)
                            if self.db.SqlCommit(sql2) != -1:
                                return "1#新密码为：%s ,请尽快修改"%passwd
                            return "找回密码失败"
                        return "信息验证失败，无法找回密码"
                    return "身份信息不存在"
                return "执行错误"
            # return res1
        return "输入不能为空"

    # 5.退出（如果用户退出前有修改配置，则执行这个函数）
    def Drop_out(self, cardId: str, **kwargs: str):
        '''
        :param cardId:银行卡号
        :param kwargs: 配置信息 eg: bg=1,color=2
        :return:
        '''

        pass




    # 操作页面函数


    # 6.账单日志
    def Bill_info(self, cardId: str):
        '''
        :param cardId:银行卡号
        :return: 日志列表，格式为：Tuple((time,type,money),(time,type,money),(),())
        '''
        sql1 = "select InsertTime,OptionsType,Money from loginfo where CardId = '%s' ORDER BY Id DESC" % cardId
        res = self.db.SqlSelect(sql1)
        print(res)
        if  res != -1:
            if len(res) != 0:
                return res
        return None



    # 7.取款
    def Withdrawal(self, cardId: str, money: str):
        '''
        :param cardId: 银行卡号
        :param money: 金额
        :param operatingType: 操作值，存钱为1，取钱为2
        :return: 执行结果
        '''
        cardId = str(cardId).strip()
        money = str(money).strip()
        if MyFunctions.Check_args(cardId, money):
            # 取款
            sql1 = "select Money from card where Id = %s" % cardId
            res1 = self.db.SqlSelect(sql1)
            all_money = res1[0][0]  # 获取查到的钱数
            if all_money >= int(money):
                sql2 = "UPDATE card set money = money -%d where id='%s'" % (int(money), cardId)
                res2 = self.db.SqlCommit(sql2)
                if res2 != 1:  # 返回执行成功的行数
                    return "操作失败"
            else:
                return "余额不足"
            # 把记录插入到日志
            self.Insert_loginfo(cardId,1,money)
            return 1
        return "内容不能为空"

    # 8.存款
    def Deposit(self, cardId: str, money: str):
        '''
            :param cardId: 银行卡号
            :param money: 金额
            :param operatingType: 操作值，存钱为1，取钱为2
            :return: 执行结果
        '''
        cardId = str(cardId).strip()
        money = str(money).strip()
        if MyFunctions.Check_args(cardId, money):
            sql2 = "UPDATE card set money = money +%d where id='%s'" % (int(money), cardId)
            res2 = self.db.SqlCommit(sql2)
            if res2 != 1:  # 返回执行成功的行数
                return "操作失败"
            # 把记录插入到日志
            self.Insert_loginfo(cardId, 2, money)
            return 1
        return "内容不能为空"

    #9把信息存入日志
    def Insert_loginfo(self, cardId, operatingType, money):
        sql3 = "insert into loginfo(CardId,OptionsType,Money) values ('%s','%s','%s')" % (cardId, operatingType, money)
        res2 = self.db.SqlCommit(sql3)
        if res2 != 1:
            return "日志表插入失败"

    # 10.转账
    def Transfer_money(self, cardId1: str, cardId2: str, money: str):
        '''
        :param cardId1:当前卡号
        :param cardId2: 对方卡号
        :param money: 金额
        :return: 执行结果
        '''
        if MyFunctions.Check_args(cardId1,cardId2, money):
            # 检查cardId2是否存在
            sql1 = "select count() from card where Id = %s" % cardId2
            res = self.db.SqlSelect(sql1)
            if res != -1 and res[0][0] != 0:
                res1 = self.Withdrawal(cardId1, money)
                if res1 == 1:
                    res2 = self.Deposit(cardId2, money)
                    if res2 == 1:
                        self.Insert_loginfo(cardId1, 3, money)  # 3代表转账
                        self.Insert_loginfo(cardId2, 4, money)  # 4代表收款
                        return 1
                    return res2
                return res1
            return "对方卡号不存在"
        return "输入有误"

    # 11.改密
    def Change_passwd(self, cardId: str, passwd1: str, passwd2: str):
        '''
        :param cardId:当前卡号
        :param passwd1: 密码1
        :param passwd2: 密码2
        :return: 执行结果
        '''
        passwd1 = str(passwd1).strip()
        passwd2 = str(passwd2).strip()
        if MyFunctions.Check_args(cardId,passwd1, passwd2):
            if passwd1 == passwd2:
               passwd1 = hmac.new("sunck".encode("utf-8"), passwd1.encode("utf-8"), digestmod="MD5").hexdigest()
               sql1 = "update card set Passwd = '%s' where id ='%s'" %(passwd1, cardId)
               res = self.db.SqlCommit(sql1)
               if res == 1:
                   return "修改成功"
               return "操作失败"
            return "两次密码不一致"
        return "不能输入空值"

    # 12.锁卡/挂失
    def Lock_Account(self, userName: str, IDcard: str, Tel: str, cardId: str):
        userName = str(userName).strip()
        IDcard = str(IDcard).strip()
        Tel = str(Tel).strip()
        cardId = str(cardId).strip()
        if MyFunctions.Check_args(userName, IDcard, Tel, cardId):
            #     #检查身份证号
            # res1 = MyFunctions.Check_IDcard(IDcard)
            # if res1 == 1:
                # 核验信息
                sql1 = "select Name,Tel from user where Idcard = %s" % IDcard
                res1 = self.db.SqlSelect(sql1)
                if res1 != -1:
                    if len(res1) != 0:
                        if res1[0][0] == userName and res1[0][1] == Tel:
                            sql2 = "update card set Status = 0 where id =%s" % cardId
                            res = self.db.SqlCommit(sql2)
                            if res == 1:
                                return 1
                            return "操作失败"
                        return "信息验证失败，无法锁卡"
                    return "身份信息不存在"
                return "执行错误"
            # return res1
        return "输入不能为空"

    # 13 .销户
    def Delete_Account(self, userName: str, IDcard: str, Tel: str, cardId: str):
        userName = str(userName).strip()
        IDcard = str(IDcard).strip()
        Tel = str(Tel).strip()
        cardId = str(cardId).strip()
        if MyFunctions.Check_args(userName, IDcard, Tel, cardId):
            # #     #检查身份证号
            # res1 = MyFunctions.Check_IDcard(IDcard)
            # if res1 == 1:
                # 核验信息
                sql1 = "select Name,Tel from user where Idcard = %s" % IDcard
                res1 = self.db.SqlSelect(sql1)
                if res1 != -1:
                    if len(res1) != 0:
                        if res1[0][0] == userName and res1[0][1] == Tel:
                            sql2 = "delete from card where id =%s" % cardId
                            res = self.db.SqlCommit(sql2)
                            if res == 1:
                                return 1
                            return "操作失败"
                        return "信息验证失败，无法销户"
                    return "身份信息不存在"
                return "执行错误"
            # return res1
        return "输入不能为空"



