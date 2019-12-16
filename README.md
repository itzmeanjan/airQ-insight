# airQ-insight

![airQuality ( PM10 ) at Alipur, Delhi-DPCC, Delhi](airQualityAlipur,Delhi-DPCC,Delhi_PM10_.gif)

Visualization of Air Quality Indication Dataset collected by **airQ** to get deeper insight, written with :heart:

**Accompanying website for Visualization of Air Quality, Coming soon ...** :boss:

## motivation
Prior to it, I wrote one simple data collection module, which collects Air Quality Indication Data from Govt. Of India's [Open Data Platform](https://data.gov.in). 

Now for getting a peek into that collected dataset, I'm writing this module, which can generate animated plot of pollutants _( i.e. CO, NH3, NO2, OZONE, PM10, PM2.5, SO2 )_ for all monitoring stations, from which Pollution Control Board(s) collect data.

## installation
This python module is available on PyPI.
```bash
$ pip install airQInsight --user
$ python3 -m pip install airQInsight --user # if above one doesn't work
```

## usage
After installing **airQInsight**, make sure you've put installation path _( which is by default /home/user/.local/bin/ )_ in your system PATH variable.

Now it can be invoked using its name directly.
```bash
$ airQInsight
airQInsight - Air Quality Data Visualization System

	$ airQInsight `path-to-data-file_( *.json )_` `path-to-sink-directory`

Bad Input
```

## automation
It'd be a good idea to automate this animated plot generation method using _systemd_, as we did in case of **airQ** _( which collected Air Quality Indication Data periodically )_.

Required UNIT files are supplied [here](./systemd)

You'll require to make some changes in order to run this on your environment.

Thanking you :wink:
