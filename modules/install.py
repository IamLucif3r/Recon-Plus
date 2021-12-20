import os
from pyfiglet import Figlet
def render(text,style):
    f = Figlet(font=style)
    print(f.renderText(text))
    print("\t\t Created By: Anmol | Vaibhav | Aarushi | Harshit \n \n")

render('Recon+ Installing  ','smslant')
os.system("pip install -r requirements.txt")