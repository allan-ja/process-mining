# -*- coding: utf-8 -*-

import csv
import datetime


originalFile = open('./report_4.csv', newline='')
reader = csv.reader(originalFile, delimiter=',', quotechar='"')

reader.__next__()

timestamp = datetime.date.today()
one_day = datetime.timedelta(days=1)


with open('event_log_4.csv', 'w') as csvfile:
    fieldnames = ['Patient', 'Activity', 'Timestamp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        paths = row[1].split(', ')
        for path in paths:
            writer.writerow({'Patient': row[0], 'Activity': path, 'Timestamp': timestamp})
            timestamp+=one_day
        writer.writerow({'Patient': row[0], 'Activity': row[2], 'Timestamp': timestamp})

originalFile.close
