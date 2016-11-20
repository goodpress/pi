#!/bin/bash
logFile="/var/log/sdb/pythonCron.log"
now="$(date +"%Y_%m_%d_%H:%M:%S")"
echo "status ============= start" >> $logFile
ps -ef |grep python  >> $logFile 
echo "status ============= end" >> $logFile

if [[ ! -f "$1" ]] ;then
	echo "$now error , $1 does not exist " >> $logFile 
	exit 1
fi
prog=` pgrep -fl "$1" |  awk '{print $2}' | grep "python3" | wc -l  `
if [[ $prog -lt 1 ]]  ;then
	echo "$now  $1 is dead , start ... " >> $logFile
	which python3
	code=$?
	if [ $code -eq 0 ] ;then
		echo "will use pyhone3 "  >> $logFile
		python3 $1  >> $logFile   2>&1 & 
	else
		echo "$now check python3 installed ? " >> $logFile
	fi
elif [[ $prog -eq 1 ]] ;then
	echo " $now skip   , prog : $prog is ok" >> $logFile
else
	echo " $now WARNING   , prog : $prog is more than one !" >> $logFile
fi

