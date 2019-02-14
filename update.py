#!/usr/bin/env python3

import os
import subprocess
import sys

def y_n(q):
    while True:
        ri = input('{} (y/n): '.format(q))
        if ri.lower() in ['yes', 'y']: return True
        elif ri.lower() in ['no', 'n']: return False

def update_deps():
    print("Trying to update dependencies...")

    try:
        subprocess.check_call('"{}" -m pip install -U -r requirements.txt'.format(sys.executable), shell=True)
    except subprocess.CalledProcessError:
        raise OSError("\nCould not update dependencies. You will need to run '\"{0}\" -m pip install -U -r requirements.txt' yourself.\n".format(sys.executable))

def finalize():
    try:
        from musicbot.constants import VERSION
        print('\nThe current ChudyBot version is {0}.\n'.format(VERSION))
    except Exception:
        print('\nThere was a problem fetching your current bot version. The installation may not have completed correctly.\n')

    print("\nDone!\n")

def main():
    print('Starting update...')

    update_deps()
    finalize()

if __name__ == '__main__':
    main()
