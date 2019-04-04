# 计算地址经纬度
import requests
from math import radians, cos, sin, asin, sqrt
EARTH_RADII = 6371 # 地球平均半径，单位为公里
def geocode(address):
    parameters = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    # print(address + "的经纬度：", answer['geocodes'][0]['location'])
    lon = float(answer['geocodes'][0]['location'].split(',')[0])
    lat = float(answer['geocodes'][0]['location'].split(',')[1])
    return lon, lat


def getdistqance(address1, address2):
    lon1,lat1 = geocode(address1)
    lon2,lat2 = geocode(address2)
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = EARTH_RADII
    print(c * r * 1000, "m")
    # return c * r * 1000

if __name__ == '__main__':
    address1 = '上海市徐汇区桂箐路靠近华鑫天地'
    address2 = '北京市海淀区北医三院'
    getdistqance(address1, address2)
