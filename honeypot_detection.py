import sys
from requests import get
from core.colors import bad, info, red, green, end

inp = input('Enter Target IP Address: \t')

def honeypot(inp):
    honey = 'https://api.shodan.io/labs/honeyscore/%s?key=2jI9a07EwbZdWcwYmtpeZZMb8WQcYiue' % inp
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write('%s No information available' % bad + '\n')
    if result:
        if float(result) < 0.5:
            color = green
        else:
            color = red
        probability = str(float(result) * 10)
        sys.stdout.write('%s Honeypot Probabilty: %s%s%%%s' %
                         (info, color, probability, end) + '\n')

honeypot(inp)