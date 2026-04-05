# Automated IP Blacklisting Using Honeypot Logs

## Project Overview

This project is designed to detect and prevent SSH brute-force attacks using a honeypot-based approach. It uses the Cowrie SSH honeypot to capture attacker activity and integrates with the ELK Stack (Elasticsearch, Logstash, and Kibana) for log processing and visualization.

A Python script is used to analyze attacker behavior from the logs and automatically block malicious IP addresses when suspicious activity is detected. This helps in improving system security by enabling faster and automated response to attacks.

## Features

* Cowrie honeypot for capturing SSH attack attempts
* ELK Stack integration for log collection and visualization
* Automated IP blocking based on attacker commands
* Cron job scheduling for continuous monitoring
* Simple and organized project structure

## Architecture

Attacker → Cowrie Honeypot → Logstash → Elasticsearch → Kibana
Python Script → Firewall (IP Blocking)

## Technologies Used

* Cowrie Honeypot
* Elasticsearch
* Logstash
* Kibana
* Python
* Linux (Ubuntu recommended)

## Installation

### Clone the Repository

git clone https://github.com/Pravinashrajendran/Automated-IP-Blacklisting-Using-honeypot-Logs.git
cd Automated-IP-Blacklisting-Using-honeypot-Logs

### Setup Cowrie Honeypot

git clone https://github.com/cowrie/cowrie.git
cd cowrie
./bin/cowrie start

### Install ELK Stack

Install Elasticsearch, Logstash, and Kibana and start the services:

sudo systemctl start elasticsearch
sudo systemctl start logstash
sudo systemctl start kibana

### Configure Logstash

Use the configuration file provided in the logstash folder to forward Cowrie logs to Elasticsearch.

### Install Python Requirements

pip install -r requirements.txt

## Usage

Start the Cowrie honeypot and ELK services.

Run the IP blocking script:
python scripts/ip_blocker.py

To automate the process, add a cron job:
crontab -e

Example:
*/5 * * * * python3 /path/to/scripts/ip_blocker.py

## Folder Structure

scripts/        Python scripts for IP blocking
sample_logs/    Sample Cowrie logs
logstash/       Logstash configuration
cron/           Cron job setup

## Output

* Detection of SSH brute-force attacks
* Collection of attacker IP addresses and commands
* Automatic blocking of malicious IPs
* Visualization of attack activity in Kibana dashboards

## Conclusion

This project demonstrates how honeypot data can be used to detect real-world attacks and respond automatically. It provides a practical implementation of threat detection and prevention using open-source tools.

## Author

Pravinash SMR
Master’s in Cybersecurity

## Future Work

* Machine learning-based attack detection
* Integration with threat intelligence feeds
* Real-time alerting system
* Enhanced Kibana dashboards
