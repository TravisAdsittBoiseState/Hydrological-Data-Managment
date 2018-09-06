## Team Name: GeoMiners

## Sponsor Name: Cathie Olschanowsky and Lejo Flores

## Project Description:
We propose a service that can be deployed locally by a researcher. The server will periodically download relevant data. A database should be kept so that the researcher can quickly discover which files are present/absent from the local collection. Additionally, a subsetting service should be available that allows the researcher to subset a file or set of files. All original data should be kept and the subsetting should result in copies.

## Team Members:

Last Name       | First Name      | GitHub User Name     | Scrum Role
--------------- | --------------- | -------------------- | ---------------
Barclay         | Logan           | loganbarclay         | Developer
Bell            | Joe             | joeb-bsu             | Product Owner
Cullings        | Patrick         | pcullings            | Developer
Hetz            | Benjamin        | BenjaminHetz         | Developer
McLellen        | Chris           | chrismclellen        | Scrum Master
Whetzel         | Aaron           | awhetzel             | Developer

## Team Velocity:

Sprint | Estimated Velocity | Actual Velocity
------ | ------------------ | ---------------
   1   | 20                 | 20
   2   | 21                 | 21
   3   | 0                  | 10
   4   | 21                 | TBD
   5   | TBD                | TBD
   
## Config File Format:

The config.json file is parsed by main.py. It contains an array of host objects. Each host object contians the following parameters:
------ | 
hostName: contains the url address for the resource   
interval: frequency in which the files should be retrieved (specified in hours)    
protocol: either ftp or http
directory: the host directory path *with optional regular expression formatting to insert year, month, day, hour
filename: the file name *with optional regular expression formatting to insert year, month, day, hour

*to insert the year, inject #yyyy# into the directory of filename

*to insert the month, inject #mm# into the directory of filename

*to insert the day, inject #dd# into the directory of filename

*to insert the hour, inject #hh# into the directory of filename


Here is an example config file:
[

{

"hostName": "ftp.ssec.wisc.edu",

"interval":"1",

"protocol": "ftp",

"directory": "/pub/mtpw2/data/#yyyy##mm#/",

"fileName": "comp#yyyy##mm##dd#.#hh#0000.nc"

},

{

"hostName": "n5eil01u.ecs.nsidc.org",

"interval":"24",

"protocol": "http",

"directory": "/SMAP/SPL3SMP_E.001/#yyyy#.#mm#.#dd#/",

"fileName": "SMAP_L3_SM_P_E_#yyyy##mm##dd#_R15181_002.h5"

},

{

"hostName": "www.orimi.com",

"interval":"1",

"protocol": "http",

"directory": "/",

"fileName": "pdf-test.pdf"

}

]




http://cs.boisestate.edu/~bdit/GitHubAutoGrader/CS471F17ScrumLinterReports/CS471-F17-MAD_CZ8Ty6S0TEm2NzDngZQQEf00EcDRmkONUuIdVPyD/
