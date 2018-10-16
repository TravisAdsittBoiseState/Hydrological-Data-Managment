#!/usr/bin/python

import os
from datetime import datetime
from FTP_download import *
from HTTP_download import *
import json
from pprint import pprint
import logging

#Setting up Logging File
logging.basicConfig(filename='cronlog.log',level=logging.DEBUG)


#SSECDir = "/pub/mtpw2/data/"
#SSECHost = "ftp.ssec.wisc.edu"

#lets pull out our year, month, day, hour, min (UTC)
dateNow = datetime.utcnow().date()
timeNow = datetime.utcnow()
year = '{:04d}'.format(dateNow.year)
month = '{:02d}'.format(dateNow.month)
day = '{:02d}'.format(dateNow.day - 1)
hour = timeNow.strftime('%H')
minute = timeNow.strftime('%M')

def main():
	if os.path.exists("config.json"):
		logging.info("Reading config file.")
		config = json.load(open('config.json'))
		for resource in config:
			#check if this lines up with our specified interval
			if (int(hour) % int(resource["interval"]) != 0): #if this-hour MOD config-interval is not = 0, then skip this download
				continue
			#determine if this is an http or ftp
			if (resource["protocol"] == "ftp"):
				#first, lets get any files that may have been missed
				DL_MISSED_FTP()
				#calculate dir and filenames based on date values
				dir = putDateInString(resource["directory"])
				fileName = putDateInString(resource["fileName"])
				FTP_download(resource["hostName"], dir, fileName)
			elif (resource["protocol"] == "http"):
				if (resource["hostName"] == "n5eil01u.ecs.nsidc.org"): #this is a special case for NASA files
					checkForNASAFile()
				else:
					#first, lets get any files that may have missed
					HTTP_DOWNLOAD_MISSED()
					#calculate dir and filenames based on date values
					dir = putDateInString(resource["directory"])
					fileName = putDateInString(resource["fileName"])
					#localDir = "./" + resource["hostName"] + dir
					HTTP_download(resource["hostName"], dir, fileName)

	#checkForTopDirs()
	#checkForSSECFile()

def putDateInString(string):
	myStr = ""
	if (string.find("#")):
		parts = string.split("#")
		for part in parts:
			if (part != ""):
				if (part == "yyyy"):
					myStr += year
				elif (part == "mm"):
					myStr += month
				elif (part == "dd"):
					myStr += day
				elif (part == "hh"):
					myStr += hour
				else:
					myStr += part
	else:
		return string
	return myStr

#NASA files are special case, the file suffix ("...R15181_002") changes every few months and is unpredictable
#We handle this in the HTTP script with a special function to parse the site's page and determine the name of today's file
def checkForNASAFile(): 
	NASADir = "/SMAP/SPL3SMP_E.001" 
	NASAHost = "n5eil01u.ecs.nsidc.org"
	#just need to see if the directory exists in this case, if not, we dont have our h5 file either.
	NASASubFolder = "./downloaded-files/" + NASAHost + NASADir + "/" + year + "." + month + "." + day
	logging.info("Checking for nasa sub folder: " + NASASubFolder + "\n")
	if os.path.exists(NASASubFolder):
		logging.info("Looks like the NASA sub folder already exists, no need to fetch its contents\n")
	else:
		#https://n5eil01u.ecs.nsidc.org/SMAP/SPL3SMP_E.001/2018.01.13/SMAP_L3_SM_P_E_20180113_R15181_002.h5
		logging.info("NASA subfolder for today does not exist. Attempting download.\n")
		#check for missed files first
		DL_MISSED_HTTP_NASA()
		#check for todays file
		DL_HTTP_NASA(year + "." + month + "." + day)
		
#______________________________________________________________________________
#NOT USING ANYMORE

#def checkForTopDirs():
	#if not os.path.isdir("./NASA/" + NASADir):
		#print("MAKING NASA DIR")
		#os.makedirs("./NASA/" + NASADir)

	#if not os.path.isdir("./SSEC/" + SSECDir):
		#print("MAKING SSEC DIR")
		#os.makedirs("./SSEC/" + SSECDir)

#def checkForSSECFile():
	#ftp://ftp.ssec.wisc.edu/pub/mtpw2/data/201802/comp20180201.000000.nc
	#SSECSubFolder = SSECDir + year + month + "/"
	#print("Checking for ssec sub folder: " + SSECSubFolder)

	#see if our local directory exists for this month, if not create it
	#if not os.path.exists("./SSEC" + SSECSubFolder):
		#print("Creating SSEC local sub folder")
		#os.makedirs("./SSEC" + SSECSubFolder)

	#SSECFileName = "comp" + year + month + day + "." + hour + "0000.nc"
	#print("Here's the SSEC file name: " + SSECFileName)

	#Need to pass Aaron hostName, hostDir, fileName, local directory to store in (SSECDir)
	#if DL process returns true, move the file into the correct dir
	#if (DL_FTP(SSECHost, SSECSubFolder, SSECFileName)):
		#moveFile(SSECFileName, "./SSEC" + SSECSubFolder)



if __name__== "__main__":
	main()
