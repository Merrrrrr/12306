# -*- coding: UTF-8 -*-
import requests
import city
import json


def getAll(from_station, to_station, train_date):
    # url请求参数
    from_station_code = city.getCityCode(from_station)
    to_station_code = city.getCityCode(to_station)
    if from_station_code is None:
        print("出发地错误")
        return
    if to_station_code is None:
        print("目的地错误")
        return

    # http请求头
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_uab_collina=160076245128221049107629; JSESSIONID=D03C615BE51149C2B568380550C501E7; BIGipServerotn=149946890.64545.0000; RAIL_EXPIRATION=1601087717282; RAIL_DEVICEID=Jit4ZVpNrIqr51NBT5cXXsJeBan3wYcCO7Owqd0vtJgvUI_7ZOubYJY3rBgrgiaTUTUpYXNjk7vw-40AKzvRAl840hC4TqdQ1fzylfnxopynyz1gv9vKpdb6k3_qUQpbHKVGmlR3OHt6XIEjtgNI1qci9xKGW5wA; BIGipServerpool_passport=300745226.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2020-09-22; _jc_save_toDate=2020-09-22; _jc_save_wfdc_flag=dc',
        'Host': 'kyfw.12306.cn',
        'If-Modified-Since': '0',
        'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E4%B8%8A%E6%B5%B7,SHH&date=2020-09-22&flag=N,N,Y',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (
        train_date, from_station_code, to_station_code)

    # print(from_station_code,to_station_code)    
    response = requests.get(url, headers=headers)
    # 不能判断response.status_code == 200 有时会不返回数据，但是状态码还是200
    if response.content:
        response = response.content.decode('utf-8')

        # text包含BOM字符 需要去掉，否则有时报错
        if response.startswith(u'\ufeff'):
            response = response.encode('utf8')[3:].decode('utf8')

        dictInfo = json.loads(response)

        trainList = dictInfo['data']['result']

        # print("车次\t出发站\t到达站 出发时间 到达时间 历时 商务座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 ")
        result = []
        for i in trainList:
            list = i.split("|")
            checi = list[3]
            chufa = city.getCityName(list[6])
            mudi = city.getCityName(list[7])
            ftime = list[8]
            dtime = list[9]
            time = list[10]
            swz = list[32]
            zy = list[31]
            ze = list[30]
            gr = list[21]
            rw = list[23]
            srrb = list[33]
            yw = list[28]
            rz = list[24]
            yz = list[29]
            wz = list[26]
            result.append((checi, chufa, mudi, ftime, dtime, time, swz, zy, ze, gr, rw, srrb, yw, rz, yz, wz))
        return result


# print(getAll("北京","石家庄","2019-12-20"))
if __name__ == "__main__":
    from_station = input('请输入始发地:')
    to_station = input('请输入目的地:')
    train_date = input('请输入日期:')

    list = getAll(from_station, to_station, train_date)
    for item in list:
        print(item)
