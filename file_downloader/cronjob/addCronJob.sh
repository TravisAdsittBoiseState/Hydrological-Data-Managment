#!/bin/bash
##Script adds the logScript.sh file to run hourly as a cron job
DIR=$(pwd)
FILE="./startProcess.sh"
echo "Adding cron job to pc"
sleep 2
crontab -l | { cat; echo "0 * * * * cd $DIR && $FILE"; } | crontab -
result=$?

if [ "$result" = "0" ]
then echo "SUCCESS! job $FILE added"
else echo "error - adding cron job failed!"
fi
sleep 1
echo "crontab listing:"
crontab -l
echo ""
