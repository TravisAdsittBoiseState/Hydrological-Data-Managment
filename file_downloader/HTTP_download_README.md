# HTTP_download.py overview

This script is responsible for downloading files via HTTP protocol.
The main script calls in using the hostname, the path to the
resource, and the name of the resource. A special case has been made
for retrieving files from the NSIDC because the filenames are non-
determinable.

##HTTP_download(host, path, resource)
this function is responsible for downloading files from an HTTP
server. The path parameter is specified from the top level of the
web server, the resource name must be exact, as wildcards/regex
are not allowed in HTTP requests.
If a request returns a 404 (not found) response, then the parameters
are logged in "missingHTTP.txt"
###Example
To request a resource at domain:
    https://www.azlyrics.com/lyrics/rickastley/nevergonnagiveyouup.html

You would call like so:
    HTTP_download("www.azlyrics.com", "/lyrics/rickastley", "nevergonnagiveyouup.html")

##HTTP_DOWNLOAD_MISSED()
This function is responsible for downloading HTTP files that have
been logged as missing in "missingHTTP.txt" Each line contains the
parameters required for calling HTTP_download(). This can also be
used to force download of files that are not currently in
config.json, or that should only be downloaded once instead of on
an interval.

###Example
To retrieve missing files, simply call
    HTTP_DOWNLOAD_MISSED()

##DL_HTTP_NASA(date)
This function is responsible for downloading the h5 file from NASA/
NSIDC for a given day. The only parameter required is the date in
format: "YYYY.MM.DD". The web interface for the NSIDC dataset shows
a webpage for each folder present. I leveraged this by retrieving
the HTML for the folder representing the day. The HTML parser in
this module is used to find links to h5 files (of which there should
only be one) and passes the filename to HTTP_download. If a file is
not found (ie 404 response) the date is stored in
"missingDaysNASA.txt" so it can be reattempted later.

It is important to note that in order to retrieve files from NSIDC,
a username and password are required. The HTTP module assumes that
the credentials are stored in ~/.netrc. The format for .netrc should
be:
    machine <hostname> login <username> password <password>

Each line can contain credentials for a different host, so credenti-
als can be stored for any number of hosts at once.

###Example
To retrieve the NASA/NSIDC file for January 8, 2018, call
    DL_HTTP_NASA("2018.01.08")

##DL_MISSED_HTTP_NASA()
This function is used for downloading NASA/NSIDC files that have
been missed previously. It renames "missingDaysNASA.txt", reads out
all of the dates inside it, storing them into a set to remove dupli-
cates and then downloads them using DL_HTTP_NASA. This function can
also be used to manually force the download of data for a given day.
If a file is missed again, it is stored back into "missingDaysNASA.
txt".
