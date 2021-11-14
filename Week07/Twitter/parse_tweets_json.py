#!/usr/bin/env python
# coding: utf-8

# need to set crontab
# crontab is a scheduler for linux systems
# the idea is to run this script every 15 min 
# the crontab command is like:
# */15 * * * * bash run_parser.sh

import json
import csv
import shutil
import bz2
from datetime import datetime
import re
import os


# os.chdir(path) ## need to specify the path to run the command like this

### rename the current file to another name 
shutil.move('tweets.json', 'tweets_temp.json')

### process tweets and save in a csv file

csv_file = open('processed_tweets.csv', mode = 'a')
with open('tweets_temp.json', 'rb') as f:
    for line in f: 
        tweet = json.loads(line) 
        output = [tweet['id_str'], 
                  tweet['text'],
                  tweet['created_at'],
                  tweet['user']['id_str'],
                  tweet['user']['screen_name'],
                  tweet['lang']]
        c_writer = csv.writer(csv_file, delimiter=',', quotechar='"', 
                   quoting=csv.QUOTE_MINIMAL)
        c_writer.writerow(output)
csv_file.close()


### compress the source tweet file in bzip2 format

#### decide file name

source_file = 'tweets_temp.json'
reg = re.compile('\W+')
outfile = "tweets_" + reg.sub('-', str(datetime.now())[:19]) + '.json.bz2'

#### compression

comp = bz2.compress(open(source_file, 'rb').read(), compresslevel = 9)
with open(outfile, 'wb') as fh:
    fh.write(comp)
