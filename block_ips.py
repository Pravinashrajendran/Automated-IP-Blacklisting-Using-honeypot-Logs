#!/usr/bin/env python3

import json
import subprocess

LOG_FILE = '/cowrie/var/log/cowrie/cowrie.json'
command_counter = {}
blocked_ips = set()

def is_ip_blocked(ip):
    result = subprocess.run(['sudo', 'iptables', '-C', 'INPUT', '-s', ip, '-j', 'DROP'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def block_ip(ip):
    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'])
    print(f"[+] Blocked IP: {ip}")

def main():
    with open(LOG_FILE, 'r') as logfile:
        for line in logfile:
            try:
                event = json.loads(line)
                if event["eventid"] == "cowrie.command.input":
                    ip = event.get("src_ip")
                    if ip:
                        command_counter[ip] = command_counter.get(ip, 0) + 1
                        if command_counter[ip] >= 5 and not is_ip_blocked(ip):
                            block_ip(ip)
                            blocked_ips.add(ip)
            except json.JSONDecodeError:
                continue  # skip malformed lines

if __name__ == "__main__":
    main()

