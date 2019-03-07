#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
                "class": "ea",
                "dataset": "era5",
                "date": "2000-01-01/to/2000-02-31",
                "domain": "g",
                "expver": "1",
                'area': '20.0/140.0/-40.0/240.0',
                "param": "237.140/238.140/239.140/245.140/249.140",
                "step": "0",
                "grid": "0.25/0.25",
                "stream": "ewda",
                "time": "00:00:00/03:00:00/06:00:00/09:00:00/12:00:00/15:00:00/18:00:00/21:00:00",
                "type": "em",
                "format": "netcdf",
                "target": "2000_poly_jan_feb.nc",
                })
