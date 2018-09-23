import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+sys.argv[1]+'&VehicleMonitoringDetailLevel=calls&LineRef='+sys.argv[2] 

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

variable1 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
variable1

index = 0
for i in variable1:
    i =i['MonitoredVehicleJourney']
    index+=1
    print ('Bus',index,'is at latitude:', i['VehicleLocation']['Latitude'],'Longitude',i['VehicleLocation']['Longitude'])
