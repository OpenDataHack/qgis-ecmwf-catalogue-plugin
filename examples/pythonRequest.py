 #!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
    
server = ECMWFDataServer()
    
server.retrieve({
    'dataset' : "interim",
    'time'    : "00",
    'date'    : "2013-09-01/to/2013-09-30",
    'step'    : "0",
    'type'    : "an",
    'levtype' : "sfc",   
    'param'   : "165.128/41.128",		#files that are downloaded, separated by / , .128 is a constat for dataset, number before it is type of data - naming list http://apps.ecmwf.int/codes/grib/param-db
    'grid'    : "0.75/0.75",
    'target'  : "testingData.grib"		#name of target file
    })
