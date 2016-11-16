#/usr/bin/python3
import lib.func as f
import time
recorderApi='http://publish.52shangou.com/o2o/shandian_pm/test/logaddress.php?act=recorder'
timeInterval=120
data= {
        'hostname_ip':f.getHostName() ,
        'fqdn_ip': f.getFqdn(),
        'pub_ip': f.getPubIp(),
        'ip': f.getEthernetAddress(),
        'mac_address':f.getMacAddress(),
        'pi_time':f.getCurTime(),
        'serial':f.getserial(),
        'cpu_temp':f.getCpuTemp(),
        }
cookies = {
        'php': 'a',
        'huo': 'a', 
        'phpbb2mysql_sid': '5b2',
        }

while True:
    f.logger.info('start loop ...')
    f.logger.info ('will post data:' + str(data))
    #f.logger.info ('received data :' + str(f.urlPostJson(recorderApi,data,cookies))
    f.logger.info ('received data :' + str(f.urlPostJson(recorderApi,data,cookies)))
    time.sleep(f.getFormatSleeptime(0,0,timeInterval))
