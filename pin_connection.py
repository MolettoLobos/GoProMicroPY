import urequests as requests
import network

pinvalue = 'XXXX' #4 number PIN  ID
ssid = 'YOUR_SSID'
password =  'YOUR_PASSWORD'
model = 'HERO4'
#connect to wifi
routercon = network.WLAN(network.STA_IF)
routercon.active()
routercon.active(True)
routercon.connect(ssid, password)

if model == 'HERO4':
    r = requests.get('https://10.5.5.9/gpPair?c=start&pin='+pinvalue+'&mode=0')
    r = requests.get('https://10.5.5.9/gpPair?c=finish&pin='+pinvalue+'&mode=0')    
else:
    print('The model '+model+'is not available, feel free to push the update')
    
