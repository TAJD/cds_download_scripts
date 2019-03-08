""" Download weather data

Download ERA5 weather data using the CDS API.

Thomas Dickson
thomas.dickson@soton.ac.uk
"""

import cdsapi
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def download_data(year, month):
    """Donwload a months worth of data."""
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'variable':[
                '10m_u_component_of_wind','10m_v_component_of_wind','mean_wave_direction',
                'mean_wave_period','significant_height_of_combined_wind_waves_and_swell'
            ],
            'product_type':'ensemble_members',
            'year':str(year),
            'month':[
                str(month).zfill(2) 
            ],

            'day':[
                '01','02','03',
                '04','05','06',
                '07','08','09',
                '10','11','12',
                '13','14','15',
                '16','17','18',
                '19','20','21',
                '22','23','24',
                '25','26','27',
                '28','29','30',
                '31'
            ],
            'time':[
                '00:00','01:00','02:00',
                '03:00','04:00','05:00',
                '06:00','07:00','08:00',
                '09:00','10:00','11:00',
                '12:00','13:00','14:00',
                '15:00','16:00','17:00',
                '18:00','19:00','20:00',
                '21:00','22:00','23:00'
            ],
            'area'    : '21.0/138.0/-40.5/240.0',
            'format':'netcdf'
        },
        "polynesia_"+str(year)+"_"+str(month).zfill(2)+'.nc')
    

def test_single_month():
    print("Test single month download function")
    download_data(1982, 1)


def test_multiple_months():
    print("Test multiple months")
    year = 1983
    for i in range(1, 13):
        download_data(year, i)
    
def download_multiple_months(year, start_m, end_m):
    print("Downloading {} {} - {}".format(year, start_m, end_m))
    for i in range(start_m, end_m+1):
        print("Downloading {} {}".format(year, i))
        download_data(year, i)
        print("Finished downloading {} {}".format(year, i))

if __name__ == "__main__":
    download_multiple_months(2005, 1, 12)