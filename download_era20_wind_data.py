#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "e2",
    "dataset": "era20c",
    "date": "1986-01-02/to/1986-03-01",
    "domain": "g",
    "expver": "1",
    "param": "229.140/230.140/232.140/245.140/249.140",
    "area": '20.0/140.0/-40.0/240.0',
    "stream": "wave",
    "time": "00:00:00/03:00:00/06:00:00/09:00:00/12:00:00/15:00:00/18:00:00/21:00:00",
    "type": "an",
    "format": "netcdf",
    "target": "1986_era20_jan_mar.nc",
})