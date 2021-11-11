from requests import get
import json

ipadd = input("Enter IP : ")
loc = get('https://ipapi.co/'+ipadd+'/json/')
obj = loc.json()
with open("IPinfo.txt", "w") as write_file:
    json.dump(obj, write_file,indent=4)

file1 = open("IPinfo.txt","r+")
print("\n\n")
print(file1.read())
file1.close()
print("\n\nIP information is stored in a file named IPinfo.txt\n\n")