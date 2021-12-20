import sys
from requests import get
from pyfiglet import Figlet
def render(text,style):
    print("\033[H\033[J") 
    f = Figlet(font=style)
    print(f.renderText(text))
    print("\t\t Created By: Anmol | Vaibhav | Aarushi | Harshit \n \n")

render('R+ Honeypot Detect','smslant')    
inp = input("Enter Target to Check for Honeypot:\t")

def honeypot(inp):
    honey = 'https://api.shodan.io/labs/honeyscore/%s?key=5448RQUXTLZVjInEHEn2r3JaC2prWbbd' % inp
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write('%s No information available' % bad + '\n')
    if result:
        
        probability = str(float(result) * 10)
        sys.stdout.write('%s Honeypot Probabilty: %s%s%%%s' %
                         (info, color, probability, end) + '\n')