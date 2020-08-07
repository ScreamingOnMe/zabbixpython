"""
此脚本未用，是网优shell的python版本，自己写着玩   dfd
"""
import sys
import os
import subprocess
FILE_PATH = sys.argv[1]
OMCID = sys.argv[2]
NUM = sys.argv[3]
my_command1 = "date -d '-1 day' +%Y-%m-%d"
my_command4 = "sed -n /%s/p %s | awk '{print $5}'" % (OMCID, FILE_PATH)
my_command5 = "sed -n /%s/p %s | awk '{print $3}'" % (OMCID, FILE_PATH)
TIME1 = subprocess.Popen(my_command1, shell=True,
                         stdout=subprocess.PIPE).stdout.read().strip('\n')

if os.path.exists(FILE_PATH) == False:
    print('0')
else:
    CHECKNUM = subprocess.Popen(
        my_command4, shell=True, stdout=subprocess.PIPE).stdout.read().strip('\n')
    CHECKDAY = subprocess.Popen(
        my_command5, shell=True, stdout=subprocess.PIPE).stdout.read().strip('\n')
    if TIME1 != CHECKDAY:
        print('3')
    else:
        if CHECKNUM <= NUM:
            print('2')
        else:
            print('1')
