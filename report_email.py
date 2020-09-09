#!/usr/bin/env python3

# Import all the necessary libraries(os, datetime and reports) that will
# be used to process the text data from the supplier-data/descriptions
# directory into the format below:
#
# name: Apple
# weight: 500 lbs
# [blank line]
# name: Avocado
# weight: 200 lbs
# [blank line]
# ...

# Once you have completed this, call the main method which will process
# the data and call the generate_report method from the reports module

# From: automation@example.com
# To: username@example.com
# Replace username with the username given in the Connection Details Panel on the right hand side.
# Subject line: Upload Completed - Online Fruit Store
# E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
# Attachment: Attach the path to the file processed.pdf

import reports
import emails

import os
import datetime

def generate_paragraph(data_list):
    paragraph = ""
    for fruit in data_list:
        paragraph += 'name: ' + fruit['name'] + '\nweight: ' + fruit['weight'] + '\n\n'
    return paragraph

def main():
    desc_dir = "supplier-data/descriptions/"
    desc_files = os.listdir(desc_dir)
    attachment = "/tmp/processed.pdf"
    title = "Processed on " + str(datetime.datetime.now().strftime("%Y-%m-%d")) + '\n'

    email_from = "automation@example.com"
    email_to = "username@example.com"
    email_subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    supplier_data_list = []

    for file in desc_files:
        fruit_data = {}
        with open(desc_dir + file) as f:
            fruit_data['name'] = f.readline().rstrip('\n')
            fruit_data['weight'] = f.readline().rstrip('\n')
            supplier_data_list.append(fruit_data)

    report = reports.generate_report(attachment, title, generate_paragraph(supplier_data_list))

    emails.send_email(emails.generate_email(email_from,
                                            email_to,
                                            subject_line,
                                            email_body,
                                            attachment))

if __name__ == "__main__":
  main()
