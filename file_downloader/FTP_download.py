from ftplib import FTP
import ftplib
import time
from datetime import datetime
import shutil
import logging
import os

#Script downloads specified file from
#the specified directory and places it
#on the local filesystem.
def DL_MISSED_FTP():
    logging.info("Getting missing FTP files")
    fileNames = []
    filePaths = []
    hostNames = []
    if not os.path.exists("missingFTP.txt"):
        return
    os.replace("missingFTP.txt", "daysToGetFTP.txt")
    missing = open("daysToGetFTP.txt", "r")
    
    lines = missing.readlines()
    for i in range(0, len(lines), 3):
        #1st line will be filename
        fileName = lines[i][:-1]
        fileNames.append(fileName)
        #2nd line is directory
        filePath = lines[i+1][:-1]
        filePaths.append(filePath)
        #3rd line is hostname
        hostName = lines[i+2][:-1]
        hostNames.append(hostName)
    missing.close()

    for i in range(0, len(hostNames)):
        fileName = fileNames[i]
        filePath = filePaths[i]
        hostname = hostNames[i]
        logging.info("Getting missing file: \n  -  " + hostName + filePath + fileName)
        FTP_download(hostname, filePath, fileName)
        #DL_FTP(hostname, filePath, fileName)
    os.remove("daysToGetFTP.txt")

def DL_FTP(hostname, hostdir, filename):
   
    try:
        #open logging file just in case
        logf = open("download.log", "w")
        logging.info("FTP downloader starting up")
        #domain name or server ip
        ftp = FTP(hostname)
        #login to site, generic credentials
        logging.info("Logging into: %s" %(hostname))
        ftp.login()
        logging.info("Navigating to: %s" %(hostdir))
        ftp.cwd(hostdir)
        # Switch to Binary mode A to switch back to ASCII
        ftp.sendcmd("TYPE i")    
        #Get file size
        filesize = ftp.size(filename)
        # returns None if there was an error
        if filesize == None:
            logging.error("FileSize Error, aborting download...")
            return 0
        else:
            logging.info("Size of file: %s" %(filesize)) 
            logging.info("Downloading file: %s" %(filename))
            #Open file
            file = open(filename, 'wb')
            #Download file
            ftp.retrbinary('RETR %s' % filename, file.write) 
            #If no exceptions, download complete
            logging.info("Download complete!") 
    except ftplib.error_perm as e:
        logf.write("Failed to download {0}: {1}\n".format(str(filename), str(e)))
        #if download failed, put file name in download backlog
        if e.args[0][:3] == '550':
            missingDays = open("missingFTP.txt", "a")
            missingDays.write(filename + "\n"+hostdir+"\n"+hostname+"\n")
            return 0
    return 1

#Move the downloaded file to the appropriate
#directory, this is just a simple example of
#how that can be done in python3
def moveFile(filename, path):
    logging.info("Moving file to: %s" %(path))
    #second param needs to be path from current directory not including '.'
    # i.e.: dirname/filename (has to include filename) "testMove/comp20161001.000000.nc"
    shutil.move(filename, path + "/" + filename)
    #If no exceptions, success!
    logging.info("Move successful")
	
#Helper function for handling FTP DL's
def FTP_download(hostName, directory, fileName):
    if (DL_FTP(hostName, directory, fileName)):
        if not os.path.exists("./" + hostName + directory):
            logging.info("Creating local sub folder")
            os.makedirs("./downloaded-files/" + hostName + directory, exist_ok=True)
        moveFile(fileName, "./downloaded-files/" + hostName + directory)


#Code below is test code, uncomment to test!
#DL_FTP("ftp.ssec.wisc.edu", "/pub/mtpw2/monkeynuts/201803/","Bogus_filename")
#DL_MISSED_FTP("ftp.ssec.wisc.edu")
#moveFile()
