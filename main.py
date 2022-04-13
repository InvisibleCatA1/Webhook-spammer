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
    requests.post(webhook_url, json={"content": message})
    print(Fore.GREEN + "Message sent! #" + str(i+1) + Fore.RESET)
print(Fore.GREEN + "Done!" + Fore.RESET)




