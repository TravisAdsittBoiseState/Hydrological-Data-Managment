#!/bin/bash
## This is the script that chron will run every hour.
## The variable LOGFILE below in main may need to be changed,
## but only if the user desires a different logfile name or location.
## This shell script checks to see if our main.py program is running,
## If found running, it kills the program, then re-starts it
## If not running, it simply starts the program and ensures it is running

# kills the process
function killPID() {
 kill -9 "$PNUM"
}

#gets the PID of the process
function getPID()
{
    local  mypid=$(pgrep -f "$PROC")
    echo "$mypid"
}

#starts the process (in background)
function start_process() {
    python3 $PROC &
    #nohup?#setsid?#disown?#exec?
}

#checks to see if main.py is running
function check_if_running() {
  PNUM=$(pgrep -f "$PROC")
  local retval=0
[ -n "$PNUM" ] && echo 1 || echo 0 #if PNUM is not null

}


### MAIN ###

#changes into main project directory
cd ..
#process path & name
PROC="./main.py"
#Logfile path & name
LOGFILE="./cronjob/ProcessStart-upLog.txt"
#process id (PID)
PNUM= #originally null
#timestamp
ts=`date +%F%t%T`
echo -e "$ts:\t --------------------------------" >> $LOGFILE
echo -e "$ts:\t starting process start-up script" >> $LOGFILE
Running=$(check_if_running)
echo $Running
if [ "$Running" = "1" ]
then
	echo "Process is running ..."
	echo "getting PID ..."
	PNUM=$(getPID)
	ts=`date +%F%t%T`
	echo -e "$ts:\t PID $PNUM found running $PROC." >> $LOGFILE
	echo -e "$ts:\t attempting to Kill Process ..." >> $LOGFILE
	killPID
	sleep 2
	Running=$(check_if_running)
	if [ "$Running" = "1" ]
	then
		ts=`date +%F%t%T`
		echo -e "$ts:\t FAILED TO KILL $PROC. Unknown ERROR, I'm Sorry Dave, I'm afraid I can't do that.  Exiting Script." >> $LOGFILE
		exit 1
	else
		ts=`date +%F%t%T`
		echo -e "$ts:\t KILLED $PROC.  Process was found running." >> $LOGFILE
	fi
	sleep 2
else
	echo "Process is NOT running ..."
fi

#variable to keep track of start-up attempts
attemptNum=1
Running=$(check_if_running)
while [ "$Running" == "0" ] && [ $attemptNum -lt 4 ] #incremented loop only tries a finite number of times and logs a fail. / breaks on success.
do
	echo "Starting Process ..."
	ts=`date +%F%t%T`
	echo -e "$ts:\t attempting launch $attemptNum of $PROC" >> $LOGFILE
	start_process
	PNUM=$(getPID)
	Running=$(check_if_running)
	if [ "$Running" = "1" ]
	then
		ts=`date +%F%t%T`
		echo -e "$ts:\t launch $attemptNum succeeded." >> $LOGFILE
		echo "echo launch $i succeeded."
		echo -e "$ts:\t $PNUM running $PROC" >> $LOGFILE
		echo "$PNUM running $PROC"
	else
		ts=`date +%F%t%T`
		echo -e "$ts:\t launch $attemptNum FAILED." >> $LOGFILE
		echo "echo launch $attemptNum FAILED."
		echo -e "$ts:\t $PROC not running." >> $LOGFILE
		echo "$PROC not running."
	fi
	attemptNum=$[$attemptNum+1]
done

#if out of loop and still not running...
if [ "$Running" = "0" ]
then
	echo -e "$ts:\t FAILED TO START $PROC. Unknown ERROR (check file permissions?), I'm Sorry Dave, I'm afraid I can't do that.  Exiting Script." >> $LOGFILE
	exit 1
fi

#wait for started processes to finish before exiting script
wait

ts=`date +%F%t%T`
echo -e "$ts:\t completed process start-up script" >> $LOGFILE
