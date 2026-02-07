# NetSec Lab

Created by **BitJacker**

## Overview
**NetSec Lab** is a modular network security testing framework designed to
analyze **network resilience**, **latency degradation**, **traffic anomalies**,
and the effectiveness of **defensive monitoring systems**.

The project is built for **controlled laboratory environments** and
**defensive cybersecurity research**, focusing on visibility, detection,
and stability rather than exploitation.

---

## Features
- Network stress and resilience testing
- MTU and fragmentation analysis
- Latency and packet loss monitoring
- HTTP and DNS traffic load testing
- Port scanning for network visibility
- Firewall and IDS/IPS behavior validation
- Modular, menu‑driven architecture

---

## Use Cases
- Cybersecurity training labs
- Network resilience validation
- Blue Team and SOC exercises
- Defensive detection tuning
- Educational and research environments

---

## Project Structure

cybersecurity-network-testing/
├── core/ # Menu, launcher, shared utilities
├── network/ # Network-level tests (MTU, fragmentation, scans)
├── application/ # Application-layer tests (HTTP, DNS, TLS)
├── detection/ # IDS, firewall, and rate-limit validation
├── monitoring/ # Latency, packet loss, traffic capture
├── reports/ # Report generation
├── requirements.txt
└── README.md


---

## Requirements
- Linux (tested on Kali Linux)
- Python 3.10+
- iperf3
- tc (netem)
- stress-ng (optional)
- Python dependencies listed in `requirements.txt`

---

## Installation
```bash
git clone https://github.com/BitJacker/cybersecurity-network-testing.git
cd cybersecurity-network-testing

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

Usage

Start the main interface with: python3 core/menu.py
You will be presented with an interactive menu to launch
network, application, monitoring, and detection tests.

Each module will prompt for the required parameters
(target IP, URL, domain, or test size) and display results
directly in the terminal.

Notes

Tests support private IP ranges (e.g. 192.168.1.0/24)

Designed for observability, not exploitation

Results can be used to tune firewalls, IDS/IPS, and monitoring tools

Disclaimer

This project is intended only for educational and defensive purposes.

Do NOT use this tool against networks, systems, or services
you do not own or have explicit authorization to test.

The author assumes no responsibility for misuse.


---


