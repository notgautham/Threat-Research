
# IP Blacklist DB (Tokyo Cabinet)

This script fetches a list of malicious IPs from a trusted GitHub source and stores them in a fast Tokyo Cabinet hash database (`.tch`) with associated metadata.

## Source Used

- GitHub Repo: https://github.com/romainmarcoux/malicious-outgoing-ip  
- Type: Malicious outgoing IPs  
- Updated: Hourly  
- Format: Plain text (1 IP per line)

---

## Setup Instructions

### 1. Clone & Navigate

```bash
git clone https://github.com/yourusername/Threat-Research.git
cd Threat-Research/ip_blacklist-db
````

---

### 2. Install Requirements

```bash
sudo apt install tokyocabinet-bin
```

```bash
python3 -m venv tc_env
source tc_env/bin/activate
pip install requests
```

---

### 3. Run Script

```bash
python source1.py
```

This creates a `blacklist_ips.tch` file where:

* **Keys** = IP addresses
* **Values** = Metadata (source repo, type, category)

---

## View Stored Entries

View the first 50 IPs:

```bash
tchmgr list blacklist_ips.tch | head -n 50
```

View value of a specific IP:

```bash
tchmgr get blacklist_ips.tch <ip-address>
```

---

## Files

* `source1.py` – Python script to fetch and insert IPs
* `blacklist_ips.tch` – Tokyo Cabinet database storing key-value entries

---
