#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import warnings
import time

warnings.filterwarnings("ignore")

offset = 24*60*60

if __name__ == "__main__":
    with open('/home/dong/PycharmProjects/parse_log/event_qrcode.2018-05-14.0.log', 'r') as f:
        i = 0
        for json_array in f:
            log_array = json.loads(json_array)
            happenTime = log_array['happenTime']
            happenTime_t = time.mktime(time.strptime(happenTime,'%Y-%m-%d %H:%M:%S'))
            if 'data' in log_array.keys() and 'data' in log_array['data'].keys():
                if 'sid' in log_array['data']:
                    sid = log_array['data']['sid']
                    appKey = log_array['data']['appKey']
                    actualOrderTime = log_array['data']['data'][0]['actualOrderTime']
                    actualOrderTime_t = time.mktime(time.strptime(actualOrderTime, '%Y-%m-%d %H:%M:%S'))
            try:
                outTradeNo = log_array['data']['data'][0]['outTradeNo']
                deviceId = log_array['data']['data'][0]['deviceId']
                if appKey == "9A174E6CF9AAD017" and happenTime_t >= actualOrderTime_t + offset:
                    i += 1
                    print ("%d\t %s\t %s\t %s\t %s\t" % (i, deviceId, outTradeNo, happenTime, actualOrderTime))
            except KeyError:
                print log_array['data']
