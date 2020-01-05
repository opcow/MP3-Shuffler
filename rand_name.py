import os
import random
import glob
import sys
import math

# requires a target directory. defaults to mp3 files if no wildcards are given
if len(sys.argv) < 2:
    print('Please provide a path to the files and optional file glob.')
    sys.exit(1)

os.chdir(sys.argv[1])
if len(sys.argv) > 2:
    listing = glob.glob(sys.argv[2])
else:
    listing = glob.glob('*.mp3')

# save the number of files found
listlen = len(listing)
if listlen < 1:
    print('\nNo matching files found.')
    exit(0)

# calculate the number of digits needed to represent the number of files
digits = str(math.floor(math.log10(listlen-1)) + 1)
ren_list = []
i = 0
files = random.sample(listing, listlen)
if len(files) == 0:
    print('No files found.')
    exit()

# first get the file list and show the pending changes
for f in files:
    s = f.split('_', 1)
    if len(s) == 2:
        fn = s[1]
    else:
        fn = s[0]
    fmt = '{:0' + digits + 'd}_{}'
    new_name = fmt.format(i, fn)
    print('{} -> {}'.format(f, new_name))
    ren_list.append(new_name)
    i += 1

sys.stdout.write("\nType 'ok' to rename files: ")
choice = input().lower()
i = 0
if choice == 'ok':
    for f in files:
        os.rename(f, ren_list[i])
        i += 1
print('\n' + str(i) + ' files renamed.')
