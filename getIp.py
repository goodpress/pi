#/bin/bash/python3
from uuid import getnode as get_mac
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import socket , fcntl, socket, struct
import time,os,subprocess



def shellGetIp():
    command="ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/' "
    tmpIp=subprocess.call(command, shell=True)
    print('command result:' ,tmpIp)
    return tmpIp
def getCurTime():
    ISOTIMEFORMAT='%Y-%m-%d %X'
    readTime=time.strftime(ISOTIMEFORMAT,time.localtime())
    return readTime
def getHostName():
    return socket.gethostbyname(socket.gethostname()) 
def getFqdn():
    return socket.gethostbyname(socket.getfqdn()) 
def post(url,jsonData,cookieData):
    request = Request(url, urlencode(jsonData).encode())
    return urlopen(request).read().decode() 
def getMacAddress():
    return get_mac()
def get_ethernet_address():
    ip=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    return ip



recorderApi='http://publish.52shangou.com/o2o/shandian_pm/test/logaddress.php?act=recorder'
data= {
        'gethostname_ip':getHostName() ,
        'getfqdn_ip': getFqdn(),
        'ip': get_ethernet_address(),
        'mac_address':getMacAddress(),
        'pi_time':getCurTime(),
        }
cookies = {
        'php': 'a',
        'huo': 'a', 
        'phpbb2mysql_sid': '5b2',
        }

print ('will post data:' ,data)
print('received data :' ,post(recorderApi,data,cookies))

