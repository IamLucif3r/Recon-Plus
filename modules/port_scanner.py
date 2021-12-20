import socket
import subprocess
import sys
from datetime import datetime
from pyfiglet import Figlet
def render(text,style):
    f = Figlet(font=style)
    print("\033[H\033[J") 
    print(f.renderText(text))
    print("\t\t Created By: Anmol | Vaibhav | Aarushi | Harshit \n \n")
# Clear the screen
subprocess.call('clear', shell=True)

render('R+ Port Scanner','smslant')
# Ask for input
remoteServer = input("[*] Enter a remote host to scan: \t")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

t1 = datetime.now()
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print('Scanning Completed in: ', total)
