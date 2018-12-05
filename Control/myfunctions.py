# -*- coding:utf-8 -*-
import re
#存放公用的工具方法


class MyFunctions(object):
    # 1.判断参数是否为空
    @staticmethod
    def Check_args(*args, **kwargs):
        '''
        :param args:
        :param kwargs:
        :return: 如果都不为空返回1，否则返回0
        '''
        for arg in args:
            if arg is None or str(arg).strip() == "":
                return 0
        for value in kwargs.values():
            if value is None or str(value).strip() == "":
                return 0
        return 1

    # 2.验证身份证
    @staticmethod
    def Check_IDcard(IDcard: str):
        '''
        身份证数字含义：
        1-6位地址位：1-2代表省  3-4城市代码   5-6区县代码
        7-14位：出生年月  yyyy-mm-dd
        15-17位：顺序码，偶数表示女，奇数表示男
        18位：校验码：对前17位数字分别乘一个因数再求和，因数列表[7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2]
                    求得的和除以11求得余数就是对应列表的下标，从0开始，对应的表就是[1 0 X 9 8 7 6 5 4 3 2]
        :param Idcard:
        :return:
        '''

        # 检验身份证校验码
        def Check_code(IDcard: str):
            list1 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            list2 = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
            sum1 = 0
            for i in range(len(list1)):
                sum1 += list1[i] * int(IDcard[i])
            num = sum1 % 11
            if str(list2[num]).upper() == IDcard[-1]:
                return 1
            return 0

        IDcard = str(IDcard)
        # re_IDcard = re.compile(r"[1-6]\d{16}[0-9X]",re.I) # 简易版验证
        # 完整验证（加出生年月）
        re_IDcard = re.compile(r"[1-6]\d{5}(19\d\d|20[01][0-8])(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[0-9X]", re.I)
        if re_IDcard.match(IDcard) is not None:
            if Check_code(IDcard):
                return 1
            return "无效的身份证号码"
        return "身份证格式信息错误"

    # 3.解析身份证

    # 4.手机号码验证
    @staticmethod
    def Check_Tel(tel: str):
        re_tel = re.compile(r"1[3-8]\d{9}")
        if re_tel.match(str(tel)) is not None:
            return 1
        return "手机号码格式错误"


# 5.解析手机号码
