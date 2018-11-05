#_*_ utf-8 _*_
from urllib import request
def get_ip():
#获取公网IP
    url = request.urlopen(r"http://ip.42.pl/raw")
    ip_address = url.read()
    ip_address = ip_address.decode('utf-8')
    print(ip_address)


get_ip()


# from urllib import request
#
# # 获取外网IP
# def get_out_ip():
#     url = r'http://1212.ip138.com/ic.asp'
#     r = request.urlopen(url)
#     txt = r.text
#     ip = txt[txt.find("[") + 1: txt.find("]")]
#     print('ip:' + ip)
#     return ip
#
# get_out_ip()


