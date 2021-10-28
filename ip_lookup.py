import os
import sys
import time
import subprocess
import json
import socket
from urllib.request import urlopen
from concurrent import futures

def lookup():
    os.system('')
    client = 1
    client = input(f'''
 [*] Enter IP Address: ''')
    url1 = "http://ip-api.com/json/"
    url2 = "http://extreme-ip-lookup.com/json/"
    trackedip1 = urlopen(url1 + client)
    trackedip2 = urlopen(url2 + client)
    data1 = trackedip1.read() 
    data2 = trackedip2.read()
    values1 = json.loads(data1)
    values2 = json.loads(data2)
    
    print(f''' 
 [>] IP: ''' + values1['query'])
    print(f" [>] City: " + values1['city'])
    print(f" [>] Country: " + values1['country'])
    print(f" [>] Name of the region: " + values1['regionName'])
    print(f" [>] Region: " + values1['region'])
    print(f" [>] ISP: " + values1['isp'])
    print(f" [>] ZIP Code: " + values1['zip'])
    print(f" [>] IP Type: " + values2['ipType'])
    print(f" [>] Organisation: " + values2['org'])
    print(f" [>] City: " + values2['city'])
    print(f" [>] Latitude: " + values2['lat'])
    print(f" [>] Longitude: " + values2['lon'])

def main():
    if len(sys.argv) < 2:
        os.system('')
        lookup()

main()
