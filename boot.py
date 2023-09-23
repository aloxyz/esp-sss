# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network, socket, time, os

def connect(ssid, password):
    print('Connecting to', ssid, '... ', end='')

    wlan_if = network.WLAN(network.STA_IF)

    wlan_if.active(True)
    wlan_if.connect(ssid, password)

    while not wlan_if.isconnected():
        pass

    print('done. Network config:', wlan_if.ifconfig())

    return wlan_if
    
def createAP(ssid, password):
    ap_if = network.WLAN(network.AP_IF)
    
    ap_if.config(ssid='ESP-AP')
    ap_if.config(max_clients=10)
    ap_if.active(True)

    return ap_if

print('Booted!')

# CONNECT TO NETWORK
time.sleep(2)
wlan_if = connect('The Wired', 'Sissi2000!')



