#!/usr/bin/python3
import os
from pyfiglet import Figlet
def render(text,style):
    print("\033[H\033[J") 
    f = Figlet(font=style)
    print(f.renderText(text))
    
render('Installing R+ ..','smslant')

os.system('pip install -r requirements.txt')