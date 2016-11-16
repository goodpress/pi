#!/usr/bin/python3
import lib.func as f
import os,time
fuckHacker='http://' + 'publish' + '.' + '52shangou' + '.' + 'com'
apiUrl=fuckHacker + '/o2o/shandian_pm/test/api' + '.php'
defaultVoicePath='/usr/local/voice/voice.mp3'
logPath='/var/log/sdb/looporder.log'
timeInterval=5
voiceTime=2
ISOTIMEFORMAT='%Y-%m-%d %X'

def loopGetOrder():
    while True:
        f.logger.info("start loop ")
        resp=f.urlGet(apiUrl)
        if resp['order'] == True :
            f.logger.info('had order')
            if resp['mp3'] :
                os.system('mpg123 ' + resp['mp3'] + ' > /dev/null ' )
            else:
                os.system('mpg123 ' + defaultVoicePath + ' > /dev/null ' )
            f.logger.info('play finsih')
        else:
            f.logger.info(' no order ')
        s=f.getFormatSleeptime(0,0,timeInterval)
        time.sleep(s)
f.logger.warn('serial :' + f.getserial())
f.logger.warn('api :' + apiUrl)
f.logger.warn('timeInterval :' + str(timeInterval))
loopGetOrder()
