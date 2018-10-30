# FTP_download.py overview

This file downloads the file specified by the main script
using the path and host name given. In the event that a 
download fails, it will log the path and file name to a 
text file explained in the next section. It will also 
generate a log called download.log if a download fails and
results in an exception. The log will contain the exception
description. The moveFile function moved a file from the 
local directory to the specified location on the local file
system. This is used to mimic the directory structure on the
NOAA server from which we are retrieving the files.

# Explanation of FTP DL_MISSED_FTP function: 

* Target file names and directories will be placed in a
  text file called missingDaysNOAA.txt by the FTP script
  in the event that a download is missed or fails. The 
  format will be like the following 2 lines for each file:

	comp20170401.120000.nc
	/pub/mtpw2/data/201704/

  Where the first line is the name of the missed file and 
  the second line is the path to the file on the FTP server.
  After the script attempts to download the missed file, it
  will remove the text file from the local directory. 

## Testing DL_MISSED_FTP

* Simply make a text file containing the file name and path 
  in the format described above and call the function.


