import pandas as pd
import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+sys.argv[1]+'&VehicleMonitoringDetailLevel=calls&LineRef='+sys.argv[2] 

df = pd.read_json(url)
df.to_csv("MTAbusline.csv")

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


variable1 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
df_all=pd.DataFrame(columns=['latitude', 'Longitude', 'Busstop', 'Stopstatus'])

index = 0

for i in variable1:

    bus =i['MonitoredVehicleJourney']
    if len(bus['OnwardCalls'])<1:
    	latitute = bus['VehicleLocation']['Latitude']
    	Longitude = bus['VehicleLocation']['Longitude']
    	Busstop = 'N/A'
    	Stopstatus = 'N/A'
    else:
    	latitude = bus['VehicleLocation']['Latitude']
    	Longitude = bus['VehicleLocation']['Longitude']
    	Busstop = bus['OnwardCalls']['OnwardCall'][0]['StopPointName']
    	Stopstatus = bus['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

    df_all.loc[index]= [latitude, Longitude, Busstop, Stopstatus]
    index += 1
    print(latitude, Longitude, Busstop, Stopstatus)

df_all
df_all.to_csv(sys.argv[3], index = False) 		

