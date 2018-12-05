# -*- coding:utf-8 -*-

class SqlOptions(object):
    def __init__(self, db):
        self.db = db

    # 增、删、改
    def SqlCommit(self, sql):
        '''

        :param sql:
        :return:执行过程出错，返回-1，不出错返回执行成功的行数
        '''
        c = self.db.cursor()
        try:
            res = c.execute(sql)
            self.db.commit()
            return res.rowcount
        except Exception as e:
            print(e)
            return -1

    # 查询
    def SqlSelect(self, sql):
        '''

        :param sql:
        :return:如果执行中除错，返回-1，可用 len(res)判断是否有结果，为0表示无记录
        '''
        c = self.db.cursor()
        try:
            res = c.execute(sql)
            return res.fetchall()
        except Exception as e:
            print(e)
            return -1
