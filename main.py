from colorama import Fore
import requests

a = r""" __      __      ___.   .__                   __    
/  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __
\   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ /
 \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    < 
  \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \
       \/       \/    \/     \/                   \/"""

print(Fore.RED + a + Fore.RESET)
print("by: " + Fore.GREEN + "@" + Fore.RESET + "InvisibleCat#0001")

webhook_url = input("Webhook URL: ")
if not webhook_url.__contains__("https://discord.com/api/webhooks/"):
    print(Fore.RED + "Invalid URL!" + Fore.RESET)
    exit()
print("Type the message to spam (type 'done' to to save the message):")
message = ""
while True:
    line = input("> ")
    if line == "done":
        break
    else:
        message += line + "\n"

count = int(input("How many times to spam? "))
for i in range(count):
    # jsonData = requests.post(webhook_url, json={"content": message}).json()
    response = requests.post(webhook_url, data={"content": message})

    if response.status_code == 204:
        print(Fore.GREEN + "Message sent! #" + str(i+1) + Fore.RESET)
    elif response.status_code == 400:
        print(Fore.RED + "Invalid Webhook URL!" + Fore.RESET)
        exit()
    else:
        print(Fore.RED + "Error! #" + str(i+1) + Fore.RESET + ": " + str(response.status_code))
        exit()
print(Fore.GREEN + "Done!" + Fore.RESET)




