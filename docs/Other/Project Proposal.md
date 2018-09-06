#Project Proposal


Contacts: 

Cathie Olschanowsky <catherineolschan@boisestate.edu>

Lejo Flores <lejoflores@boisestate.edu>


Problem Statement: NOAA and NASA provide access to time-series satellite observations and derived estimates of geophysical parameters for research and operational purposes. This data is organized and saved in specific servers; the data show up periodically on specified intervals. The location and organization of the files are well known. Researchers usually only need specific subsets of the original data. The problem is that manually retrieving the data is time consuming and error prone. Moreover, because of the volumes of data retrieved from the observational system, data are typically kept in rolling archives that can be accessed through web services for only a short period of time. After some period, data are typically written to tape and must be obtained via special request. 


Solution Proposal: We propose a service that can be deployed locally by a researcher. The server will periodically download relevant data from the near past. A database should be kept so that the researcher can quickly discover which files are present/absent from the local collection. Additionally, a subsetting service should be available that allows the researcher to subset a file or set of files. All original data should be kept and the subsetting should result in copies. 


Example data collections of particular interest include: 

NASA Soil Moisture Active Passive (SMAP) Enhanced L3 Radiometer Global Daily 9 km EASE-Grid Soil Moisture, Version 1: https://nsidc.org/data/SPL3SMP_E/versions/1

Total Precipitable Water derived from a number of operational weather satellites at hourly resolutions: ftp://ftp.ssec.wisc.edu/pub/mtpw2/data/


Most data will be saved in netcdf or HDF5 format. This will be important for subsetting. The data transfer portion of the service should be the highest priority.



https://n5eil01u.ecs.nsidc.org/SMAP/SPL3SMP_E.001/


Target location: Ask Steve in research computing 10TB

Data Queries: earliest date, latest date, missing or erroneous data


Authentication

Retrieval - automatic (daemon or cron)

Queries


NOAA Data:

Hourly


Panoply is a good tool to view the data if you want to
