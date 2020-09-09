#!/usr/bin/env python3

# Import the necessary Python libraries (eg. shutil, psutil) to write
# this script.

# Complete the script to check the system statistics every 60 seconds,
# and in event of any issues detected among the ones mentioned above, an
# email should be sent with the following content:

# From: automation@example.com
# To: username@example.com
# Replace username with the username given in the Connection Details Panel on the right hand side.
# Subject line:
# ^ Case ^ Subject line ^
# | CPU usage is over 80% | Error - CPU usage is over 80% |
# | Available disk space is lower than 20% | Error - Available disk space is less than 20% |
# | available memory is less than 500MB | Error - Available memory is less than 500MB |
# | hostname "localhost" cannot be resolved to "127.0.0.1" | Error - localhost cannot be resolved to 127.0.0.1 |
#
# E-mail Body: Please check your system and resolve the issue as soon as possible.

import emails

import psutil
import socket

def check_high_cpu(threshold):
    cpu_use = psutil.cpu_percent(interval=1)
    if cpu_use > threshold:
        return True

def check_high_disk(threshold):
    _, _, _, disk_use = psutil.disk_usage('/')
    if disk_use > threshold:
        return True

def check_high_mem(threshold):
    mem_use = psutil.virtual_memory()
    if mem_use.available * 1024 * 1024 < threshold:
        return True

def check_bad_network(hostname, desired_ip):
    ip_addr = socket.gethostbyname(hostname)
    if ip_addr != desired_ip:
        return True

def emails_wrapper(subject):
    sender = "automation@example.com"
    recipient = "user@example.com"
    body = "Please check your system and resolve the issue as soon as possible."

    emails.send_email(emails.generate_email(sender,
                                            recipient,
                                            subject,
                                            body))

def main():
    # Run the various tests, sending necessary emails
    if check_high_cpu(80):
        emails_wrapper("Error - CPU usage is over 80%")
    if check_high_disk(80):
        emails_wrapper("Error - Available disk space is less than 20%")
    if check_high_mem(500):
        emails_wrapper("Error - Available memory is less than 500MB")
    if check_bad_network("localhost", "127.0.0.1"):
        emails_wrapper("Error - localhost cannot be resolved to 127.0.0.1")

if __name__ == "__main__":
    main()
