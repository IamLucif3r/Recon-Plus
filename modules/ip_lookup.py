import shodan
import requests
from pyfiglet import Figlet
def render(text,style):
    print("\033[H\033[J") 
    f = Figlet(font=style)
    print(f.renderText(text))
    print("\t\t Created By: Anmol | Vaibhav | Aarushi | Harshit \n \n")

SHODAN_API_KEY = "5448RQUXTLZVjInEHEn2r3JaC2prWbbd" 
api = shodan.Shodan(SHODAN_API_KEY)
render('R+ IP Lookup','slant')
target = input("[*] Enter Target Domain / IP:\t")

dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + SHODAN_API_KEY

try:
    # First we need to resolve our targets domain to an IP
    resolved = requests.get(dnsResolve)
    hostIP = resolved.json()[target]

    # Then we need to do a Shodan search on that IP
    host = api.host(hostIP)
    print ("IP: %s" % host['ip_str'])
    print ("Organization: %s" % host.get('org', 'n/a'))
    print ("Operating System: %s" % host.get('os', 'n/a'))

    # Print all banners
    for item in host['data']:
        print ("Port: %s" % item['port'])
        print ("Banner: %s" % item['data'])

    # Print vuln information
    for item in host['vulns']:
        CVE = item.replace('!','')
        print ('Vulns: %s' % item)
        exploits = api.exploits.search(CVE)
        for item in exploits['matches']:
            if item.get('cve')[0] == CVE:
                print (item.get('description'))
except:
    'An error occured'