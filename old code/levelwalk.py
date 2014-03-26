import os
import sys
'''this program is a compliment to os.walk with capability of limiting levels of search'''
# def walklevel(some_dir, level):

some_dir = sys.argv[1]
level=2

some_dir = some_dir.rstrip(os.path.sep)
assert os.path.isdir(some_dir)
num_sep = some_dir.count(os.path.sep)

for directory, dirnames, filenames  in os.walk(some_dir):
    # yield directory, dirnames, filenames 
    num_sep_this = directory.count(os.path.sep)
    if num_sep + level <= num_sep_this:
        del dirnames[:]

# walklevel(sys.argv[1], 2)