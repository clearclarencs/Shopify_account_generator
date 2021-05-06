#cdg-acc-gen.py
import random, requests, time, threading
from capmonster_python import NoCaptchaTask
characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"1","2","3","4","5","6","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
capmonsterkey=input("Capmonster key (None if not required): ")
delay = int(input("Delay in seconds: "))
def find_code(text, target, length):
    resplist=str(text).split(target)
    return(resplist[1][0:length])
    
def proxy_format(proxy):
    try:
        if proxy[len(proxy)-1]=="\n":
            proxy= proxy[0:len(proxy)-1]
        try:
            proxylist=proxy.split(":")
            if len(proxylist)==2:
                proxy=proxy
            elif len(proxylist)==4:
                proxy=str(proxylist[2])+":"+str(proxylist[3])+"@"+str(proxylist[0])+":"+str(proxylist[1])
            else:
                return False
            return{
                    "http":"http://"+proxy,
                    "https":"https://"+proxy,
                    "ftp":"ftp://"+proxy
                }
        except:
            return False
    except:
        return False
while True:
    try:
        domain=input("Shopify site eg \"https://uk.cdgcdgcdg.com\": " )
        proxy_bool=input("Use proxies.txt? (y/n): ")
        if proxy_bool=="y":
            proxy_bool=True
            worked=True
        elif proxy_bool=="n":
            proxy_bool=False
            worked=True
        else:
            proxy_bool=False
            worked=False
        if proxy_bool:
            try:
                with open("proxies.txt","r") as r:
                    proxies=r.read().splitlines()
            except:
                print("Unable to open proxies.txt, ensure file is in same directory")
                worked=False
        if domain.count("/")==2 and worked==True:
            break
        else:
            print("Incorrect info, must be exactly as shown.")
    except:
        print("Error try again, ensure amount is a number.")


headers={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-length": "525",
    "content-type": "application/x-www-form-urlencoded",
    "origin": domain,
    "pragma": "no-cache",
    "referer": domain,
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

print("Creating accounts for "+domain+" if the site requires captcha this could take a while.")

def setup(proxy, data):
    sesh=requests.session()
    if proxy != "False":
        proxydict=proxy_format(proxy)
        if proxydict == False:
            print("Invalid proxy: "+str(proxy))
            return
    else:
        proxydict=False
    try:
        sesh.get(domain+"/account/register")
    except:
        print("Invalid url, please try again.")
        time.sleep(20)
        quit()
    data={
        "form_type": "create_customer",
        "utf8": "✓",
        "customer[last_name]": task.split(",")[3],
        "customer[first_name]": task.split(",")[2],
        "customer[email]": task.split(",")[0],
        "customer[password]":task.split(",")[1],
        "terms_and_conditions": "1"
    }
    resp=sesh.post(domain+"/account",data=data,headers=headers, proxies=proxydict)
    if str(resp.history).startswith("[<Response [302]>]"):
        if resp.url.startswith(domain+"/challenge"):
            try:
                capmonster = NoCaptchaTask(client_key=capmonsterkey)
                taskId = capmonster.createTask(website_key=sitecapkey, website_url=prodlink)
                response = capmonster.joinTaskResult(taskId=taskId, maximum_time=300)
            except:
                print("Error getting captcha")
            res=sesh.post(domain+"/account",headers=headers,data=data, proxies=proxydict)
            if str(res.status_code)=="200":
                print(task.split(",")[0]+":"+task.split(",")[1])
            else:
                print("Error submitting captcha")
        else:
            try:
                with open("accounts.txt", "a+") as r:
                    r.write(task.split(",")[0]+":"+task.split(",")[1]+"\n")
            except:
                print(task.split(",")[0]+":"+task.split(",")[1])
    else:
        print("Error creating account")
    #except:
     #   print("Error occured")

try:
    with open("accounts.txt", "a+") as r:
        r.write(domain+":\n")
except:
    None  
with open("tasks.csv", "r") as r:
    tasks=r.read().splitlines()
    tasks.pop(0)
for task in tasks:
    if proxy_bool:
        try:
            proxy=random.choice(proxies)
        except:
            print("Proxy error, ensure you have proxies in proxies.txt")
            break
    if proxy_bool:
        x = threading.Thread(target=setup, args=(proxy, task))
    else:
        x = threading.Thread(target=setup, args=("False", task))
    x.start()
    time.sleep(delay)
while True:
    input("Finished")
