# Threat Research: Blacklisted IP Sources

This document lists curated and regularly monitored sources for malicious or suspicious IP addresses. These sources can be integrated into firewalls, IDS/IPS systems, or threat intelligence pipelines.

---

## Existing Sources in `badfellas.xml`

### Regularly Updated
1. **Malware Domains (Lehigh University)**  
   URL: [http://malwaredomains.lehigh.edu/files/justdomains](http://malwaredomains.lehigh.edu/files/justdomains)

2. **PhishTank**  
   URL: [https://data.phishtank.com/data/online-valid.csv](https://data.phishtank.com/data/online-valid.csv)

3. **Tor Exit Nodes (dan.me.uk)**  
   URL: [https://www.dan.me.uk/tornodes](https://www.dan.me.uk/tornodes)

4. **Abuse.ch SSL Blacklist**  
   URL: [https://sslbl.abuse.ch/blacklist/sslblacklist.csv](https://sslbl.abuse.ch/blacklist/sslblacklist.csv)

5. **AlienVault IP Reputation**  
   URL: [http://reputation.alienvault.com/reputation.generic.gz](http://reputation.alienvault.com/reputation.generic.gz)

6. **Abuse.ch URLhaus**  
   URL: [https://urlhaus.abuse.ch/downloads/csv_online/](https://urlhaus.abuse.ch/downloads/csv_online/)

### Not Regularly Updated
- **Feodo Tracker (Abuse.ch)**  
  URL: [https://feodotracker.abuse.ch/downloads/ipblocklist.txt](https://feodotracker.abuse.ch/downloads/ipblocklist.txt)

### Access Denied or Requires Registration
- [http://malwareurl.com](http://malwareurl.com)  
- [http://www.malwareurl.com/reg-export-urls.php](http://www.malwareurl.com/reg-export-urls.php?export=domain&key=PUT_YOUR_KEY_HERE)  
- [http://s3.amazonaws.com/alexa-static/top-1m.csv.zip](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip)

### Unresponsive Links
- [http://malwaredomains.lehigh.edu/files/justdomains](http://malwaredomains.lehigh.edu/files/justdomains)

---

## High-Reliability Public IP Blacklist Sources

### 1. Spamhaus DROP / SBL / XBL / ZEN
- URL: [https://www.spamhaus.org/drop/](https://www.spamhaus.org/drop/)
- Update Frequency: Real-time (DNS-based)
- Cost: Free for small-scale/personal use; licensing required for enterprise use
- Format: DNSBL, plain text, zone files
- Use Case: Blocking malware, spam, and DDoS infrastructure

### 2. Abuse.ch Feodo Tracker
- URL: [https://feodotracker.abuse.ch/blocklist/](https://feodotracker.abuse.ch/blocklist/)
- Update Frequency: Every 5 minutes
- Cost: Free
- Format: Plain text, JSON, Suricata/Snort rules
- Use Case: Detecting botnet command-and-control servers

### 3. Abuse.ch SSL Blacklist (SSLBL)
- URL: [https://sslbl.abuse.ch/](https://sslbl.abuse.ch/)
- Update Frequency: Every 5 minutes
- Cost: Free
- Format: CSV, Suricata/Snort rules
- Use Case: Detecting abused SSL certificates in encrypted C2 channels

### 4. FireHOL IP Blocklists
- URL: [https://iplists.firehol.org/](https://iplists.firehol.org/)
- Update Frequency: Daily
- Cost: Free
- Format: CIDR, ipset-compatible plain text
- Use Case: Categorized firewall filtering; multiple tiers of aggressiveness

### 5. AbuseIPDB
- URL: [https://www.abuseipdb.com/](https://www.abuseipdb.com/)
- Update Frequency: Real-time (API)
- Cost: Free tier with rate limit; paid plans available
- Format: JSON API
- Use Case: Crowd-sourced IP reputation monitoring and abuse reporting

---

## GitHub-Based IP Blacklists

### 1. [stamparm/ipsum](https://github.com/stamparm/ipsum)
- Update Frequency: Daily
- Format: Plain text (`ipsum.txt`), with tiered consensus levels
- Use Case: IP blocking based on aggregated multi-source consensus

### 2. [bitwire-it/ipblocklist](https://github.com/bitwire-it/ipblocklist)
- Update Frequency: Every 2 hours
- Format: Plain text (`ip-list.txt`) with exclusions
- Use Case: General-purpose IP blacklist, combines multiple threat feeds

### 3. [romainmarcoux/malicious-ip](https://github.com/romainmarcoux/malicious-ip)
- Update Frequency: Hourly
- Format: Multiple files, ranked by source frequency
- Use Case: Network perimeter filtering based on consensus scoring

### 4. [romainmarcoux/malicious-outgoing-ip](https://github.com/romainmarcoux/malicious-outgoing-ip)
- Update Frequency: Hourly
- Format: Outgoing IP blocklists by consensus ranking
- Use Case: Blocking phishing or malware beaconing from internal systems

---
