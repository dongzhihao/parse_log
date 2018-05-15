#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'passwd': '123456',
    'port': 3306,
    'db': 'POS',
    'charset': 'utf8'
}


def getDB():
    try:
        conn = MySQLdb.connect(host=db_config['host'], user=db_config['user'], passwd=db_config['passwd'],
                               port=db_config['port'],charset=db_config['charset'])
        conn.autocommit(True)
        curr = conn.cursor()
        curr.execute("SET NAMES utf8;")
        curr.execute("USE %s;" % db_config['db'])
        return conn, curr
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return None, None