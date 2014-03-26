import os
import sys

level_counter = 0

for directory, dirnames, filenames in os.walk(sys.argv[1]):
	
    print "\n directory: {} \n".format(directory)

    i = 1 
    for dirname in dirnames:
        print " with in this folder: subdirectory #{}'s name is: {}".format(i,dirname)
        i=i+1
    level_counter = level_counter + 1
    if level_counter == 0:
    	break
print "directory count = " , level_counter

