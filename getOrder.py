#!/bin/bash/python3
from  urllib.request  import urlopen
import json,os,time
apiUrl='http://publish.52shangou.com/o2o/shandian_pm/test/api.php'
voicePath='/usr/local/voice/voice.mp3'
timeInterval='10'
voiceTime='2'
ISOTIMEFORMAT='%Y-%m-%d %X'
def sleeptime(hour,min,sec):
        return hour*3600 + min*60 + sec;
timeInterval = sleeptime(0,0,5);
while True:
    readTime=time.strftime(ISOTIMEFORMAT,time.localtime())
    print(readTime ,'============')
    u=urlopen(apiUrl)
    resp=json.loads(u.read().decode('utf-8'))
    print(' resp str:' , resp)
    if resp['order'] == True :
        print('had order')
        os.system(' omxplayer -b -o local ' + voicePath)
        #os.system(' aplay ' + voicePath)
        #os.system(' omxplayer -o hdmi ' + voicePath)
        print('play finsih')
    time.sleep(timeInterval)
