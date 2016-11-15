#!/bin/bash
num=`ps -aux |grep getOrder.py | wc -l`
logFile="/var/log/sdb/getOrder.log"
now="$(date +"%Y_%m_%d_%H:%M:%S")"
echo "$now run  getOrder.sh " >> $logFile
if [[ $num -eq 1 ]] ;then
	echo "$now will start getOrder.py by shell " >> $logFile
	which python3
	code=$?
	if [[ $code -eq 0 ]] ;then
		python3 /usr/local/scripts/getOrder.py  >>  /var/log/sdb/getOrder.log 
	else
		if [[ -f "/usr/bin/python3" ]] ;then
			/usr/bin/python3 /usr/local/scripts/getOrder.py  >>  /var/log/sdb/getOrder.log 
		else
			echo "error ,python3 is not exist " >> $logFile
		fi
	fi
else
	echo " $now find getOrder.py  num :$num ,skip" >> $logFile
fi

