import os
import datetime
import pytz
import re

if __name__ == "__main__":

    eastern=pytz.timezone("US/Eastern")
    et_time=datetime.datetime.now(eastern)
    et_day=et_time.date()

    date=et_day.strftime("%Y/%m/%d")
    path=f'data/{date}'
    cmd=f'rm -rf {path}; mkdir -p {path}'
    os.system(cmd)
    
    cmd=f'python3 src/yahoo-option.py QQQ {path}'
    os.system(cmd)

    cmd=f'git add {path}/*.csv'
    os.system(cmd)
