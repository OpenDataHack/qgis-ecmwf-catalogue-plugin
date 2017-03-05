#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": "2004-01-01/2004-01-02/2004-01-03/2004-01-04/2004-01-05/2004-01-06/2004-01-07/2004-01-08/2004-01-09/2004-01-10/2004-01-11/2004-01-12/2004-01-13/2004-01-14/2004-01-15/2004-01-16/2004-01-17/2004-01-18/2004-01-19/2004-01-20/2004-01-21/2004-01-22/2004-01-23/2004-01-24/2004-01-25/2004-01-26/2004-01-27/2004-01-28/2004-01-29/2004-01-30/2004-01-31/2004-02-01/2004-02-02/2004-02-03/2004-02-04/2004-02-05/2004-02-06/2004-02-07/2004-02-08/2004-02-09/2004-02-10/2004-02-11/2004-02-12/2004-02-13/2004-02-14/2004-02-15/2004-02-16/2004-02-17/2004-02-18/2004-02-19/2004-02-20/2004-02-21/2004-02-22/2004-02-23/2004-02-24/2004-02-25/2004-02-26/2004-02-27/2004-02-28/2004-02-29/2004-03-01/2004-03-02/2004-03-03/2004-03-04/2004-03-05/2004-03-06/2004-03-07/2004-03-08/2004-03-09/2004-03-10/2004-03-11/2004-03-12/2004-03-13/2004-03-14/2004-03-15/2004-03-16/2004-03-17/2004-03-18/2004-03-19/2004-03-20/2004-03-21/2004-03-22/2004-03-23/2004-03-24/2004-03-25/2004-03-26/2004-03-27/2004-03-28/2004-03-29/2004-03-30/2004-03-31/2016-04-01/2016-04-02/2016-04-03/2016-04-04/2016-04-05/2016-04-06/2016-04-07/2016-04-08/2016-04-09/2016-04-10/2016-04-11/2016-04-12/2016-04-13/2016-04-14/2016-04-15/2016-04-16/2016-04-17/2016-04-18/2016-04-19/2016-04-20/2016-04-21/2016-04-22/2016-04-23/2016-04-24/2016-04-25/2016-04-26/2016-04-27/2016-04-28/2016-04-29/2016-04-30/2016-07-01/2016-07-02/2016-07-03/2016-07-04/2016-07-05/2016-07-06/2016-07-07/2016-07-08/2016-07-09/2016-07-10/2016-07-11/2016-07-12/2016-07-13/2016-07-14/2016-07-15/2016-07-16/2016-07-17/2016-07-18/2016-07-19/2016-07-20/2016-07-21/2016-07-22/2016-07-23/2016-07-24/2016-07-25/2016-07-26/2016-07-27/2016-07-28/2016-07-29/2016-07-30/2016-07-31/2016-11-01/2016-11-02/2016-11-03/2016-11-04/2016-11-05/2016-11-06/2016-11-07/2016-11-08/2016-11-09/2016-11-10/2016-11-11/2016-11-12/2016-11-13/2016-11-14/2016-11-15/2016-11-16/2016-11-17/2016-11-18/2016-11-19/2016-11-20/2016-11-21/2016-11-22/2016-11-23/2016-11-24/2016-11-25/2016-11-26/2016-11-27/2016-11-28/2016-11-29/2016-11-30/2016-12-01/2016-12-02/2016-12-03/2016-12-04/2016-12-05/2016-12-06/2016-12-07/2016-12-08/2016-12-09/2016-12-10/2016-12-11/2016-12-12/2016-12-13/2016-12-14/2016-12-15/2016-12-16/2016-12-17/2016-12-18/2016-12-19/2016-12-20/2016-12-21/2016-12-22/2016-12-23/2016-12-24/2016-12-25/2016-12-26/2016-12-27/2016-12-28/2016-12-29/2016-12-30/2016-12-31",
    "expver": "1",
    "grid": "0.75/0.75",
    "levtype": "sfc",
    "param": "136.128/141.128/164.128/167.128/168.128/186.128/238.128",
    "step": "0",
    "stream": "oper",
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    "type": "an",
    "target": "complicatedData.grib",
})