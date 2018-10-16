import requests
import os
import shutil
import logging
from html.parser import HTMLParser
from requests.auth import HTTPBasicAuth

#parser used for retrieving filenames from the web page returned by
#asking for the folder that refers to a given day
class NASAHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        #we use a set here to prevent duplicates being added
        self.filesToGet = set()
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    url = attr[1]
                    if url[-2:] == "h5":
                        self.filesToGet.add(url)

def HTTP_DOWNLOAD_MISSED():
    logging.info("Getting missing HTTP files")
    if not os.path.exists("missingHTTP.txt"):
        return
    os.replace("missingHTTP.txt", "filesToGetHTTP.txt")
    missing = open("filesToGetHTTP.txt", "r")
    for line in missing.readlines():
        if line == '':
            continue
        params = str.split(line)
        HTTP_download(params[0], params[1], params[2])
    missing.close()
    os.remove("filesToGetHTTP.txt")
#download files from days enumerated in missingDaysNASA.txt
#which is created and added to automatically when DL_HTTP_NASA
#is called and can't retrieve files from a given day
def DL_MISSED_HTTP_NASA():
    #again using a set to prevent duplicates, though they shouldn't
    #occur through normal execution of this script
    logging.info("Getting missing NASA files")
    filesToDL = set()
    if not os.path.exists("missingDaysNASA.txt"):
        print("unable to find missingDaysNASA.txt. Returning")
        return
    os.replace("missingDaysNASA.txt", "daysToGetNASA.txt")
    missing = open("daysToGetNASA.txt", "r")
    for line in missing.readlines():
        dayToDL = line[:-1]
        logging.info(dayToDL)
        if dayToDL == '':
            continue
        filesToDL.add(dayToDL)
    missing.close()
    for date in filesToDL:
        DL_HTTP_NASA(date)
    os.remove("daysToGetNASA.txt")

#download the h5 file from a given day where date is specified
#as "YYYY.MM.DD" format
def DL_HTTP_NASA(date):
    #first we have to get the containing folder
    hostname = 'n5eil01u.ecs.nsidc.org'
    path = '/SMAP/SPL3SMP.005/' + date + '/'
<<<<<<< HEAD
    fullURL = "https://" + hostname + path
    logging.info(fullURL)
    logging.info('Getting listing of files from day: ' + date)
    r = requests.get(fullURL)
    #if the result of trying to retrieve a day is 404, then we
    #add it to days to try to get later and exit
    if r.status_code == 401:
        logging.error("Received 401: Unauthorized, verify ~/.netrc is present")
    if r.status_code == 404:
        logging.info("No files found for day: " + date + ", adding to missingDaysNASA.txt")
        missingDays = open("missingDaysNASA.txt", "a")
        missingDays.write(date + "\n")
        return
=======
    fullURL = "https://" + hostname + path		
    print(fullURL)
	
    username = os.environ['NASA_USER']
    password  = os.environ['NASA_PASS']
    
    sesRes = ""
	
    with requests.Session() as session:
        session.auth = (username, password)
        r1 = session.request('get', fullURL)
        r = session.get(r1.url, auth=(username, password))
        if r.ok:
            print('success')
            sesRes = r.text            
        elif r.status_code == 401:
            print("Received 401: Unauthorized, verify ~/.netrc is present")
            return
        #if the result of trying to retrieve a day is 404, then we
        #add it to days to try to get later and exit
        elif r.status_code == 404:
            print("No files found for day: " + date + ", adding to missingDaysNASA.txt")
            missingDays = open("missingDaysNASA.txt", "a")
            missingDays.write(date + "\n")
            return
        else:
            print("Failure!")
            return
    
>>>>>>> 5bc08d13787e942d12ee2d621122bf3c86a9a775
    #pass the html from the folder into our parser
    parser = NASAHTMLParser()
    parser.feed(sesRes)
    #pull the fileNames from that folder (those that end in h5)
    filesToDownload = parser.filesToGet
    for resourceName in filesToDownload:
        HTTP_download(hostname, path, resourceName, username, password)

#downloads the named resource from the defined host with the given path
def HTTP_download(host, path, resource, username, password):
    fullRequestURL = "https://" + host + path + resource
    outdir = "downloaded-files/" + host + path
<<<<<<< HEAD
    r = requests.get(fullRequestURL, stream=True)
    if r.status_code == 401:
        #unauthorized
        logging.critical("You do not have authorization to retrieve file from this server, verify your credentials are correct in ~/.netrc\n")
        return
    if r.status_code == 403:
        #forbidden, try https
        fullRequestURL = "https://" + host + path + resource
    r = requests.get(fullRequestURL, stream=True)
    if r.status_code == 404:
        #the resource wasn't found
        out = open("missingHTTP.txt", "a")
        out.write(host + " ")
        out.write(path + " ")
        out.write(resource + "\n")
        out.close()
        return
    if os.path.exists(outdir + "/" + resource):
        logging.info("Resource: " + resource + " has already been downloaded")
        return
    #download the resource by writing bytes out to the file
    with open(resource, 'wb') as fd:
        logging.info('Downloading File ' + resource + '\n')
        logging.info('|=', end='', flush=True)
        for chunk in r.iter_content(chunk_size=1024 * 1024 * 5):
            fd.write(chunk)
            logging.info('=', end='', flush=True)
        fd.close()
        logging.info('=|', flush=True)
    #verify the file downloaded is at least 100MB in size
    #because the files are usually ~250MB in size
    #if os.stat(resource).st_size < 1024*1024*100:
        #print('File size was smaller than expected, removing so we can try again later')
        #shutil.rmtree(outdir)
    #move the file to its appropriate folder on filesystem
    os.makedirs(outdir, exist_ok=True)
    os.replace(resource, outdir + "/" + resource)
=======
    
    with requests.Session() as session:
        session.auth = (username, password)
        r1 = session.request('get', fullRequestURL)
        r = session.get(r1.url, stream=True, auth=(username, password))
        if r.status_code == 401:
            #unauthorized
            print("You do not have authorization to retrieve file from this server, verify your credentials are correct in ~/.netrc\n")
            return
        elif r.status_code == 403:
            #forbidden, try https
            fullRequestURL = "https://" + host + path + resource
            r = requests.get(fullRequestURL)
            if r.status_code == 404:
                #the resource wasn't found
                out = open("missingHTTP.txt", "a")
                out.write(host + " ")
                out.write(path + " ")
                out.write(resource + "\n")
                out.close()
                return
        elif os.path.exists(outdir + "/" + resource):
            print("Resource: " + resource + " has already been downloaded")
            return
        else:
            #download the resource by writing bytes out to the file
            print('Downloading File ' + resource + '\n')
            file = open(resource, 'wb')
            for chunk in r.iter_content(100000):
                file.write(chunk)
            file.close()
            
        #move the file to its appropriate folder on filesystem
        os.makedirs(outdir, exist_ok=True)
        os.replace(resource, outdir + "/" + resource)
>>>>>>> 5bc08d13787e942d12ee2d621122bf3c86a9a775

#example of using this module to download data for a given day as well
#as all days that have been missed up to this point
#DL_MISSED_HTTP_NASA()
#DL_HTTP_NASA("2018.02.28")
#HTTP_download("n5eil01u.ecs.nsidc.org/", "SMAP/SPL3SMP_E.001/2018.02.28/", "SMAP_L3_SM_P_E_20180228_R15181_001.h5")
#HTTP_DOWNLOAD_MISSED()
