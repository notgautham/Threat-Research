# Threat Research: Blacklisted IP Sources

This document contains curated and categorized sources for blacklisted IPs useful in threat intelligence, malware detection, and network security systems.

---

## Existing Sources in `badfellas.xml`

### ✅ Regularly Updated
1. **Malware Domains (Lehigh Univ.)**
   - URL: [http://malwaredomains.lehigh.edu/files/justdomains](http://malwaredomains.lehigh.edu/files/justdomains)
2. **PhishTank**
   - URL: [https://data.phishtank.com/data/online-valid.csv](https://data.phishtank.com/data/online-valid.csv)
3. **Tor Exit Nodes (dan.me.uk)**
   - URL: [https://www.dan.me.uk/tornodes](https://www.dan.me.uk/tornodes)
4. **Abuse.ch SSL Blacklist**
   - URL: [https://sslbl.abuse.ch/blacklist/sslblacklist.csv](https://sslbl.abuse.ch/blacklist/sslblacklist.csv)
5. **AlienVault IP Reputation**
   - URL: [http://reputation.alienvault.com/reputation.generic.gz](http://reputation.alienvault.com/reputation.generic.gz)
6. **URLhaus (Abuse.ch)**
   - URL: [https://urlhaus.abuse.ch/downloads/csv_online/](https://urlhaus.abuse.ch/downloads/csv_online/)

### ⚠️ Not Regularly Updated
- **Feodo Tracker IP Blocklist**
  - URL: [https://feodotracker.abuse.ch/downloads/ipblocklist.txt](https://feodotracker.abuse.ch/downloads/ipblocklist.txt)

### 🚫 Yet to be Registered / Access Denied
- [http://malwareurl.com](http://malwareurl.com)
- [http://www.malwareurl.com/reg-export-urls.php?export=domain&key=PUT_YOUR_KEY_HERE](http://www.malwareurl.com/reg-export-urls.php?export=domain&key=PUT_YOUR_KEY_HERE)
- [http://s3.amazonaws.com/alexa-static/top-1m.csv.zip](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip)

### ❌ Unresponsive
- [http://malwaredomains.lehigh.edu/files/justdomains](http://malwaredomains.lehigh.edu/files/justdomains)

---

## High-Reliability Public IP Blacklist Sources

### 1. **Spamhaus DROP / SBL / XBL / ZEN**
- **URL:** [https://www.spamhaus.org/drop/](https://www.spamhaus.org/drop/)
- **Aggressiveness:** Very low false positives, highly curated
- **Update Frequency:** Real-time
- **Cost:** Free (personal/small scale); paid for commercial use
- **Format:** DNSBL, zone files, JSON
- **Best Use:** Global malware/spam/DDOS defense
- **Popularity:** Very high (ISPs, enterprises, firewalls)

### 2. **Abuse.ch Feodo Tracker**
- **URL:** [https://feodotracker.abuse.ch/blocklist/](https://feodotracker.abuse.ch/blocklist/)
- **Aggressiveness:** Very low false positives
- **Update Frequency:** Every 5 minutes
- **Cost:** Free (CC0)
- **Format:** Plain-text IPs, JSON, IDS rules
- **Best Use:** C2/malware detection
- **Popularity:** High in SOCs, malware research

### 3. **Abuse.ch SSL Blacklist (SSLBL)**
- **URL:** [https://sslbl.abuse.ch/](https://sslbl.abuse.ch/)
- **Aggressiveness:** Very low
- **Update Frequency:** Every 5 minutes
- **Cost:** Free
- **Format:** CSV, Suricata/Snort rules
- **Best Use:** Encrypted malware traffic blocking
- **Popularity:** Common in IDS setups

### 4. **FireHOL IP Blocklists**
- **URL:** [https://iplists.firehol.org/](https://iplists.firehol.org/)
- **Aggressiveness:** Varies (some very aggressive)
- **Update Frequency:** Daily
- **Cost:** Free
- **Format:** ipset-ready, CIDR
- **Best Use:** Router/firewall-level blocking
- **Popularity:** High in open-source firewalls

### 5. **AbuseIPDB**
- **URL:** [https://www.abuseipdb.com/](https://www.abuseipdb.com/)
- **Aggressiveness:** Moderate (crowdsourced, tunable thresholds)
- **Update Frequency:** Real-time
- **Cost:** Free tier (1k req/day), paid API plans
- **Format:** JSON API
- **Best Use:** Adaptive and on-demand IP reputation checking
- **Popularity:** High among web security teams

---

## GitHub Blacklist Repositories

### 1. **[stamparm/ipsum](https://github.com/stamparm/ipsum)**
- **Update Frequency:** Daily
- **Format:** Plain text (`ipsum.txt` + consensus levels)
- **Reliability:** High — aggregates from 30+ feeds
- **Best Use:** Firewall/ipset-based blocking, tiered severity

### 2. **[bitwire-it/ipblocklist](https://github.com/bitwire-it/ipblocklist)**
- **Update Frequency:** Every 2 hours
- **Format:** Plain text (`ip-list.txt`), with exclusions
- **Reliability:** Good — multiple reputable sources
- **Best Use:** General threat intelligence, IDS enrichment

### 3. **[romainmarcoux/malicious-ip](https://github.com/romainmarcoux/malicious-ip)**
- **Update Frequency:** Hourly
- **Format:** Sorted IP files (`full-aa.txt`, etc.)
- **Reliability:** High — sorted by source consensus
- **Best Use:** LAN-facing blacklist filters, IP scoring

### 4. **[romainmarcoux/malicious-outgoing-ip](https://github.com/romainmarcoux/malicious-outgoing-ip)**
- **Update Frequency:** Hourly
- **Format:** Text files by rank/consensus
- **Reliability:** High — focuses on outbound threats
- **Best Use:** Blocking phishing, exfiltration, or C2 channels from endpoints

---

## 📌 Notes

- Sources with real-time updates and curated entries (Spamhaus, Abuse.ch) are ideal for production.
- GitHub-based lists are community-driven but excellent for research, enrichment, or defense-in-depth.
- Consider logging update frequency and `hashes` of lists in your automation pipelines to detect feed changes.

---

*Maintained as part of the Threat Research repository. Contributions welcome via pull requests.*
