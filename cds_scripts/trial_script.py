#!/usr/bin/env python
import cdsapi
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
c = cdsapi.Client()
c.retrieve('reanalysis-era5-pressure-levels', {
        'variable'      : 'temperature',
        'pressure_level': '1000',
        'product_type'  : 'reanalysis',
        'year'          : '2008',
        'month'         : '01',
        'day'           : '01',       
        'area'          : [60, -10, 50, 2], # North, West, South, East. Default: global
        'grid'          : [1.0, 1.0], # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: 0.25 x 0.25
        'time'          : '12:00',
        'format'        : 'netcdf' # Supported format: grib and netcdf. Default: grib
    }, 'test.nc')
