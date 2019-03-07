"""Combine data into a single large nc file.

Thomas Dickson
thomas.dickson@soton.ac.uk
"""
import xarray as xr
import glob, os


def get_weather_files(dir_path):
    return glob.glob(dir_path+"/*.nc")


def concatenate_weather_files(dir_path):
    """Concatenate all .nc files found in the directory set by path."""
    # import all the files as datasets
    fnames = get_weather_files(dir_path)
    ds_list = []
    for f in fnames:
        with xr.open_dataset(f, engine='netcdf4') as ds:
            ds_list.append(ds)
    ds_main = xr.concat(ds_list, dim='time')
    groups = ds_main.groupby('time')
    return groups


def generate_year_weather_data(directory, new_fname):
    """Generate yearly weather data."""
    ds_whole = concatenate_weather_files(directory)
    print(ds_whole.last())
    ds_whole.last().to_netcdf(directory+new_fname+".nc")


def generate_polynesian_weather_data():
    """Generate the 14 month long weather scenarios required for the Polynesian voyaging case study."""
    weather_path = os.path.dirname(os.path.realpath(__file__))
    low_fp = weather_path + "/polynesia_weather/low/1976/"
    med_fp = weather_path + "/polynesia_weather/med/1985/"
    high_fp = weather_path + "/polynesia_weather/high/1982/"
    low_name = "polynesia_1976"
    med_name = "polynesia_1985"
    high_name = "polynesia_1982"
    generate_year_weather_data(low_fp, low_name)
    generate_year_weather_data(med_fp, med_name)
    generate_year_weather_data(high_fp, high_name)


def inspect_data():
    # fname = "polynesia_weather/high/1982/1982_era20_april_june.nc"
    fname = "cds_scripts/download_2018_year_geographic_sub.nc"
    # fname = "cds_scripts/download_2018_year_geographic_subset.nc"
    with xr.open_dataset(fname) as ds:
        print(ds.keys())

if __name__ == "__main__":
    # generate_polynesian_weather_data()
    inspect_data()