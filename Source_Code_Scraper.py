import requests
import time
from time import sleep

url = input("Enter Website To Scrape Source Code Of (Please Note: It Can Only Scrape Code Of The Page You Have Given):")

r = requests.get(url)

f = open('Source_Code.txt', 'w')

f.write(r.text)

print("Done Scraping Source Code!")
sleep(1)
print("Exiting Now...")
sleep(1)
exit()