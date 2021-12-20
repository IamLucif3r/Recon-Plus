#Created by IamLucif3r
from subprocess import call
from pyfiglet import Figlet
def render(text,style):
    print("\033[H\033[J") 
    f = Figlet(font=style)
    print(f.renderText(text))
    print("\t Created By: Anmol | Vaibhav | Aarushi | Harshit \n \n")

class reconPlus(object):

    def __init__(self,path='/home/iamlucif3r/Documents/Recon-Plus-final/test.py') :
        self.path=path

    def port_scanner(self):
        path = 'modules/port_scanner.py'
        call(["python3","{}".format(path)])
    
    def cms_scanner(self):
        path = 'modules/cms_scanner.py'
        call(["python3","{}".format(path)])
    
    def subdomain(self):
        path = 'modules/subdomain.py'
        call(["python3","{}".format(path)])
    
    def honeypot_detect(self):
        path = 'modules/honeypot_detect.py'
        call(["python3","{}".format(path)])
   
    def ip_lookup(self):
        path = 'modules/ip_lookup.py'
        call(["python3","{}".format(path)])
   
    def ns_lookup(self):
        path = 'modules/ns_lookup.py'
        call(["python3","{}".format(path)])
   
    def web_recon(self):
        path = 'modules/web_recon.py'
        call(["python3","{}".format(path)])


if __name__ == "__main__":
    c=reconPlus()
    while True:
        render('Recon-Plus','slant')
        print("1.Port Scanner")
        print("2.Web-Assets")
        print("3.Honeypot Detection")
        print("4.IP Lookup")
        print("5.Name Server Lookup")
        print("6.Web - Recon")
        print("7.CMS Scanner")
        print("8.Exit!")
        n = int(input("Select Your Option [1-5]: "))
        if n==1:
            c.port_scanner()
        elif n==2:
            c.subdomain()
        elif n==3:
            c.honeypot_detect()
        elif n==4:
            c.ip_lookup()
        elif n==5:
            c.ns_lookup()
        elif n==6:
            c.web_recon()
        elif n==7:
            c.cms_scanner()
        elif n==8:
            print("\n Byee ... \n")
            exit();
        else:
            print("\nInvalid Choice ..... Try again")
        ans = input("\n\n Enter 0 to continue ... \t")
        if ans == 0:
            break;

    #c.test_file()