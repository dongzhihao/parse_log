#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import warnings
from db import getDB

warnings.filterwarnings("ignore")

conn, curr = getDB()


def log_parse_heartbeat(log_data):
    '''
    appKey = log_data['appKey']
    deviceId = log_data['data']['deviceId']
    time = log_data['data']['time']
    print ("%s %s %s %s" % (sid, appKey, deviceId, time))
    '''
    pass


def log_parse_basicinfo(log_data):
    '''
    appKey = log_data['appKey']
    deviceId = log_data['data']['deviceId']
    lineId = log_data['data']['lineId']
    # companyName = log_data['data']['companyName']
    lineName = log_data['data']['lineName']
    lineCode = log_data['data']['lineCode']
    lineShort = log_data['data']['lineShort']
    carryCode = log_data['data']['carryCode']
    carryNo = log_data['data']['carryNo']
    price = log_data['data']['price']
    gprsCode = log_data['data']['gprsCode']
    gprsType = log_data['data']['gprsType']
    supplier = log_data['data']['supplier']
    headShow = log_data['data']['headShow']
    lineShow = log_data['data']['lineShow']
    type = log_data['data']['type']
    originalPrice = log_data['data']['originalPrice']
    localCompanyName = log_data['data']['localCompanyName']
    localCompanyCode = log_data['data']['localCompanyCode']
    localDepartmentCode = log_data['data']['localDepartmentCode']
    localDepartmentName = log_data['data']['localDepartmentName']
    count = log_data['data']['count']
    print ("%s %s %s %s %s %s %s %s %s %d %s %s %s"
           % (sid, appKey, deviceId, lineId, lineCode, lineName, lineShort, carryCode, carryNo, price,
              supplier, type, originalPrice,))
    '''
    pass


def log_parse_businfo(log_data):
    appKey = log_data['appKey']
    deviceId = log_data['data']['deviceId']
    appVersion = log_data['data']['appVersion']
    sql = "insert into DEVICE(appKey, deviceId, version) values ('%s', '%s')" % (appKey, deviceId, appVersion)
    print sql

    curr.execute(sql)


def log_parse_time(log_data):
    # print log_data
    pass


def log_parse_appkey(log_data):
    # print log_data
    pass


def log_parse_upgrade(log_data):
    # print log_data
    pass

def log_parse_error(log_data):
    # print log_data
    pass


if __name__ == "__main__":
    with open('/home/dong/PycharmProjects/parse_log/event.2018-05-14.0.log', 'r') as f:
        for json_array in f:
            log_array = json.loads(json_array)
            happenTime = log_array['happenTime']
            if 'data' in log_array.keys() and 'data' in log_array['data'].keys():
                if 'sid' in log_array['data']:
                    sid = log_array['data']['sid']
                    try:
                        value = {
                            '10202': log_parse_basicinfo,
                            '10001': log_parse_businfo,
                            '10002': log_parse_time,
                            '10007': log_parse_appkey,
                            '10004': log_parse_heartbeat,
                            '10003': log_parse_upgrade
                        }.get(sid, log_parse_error)(log_array['data'])
                    except KeyError:
                        print log_array['data']
                    except TypeError:
                        print log_array['data']
    curr.close()
    conn.close()