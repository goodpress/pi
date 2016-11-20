#/usr/bin/python3
from uuid import getnode as get_mac
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import socket , fcntl, socket, struct
import time,os,subprocess,json
import lib.hlogger as hl

logger = hl.function_logger(hl.logging.DEBUG, hl.logging.DEBUG)
def getPubIp():
    command="ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/' "
    stdoutdata = subprocess.getoutput(command)
    #logger.info("stdoutdata: " + stdoutdata.split()[0])
    logger.info(command  +  "---> stdoutdata: " + stdoutdata)
    return stdoutdata
def getCurTime():
    ISOTIMEFORMAT='%Y-%m-%d %X'
    return time.strftime(ISOTIMEFORMAT,time.localtime()) 
def getHostName():
    return socket.gethostbyname(socket.gethostname()) 
def getFqdn():
    return socket.gethostbyname(socket.getfqdn()) 
def getMacAddress():
    return get_mac()
def getEthernetAddress():
    ip=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    return ip

def getFormatSleeptime(hour,min,sec):
        return hour*3600 + min*60 + sec
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
  return cpuserial

def urlGet(url):
    u=urlopen(url)
    resp=json.loads(u.read().decode('utf-8'))
    logger.info( 'url : ' + url + ' resp : ' + str(resp))
    return resp
def urlPost(url,jsonData,cookieData):
    request = Request(url, urlencode(jsonData).encode())
    return urlopen(request).read().decode() 
def urlPostJson(url,jsonData,cookieData):
    request = Request(url, urlencode(jsonData).encode())
    respStr=urlopen(request).read().decode() 
    jsonObj=json.loads(respStr)
    return jsonObj

def getCpuTemp():
    command="vcgencmd measure_temp"
    stdoutdata = subprocess.getoutput(command)
    #logger.info("stdoutdata: " + stdoutdata.split()[0])
    logger.info(command + " -->stdoutdata: " + stdoutdata)
    return stdoutdata
def getLoad():
    command="uptime | awk -F 'load' '{print $2}'"
    stdoutdata = subprocess.getoutput(command)
    #logger.info("stdoutdata: " + stdoutdata.split()[0])
    logger.info(command + " -->stdoutdata: " + stdoutdata)
    return stdoutdata
