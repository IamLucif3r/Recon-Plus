import os
from pyfiglet import Figlet
def render(text,style):
    print("\033[H\033[J") 
    f = Figlet(font=style)
    print(f.renderText(text))
    print("\t\t Created By: Anmol | Vaibhav | Aarushi | Harshit \n \n")

render('R+ Sub-Domains','slant')
domain = input("[*] Enter Target Domain: \t")
os.system("gau --subs {}".format(domain))