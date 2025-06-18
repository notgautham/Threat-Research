import requests
import os
import subprocess

db_file = "blacklist_ips.tch"
source_url = "https://raw.githubusercontent.com/romainmarcoux/malicious-outgoing-ip/main/full-outgoing-ip-aa.txt"
source_meta = {
    "source": "GitHub",
    "repo": "https://github.com/romainmarcoux/malicious-outgoing-ip",
    "category": "outgoing malicious IPs",
    "format": "plain text"
}

print("[*] Fetching IP list from GitHub...")
response = requests.get(source_url)

if response.status_code != 200:
    print("[-] Failed to fetch data.")
    exit(1)

ip_list = response.text.strip().split("\n")
print(f"[+] Retrieved {len(ip_list)} IPs")

if not os.path.exists(db_file):
    print("[*] Creating new Tokyo Cabinet database...")
    subprocess.run(["tchmgr", "create", db_file])

for ip in ip_list:
    value = f"source={source_meta['source']};repo={source_meta['repo']};category={source_meta['category']}"
    subprocess.run(["tchmgr", "put", db_file, ip.strip(), value], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"[✓] Inserted {len(ip_list)} IPs into {db_file}")
