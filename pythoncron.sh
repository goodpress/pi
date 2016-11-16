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
prog=` pgrep -fl "$1" | head -n1 | awk '{print $2}' `
if [[ $prog != "python3" ]]  ;then
	echo "$now  $1 is dead , start ... " >> $logFile
	which python3
	code=$?
	if [ $code -eq 0 ] ;then
		echo "will use pyhone3 "  >> $logFile
		python3 $1  >> $logFile   2>&1 & 
	else
		echo "$now check python3 installed ? " >> $logFile
	fi
else
	echo " $now skip   , prog : $prog" >> $logFile
fi

