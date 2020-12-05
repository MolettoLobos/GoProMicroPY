#main.py

import urequests as requests
import network
import time
from machine import Pin, time_pulse_us
ssid = 'goprohero4'
password =  'goprohero4'
model = 'HERO4'
print('main start up, please wait 5 seconds...')
time.sleep(5) #10 secs before connection
def shutter_camera(pin):
    print('taking picture')
    requests.get('http://10.5.5.9/gp/gpControl/command/shutter?p=1')
    return

    
#connect to wifi
routercon = network.WLAN(network.STA_IF)
routercon.active()
routercon.active(True)
routercon.connect(ssid, password)

#SIGNAL FROM RC SHUTTER PIXHAWK
btn = Pin(4, Pin.IN) #GPIO4 (D2) as Input GPIO
trim_threshold = 1500
while 1 < 2: #eternal loop
    #print('btn value')
    #print(btn.value())
    print('time pulse value / trim values')
    print(time_pulse_us(btn,1))
    #1000 value is camera untriggered and 1800 is trigger camera
    if time_pulse_us(btn,1) > trim_threshold:
        #pix.irq(shutter_camera,Pin.IRQ_RISING)
        print('cheese!!')
        try:
            requests.get('http://10.5.5.9/gp/gpControl/command/shutter?p=1')
            print(btn.read())
            time.sleep(2)
        except OSError:
            print('query failed, sleeping 2 seconds...')
            time.sleep(2)
        print('request sent to GoPro API')
    else:
        print('waiting')
        time.sleep(0.25)
#locate = requests.get('http://10.5.5.9/gp/gpControl/command/system/locate?p=1')
#locate = requests.get('http://10.5.5.9/gp/gpControl/command/system/locate?p=1')
#defaultcameramode = requests.get('http://10.5.5.9/gp/gpControl/setting/53/1')
#defaultvideomode = requests.get('http://10.5.5.9/gp/gpControl/setting/53/1')