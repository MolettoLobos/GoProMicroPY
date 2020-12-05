import urequests as requests
import network
import time
from machine import Pin
ssid = 'goprohero4'
password =  'goprohero4'
model = 'HERO4'
time.sleep(10000) #10 secs before connection
#connect to wifi
routercon = network.WLAN(network.STA_IF)
routercon.active()
routercon.active(True)
routercon.connect(ssid, password)

#SIGNAL FROM RC SHUTTER PIXHAWK
btn = Pin(4, Pin.IN) #GPIO4 (D2) as Input GPIO
pin = Pin(2, Pin.OUT)
pin.on()
while 1 < 2: #eternal loop
    if btn.value() == 1:
        print('cheese!!')
        requests.get('http://10.5.5.9/gp/gpControl/command/shutter?p=1')
        pin.off()
    else:
        print('waiting')
        pin.on()
        #time.sleep(200)
#locate = requests.get('http://10.5.5.9/gp/gpControl/command/system/locate?p=1')
#locate = requests.get('http://10.5.5.9/gp/gpControl/command/system/locate?p=1')
#defaultcameramode = requests.get('http://10.5.5.9/gp/gpControl/setting/53/1')
#defaultvideomode = requests.get('http://10.5.5.9/gp/gpControl/setting/53/1')
