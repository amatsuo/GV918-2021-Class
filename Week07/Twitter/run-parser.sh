#!bin/bash

# need to set crontab
# crontab is a scheduler for linux systems
# the idea is to run this script every 15 min 
# the crontab command is like:
# */15 * * * * bash /path/to/file/run_parser.sh

conda activate gv918
python /path/to/file/parse_tweets_json.py
conda deactviate
