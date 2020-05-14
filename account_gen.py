#cdg-acc-gen.py
import random, requests, time
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"1","2","3","4","5","6","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
firstnames=['Annabelle', 'Jason', 'Michael', 'Austin', 'Alva', 'Acacius', 'Tate', 'Diego', 'Easton', 'Lucius', 'Cash', 'Ash', 'Luca', 'Adah', 'Reese', 'Mika', 'Paisley', 'Amina', 'Teagan', 'Nova', 'Aura', 'Pearl', 'Billie', 'Oliver', 'George', 'Harry', 'Noah', 'Jack', 'Charlie', 'Leo', 'Jacob', 'Freddie', 'Alfie', 'Archie', 'Theo', 'Oscar', 'Arthur', 'Thomas', 'Logan', 'Henry', 'Joshua', 'James', 'William', 'Max', 'Isaac', 'Lucas', 'Ethan', 'Teddy', 'Finley', 'Mason', 'Harrison', 'Hunter', 'Alexander', 'Daniel', 'Joseph', 'Tommy', 'Arlo', 'Reggie', 'Edward', 'Jaxon', 'Adam', 'Sebastian', 'Rory', 'Riley', 'Dylan', 'Elijah', 'Carter', 'Albie', 'Louie', 'Toby', 'Benjamin', 'Reuben', 'Jude', 'Samuel', 'Harley', 'Luca', 'Frankie', 'Ronnie', 'Jenson', 'Hugo', 'Jake', 'David', 'Theodore', 'Roman', 'Bobby', 'Alex', 'Caleb', 'Ezra', 'Ollie', 'Finn', 'Jackson', 'Zachary', 'Jayden', 'Harvey', 'Albert', 'Lewis', 'Blake', 'Stanley', 'Elliot', 'Grayson', 'Liam', 'Louis', 'Matthew', 'Elliott', 'Tyler', 'Luke', 'Michael', 'Gabriel', 'Ryan', 'Dexter', 'Kai', 'Jesse', 'Leon', 'Nathan', 'Ellis', 'Connor', 'Jamie', 'Rowan', 'Sonny', 'Dominic', 'Eli', 'Aaron', 'Jasper', 'Olivia', 'Amelia', 'Isla', 'Ava', 'Emily', 'Sophia', 'Grace', 'Mia', 'Poppy', 'Ella', 'Lily', 'Evie', 'Isabella', 'Sophie', 'Ivy', 'Freya', 'Harper', 'Willow', 'Charlotte', 'Jessica', 'Rosie', 'Daisy', 'Alice', 'Elsie', 'Sienna', 'Florence', 'Evelyn', 'Phoebe', 'Aria', 'Ruby', 'Isabelle', 'Esme', 'Scarlett', 'Matilda', 'Sofia', 'Millie', 'Eva', 'Layla', 'Chloe', 'Luna', 'Maisie', 'Lucy', 'Erin', 'Eliza', 'Ellie', 'Mila', 'Imogen', 'Bella', 'Lola', 'Molly', 'Maya', 'Violet', 'Lilly', 'Holly', 'Thea', 'Emilia', 'Hannah', 'Penelope', 'Harriet', 'Georgia', 'Emma', 'Lottie', 'Nancy', 'Rose', 'Amber', 'Elizabeth', 'Gracie', 'Zara', 'Darcie', 'Summer', 'Hallie', 'Aurora', 'Ada', 'Anna', 'Orla', 'Robyn', 'Bonnie', 'Abigail', 'Darcy', 'Eleanor', 'Arabella', 'Lexi', 'Clara', 'Heidi', 'Lyla', 'Annabelle', 'Jasmine', 'Nevaeh', 'Victoria', 'Amelie', 'Myla', 'Maria', 'Julia', 'Niamh', 'Mya', 'Annie', 
'Darcey', 'Zoe', 'Felicity', 'Iris']
lastnames=['Stockley', 'Smith', 'Trinder', 'Skipworth', 'Percival', 'Wordley', 'Hobbs', 'Lewington', 'Illiffe', 'Jones', 'Brown', 'Taylor', 'Wilson', 'Davies', 'Evans', 'Johnson', 'Thomas', 'Roberts', 'Walker', 'Wright', 'Thompson', 'Robinson', 'White', 'Hall', 'Hughes', 'Green', 'Edwards', 'Martin', 'Wood', 'Clarke', 'Harris', 'Jackson', 'Lewis', 'Clark', 'Turner','Smith']
anticaptcha_key=input("Anticaptcha key: ")
amount=int(input("Amount: "))
catchall=input("Catchall eg@akchefs.com: ")
while True:
    domain=input("Shopify site eg \"https://uk.cdgcdgcdg.com\": " )
    if domain.count("/")==2:
        break
    else:
        print("Incorrect url, must be exactly as shown.")


headers={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-length": "525",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://uk.cdgcdgcdg.com",
    "pragma": "no-cache",
    "referer": "https://uk.cdgcdgcdg.com",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

def find_code(text, target, length):
    resplist=str(text).split(target)
    return(resplist[1][0:length])

print("Creating accounts for "+domain+" if the site requires captcha this could take a while.")

for i in range(amount):
    sesh=requests.session()
    email=""
    passw=""
    for i in range(10):
        email+=random.choice(characters)
    email+=catchall
    for i in range(10):
        passw+=random.choice(characters)
    try:
        sesh.get(domain+"/account/register")
    except:
        print("Invalid url, please try again.")
        time.sleep(20)
        quit()
    data={
        "form_type": "create_customer",
        "utf8": "✓",
        "customer[last_name]": random.choice(lastnames),
        "customer[first_name]": random.choice(firstnames),
        "customer[email]": email,
        "customer[password]":passw,
        "terms_and_conditions": "1"
    }
    resp=sesh.post(domain+"/account",data=data,headers=headers)
    if str(resp.history).startswith("[<Response [302]>]"):
        if resp.url.startswith(domain+"/challenge"):
            try:
                auth_token=find_code(resp.text,"authenticity_token\" value=\"",86)
                captcha_token=find_code(resp.text,"sitekey: \"",40)
                client = AnticaptchaClient(anticaptcha_key)
                task = NoCaptchaTaskProxylessTask(domain+"/challenge", captcha_token)
                job = client.createTask(task)
                job.join()
                captcha_response=job.get_solution_response()
                data={
                    "authenticity_token": auth_token,
                    "g-recaptcha-response":captcha_response
                }
            except:
                print("Error contacting anti-captcha")
            res=sesh.post(domain+"/account",headers=headers,data=data)
            if str(res.status_code)=="200":
                print(email+":"+passw)
            else:
                print("Error submitting captcha")
        else:
            print(email+":"+passw)
    else:
        print("Error creating account")

    
    
