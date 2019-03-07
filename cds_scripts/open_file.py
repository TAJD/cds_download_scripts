#!/usr/bin/env python
import xarray as xr


if __name__=="__main__":
    fname = "test.nc"
    with xr.open_dataset(fname) as ds:
        print(ds.keys())
