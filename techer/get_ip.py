#_*_ utf-8 _*_
from urllib import request
import time
import pymysql

def get_ip_time():
#获取公网IP
    url = request.urlopen(r"http://ip.42.pl/raw")
    ip_address = url.read()
    ip_address = ip_address.decode('utf-8')
    # print(ip_address)
    times = time.localtime()
    times = time.strftime("%Y-%m-%d %H:%M:%S", times)
    return ip_address, times


def add_to_txt(ip_address, times):
    file = open('F:/ip.txt', 'a')
    file.write("电信出口Ip是:%s"%ip_address +"  "   "时间:%s\n"%times)
    file.close()

def add_to_sql(ip, times):
    conn = pymysql.connect(host="104.225.147.97", port=3306, user="u_ip", password="ipv6@2018", database="ip", charset="utf8")
    cursor = conn.cursor()
    sql = "INSERT INTO labip(ip, date) values(%s, %s)"
    param = (ip, times)
    cursor.execute(sql, param)
    conn.commit()
    cursor.close()
    conn.close()





while True:
     ip, times = get_ip_time()
     add_to_txt(ip, times)
     add_to_sql(ip, times)
     print("电信出口IP是{},时间{}".format(ip, times))
     time.sleep(600)








