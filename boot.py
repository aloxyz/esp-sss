# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network, socket, time, os, sss
from umqtt.simple import MQTTClient

def wlan_connect(ssid, password):
    print('Connecting to', ssid, '... ', end='')

    wlan_if = network.WLAN(network.STA_IF)

    wlan_if.active(True)
    wlan_if.connect(ssid, password)

    while not wlan_if.isconnected():
        pass

    print('done. Network config:', wlan_if.ifconfig())

    return wlan_if
    
def create_AP(ssid, password):
    ap_if = network.WLAN(network.AP_IF)
    
    ap_if.config(ssid='ESP-AP')
    ap_if.config(max_clients=10)
    ap_if.active(True)

    return ap_if
    
def mqtt_connect(host, client_name):
    client = MQTTClient(client_name, host, keepalive=60)

    print('Connecting to mqtt broker', host, '... ', end='')
    client.connect()
    print('done. Client id:', client_name)

    return client

def publish_split_secret(client, secret):
    shares = sss.shamir_deconstruct(3, 6, 1234)
    print('shares of', secret, ':', shares)
    
    client.publish('sss', ";".join(map(str, shares)))

    return shares

print('Booted!')
# CONNECT TO NETWORK
time.sleep(2)
wlan_if = wlan_connect('The Wired', 'Sissi2000!')

# CONNECT TO MQTT SERVER
time.sleep(2)
client = mqtt_connect('192.168.1.60', 'esp32')

# SECRET SPLIT
publish_split_secret(client, 1234)