#!/bin/python
import requests 
import sys
from pyfiglet import Figlet

def render(text,style):
    print("\033[H\033[J") 
    f = Figlet(font=style)
    print(f.renderText(text))
    print("\t\t Created By: Anmol | Vaibhav | Aarushi | Harshit \n \n")


render('R+ CMS Detect','smslant')    

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED='\033[31m'

def main():
    target = input("Enter Target Domain: ")
    try:
        if target != "" :
            print (" {}{}Target -{} {}".format(bcolors.BOLD,bcolors.RED,bcolors.ENDC,target))
            url_data = "https://whatcms.org/APIEndpoint/Detect?key=746f350b4b16644cd12fdb77a8ea14155c083cd3269036b30126e423ba0d7d61ffdd4f&url={}".format(target)
            object_json = requests.get(url_data)
            temp_storage = object_json.json()
            data_storage = temp_storage['result']
           
            if data_storage['code'] == 200:
                print (" {}CMS NAME :{} {}{}{} ~ {}VERSION :{} {}{}{}".format(bcolors.BOLD,bcolors.ENDC,bcolors.OKGREEN,data_storage['name'],bcolors.ENDC,bcolors.BOLD,bcolors.ENDC,bcolors.OKGREEN,data_storage['version'],bcolors.ENDC))
            else:
                print ("{}{}{}".format(bcolors.BOLD.bcolors.RED,data_storage['msg']))
        else:
            print ("{}Url Not Found !{}".format(bcolors.WARNING,bcolors.ENDC))
    except:
        print ("{} Error Found ! Check the Url {}".format(bcolors.WARNING,bcolors.ENDC))

if __name__ == '__main__':
    main()
    

 