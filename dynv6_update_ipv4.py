import argparse
import json
import requests
import time

parser = argparse.ArgumentParser(description='A script to update dynv6')
parser.add_argument('--token', dest='token', type=str, help="Token displayed as username in dynv6")
parser.add_argument('--frequency', dest='frequency', type=int, help="How often the script checks whether the ip has changed in seconds")
parser.add_argument('--hostname', dest='hostname', type=str, help="The domain/hostname")

args = parser.parse_args()

last_ip = ""

try:
    while True:
        r = requests.get('https://api.ipify.org/?format=json')
        if r.status_code == 200:
            ip = r.json()["ip"]
            if last_ip != ip:
                last_ip = ip
                update_url = "https://dynv6.com/api/update?hostname=" + args.hostname + "&token=" + args.token + "&ipv4=" + ip
                success = requests.get(update_url)
                if success.status_code != 200:
                    print("Update was not successful")
                else:
                    print("Successfuly updated ip to " + ip)
        time.sleep(args.frequency * 60)
except KeyboardInterrupt:
    print("Shutting down update service")
    exit(0)