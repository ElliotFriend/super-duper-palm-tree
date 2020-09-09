#!/usr/bin/env python3

# The content of the report should look like this:
#
# Processed Update on <Today's date>
# [blank line]
# name: Apple
# weight: 500 lbs
# [blank line]
# name: Avocado
# weight: 200 lbs
# [blank line]
# ...

# Using the reportlab Python library, define the method generate_report
# to build the PDF reports. We have already covered how to generate PDF
# reports in an earlier lesson; you will want to use similar concepts to
# create a PDF report named processed.pdf.

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, paragraph])
