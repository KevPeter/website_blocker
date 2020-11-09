import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
websites = ['www.instagram.com', 'instagram.com', 'www.facebook.com', 'facebook.com']

while True:
    isBlockTime = dt(dt.now().year, dt.now().month, dt.now().day, 7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18)
    if isBlockTime:
        print("blocking")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        file.close()
    else:
        print("not blocking")
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        file.close()
    time.sleep(5)
