import argparse
import json
import requests
import time

parser = argparse.ArgumentParser(description='A script to update dynv6')
parser.add_argument('--token', dest='token', type=str, help="Token displayed as username in dynv6")
parser.add_argument('--frequency', dest='frequency', type=int, help="How often the script checks whether the ip has changed in seconds")
parser.add_argument('--hostname', dest='hostname', type=str, help="The domain/hostname")

args = parser.parse_args()

last_ipv4 = ""
last_ipv6 = ""

try:
    while True:
        r = requests.get('https://api.ipify.org/?format=json')
        rv6 = requests.get('http://api6.ipify.org/?format=json')

        if r.status_code == 200 and rv6.status_code == 200:

            ipv4 = r.json()["ip"]
            ipv6 = rv6.json()["ip"]
            if last_ipv4 != ipv4 or last_ipv6 != ipv6:
                last_ipv4 = ipv4
                last_ipv6 = ipv6

                update_url_ipv4 = "https://dynv6.com/api/update?hostname=" + args.hostname + "&token=" + args.token + "&ipv4=" + ipv4
                update_url_ipv6 = "https://dynv6.com/api/update?hostname=" + args.hostname + "&token=" + args.token + "&ipv6prefix=" + ipv6
                print(update_url_ipv6)
                print(update_url_ipv4)
                success_ipv4 = requests.get(update_url_ipv4)
                success_ipv6 = requests.get(update_url_ipv6)
                if success_ipv4.status_code != 200 or success_ipv6.status_code != 200:
                    print("Update was not successful")
                else:
                    print("Successfuly updated ip to " + ipv6)
        time.sleep(args.frequency * 60)
except KeyboardInterrupt:
    print("Shutting down update service")
    exit(0)