# dynv6_update_script
A small python script to automaticly updates the ip adress of the dynv6 service to the IP of the device where the script is executed.

It is used with the following command:

```sh
   python3 dynv6_update.py --frequency 30 --token TOKEN --hostname HOSTNAME.dynv6.net
```

Using those settings, the script checks every 30 seconds if the ip has changed. Replace TOKEN with the API-Token of your dynv6 zone and change HOSTNAME.dynv6.net to the hostname of the respective zone.
