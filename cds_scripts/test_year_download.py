#!/usr/bin/env python
import calendar
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
 
def retrieve_era5():
    """      
       A function to demonstrate how to iterate efficiently over several years and months etc    
       for a particular era5 request.     
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'target' to organise the requested data in files as you wish.
       In the example below the data are organised in files per month. (eg "era5_daily_201510.grb")
    """
    yearStart = 2014
    yearEnd = 2015
    monthStart = 1
    monthEnd = 12
    for year in list(range(yearStart, yearEnd + 1)):
        for month in list(range(monthStart, monthEnd + 1)):
            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            target = "era5_daily_%04d%02d.grb" % (year, month)
            requestDates = (startDate + "/TO/" + lastDate)
            era5_request(requestDates, target)
 
def era5_request(requestDates, target):
    """      
        An ERA5 request for analysis pressure level data.
        Change the keywords below to adapt it to your needs.
        (eg to add or to remove  levels, parameters, times etc)
        Request cost per day is 112 fields, 14.2326 Mbytes
    """
    server.retrieve({
        "class": "ea",                                  # do not change
        "dataset": "era5",                              # do not change
        "expver": "1",                                  # do not change
        "stream": "oper",                               # do not change
        "type": "an",                                   # analysis (versus forecast, fc)
        "date": requestDates,                           # dates, set automatically from above
        "levtype": "sfc",                                # pressure level data (versus surface, sfc, and model level, ml)
        "levelist": "100/500/700/750/850/925/1000",     # levels, required only with levtype:pl and levtype:ml
        "param": "129.128/133.128/157.128/248.128",     # here: Geopotential (z), Specific humidity (q), Relative humidity (r), Fraction of cloud cover (cc); see http://apps.ecmwf.int/codes/grib/param-db
        "target": target,                               # output file name, set automatically from above
        "time": "00/06/12/18",                          # times of analysis (with type:an), or initialization time of forecast (with type:fc)
        "grid": "0.25/0.25",                            # Optional for GRIB, required for NetCDF. The horizontal resolution in decimal degrees. If not set, the archived grid as specified in the data documentation is used.
        "area": "75/-20/10/60",                         # Optional. Subset (clip) to an area. Specify as N/W/S/E in Geographic lat/long degrees. Southern latitudes and western longitudes must be
                                                        # given as negative numbers. Requires "grid" to be set to a regular grid, e.g. "0.25/0.25".
        "format": "netcdf",                             # Optional. Output in NetCDF format. Requires that you also specify 'grid'. If not set, data is delivered in GRIB format, as archived.
    })
if __name__ == '__main__':
    retrieve_era5()
