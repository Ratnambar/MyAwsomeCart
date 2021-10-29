import requests
import urllib.parse



hostname="" #the hostname for which want to get the balance details
username=""
password=""
port=""  #this include port number 


payload = '' #it includes the SSD code of respective carieer
res = urllib.parse.quote(payload)

url = "http://{hostname}/cgi/WebCGI?1500102=account={username}&password={password}&port={port}&content={ussd}".format(hostname=hostname,username=username,password=password,port=port,ussd=res)

r = requests.get(url)

res = r.text
print(res)


