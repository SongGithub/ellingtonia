import os, sys, string
from  jinjaconf import messenger

# path = sys.argv[1]
path = 'docs_in_test'
# path = os.path.normpath(path)
alist = [1,2,3,4]

for root,dirs,files in os.walk(path, topdown=True):
    depth = root[len(path) + len(os.path.sep):].count(os.path.sep)

    if depth == 0: 

	    # print len(dirs) ,"root_dir = ", root, "\n", "children_dirs=",dirs,"\n"
        
        messenger(depth, root, dirs)
    elif depth == 2:
	        dirs[:] = [] # Don't recurse any deeper


# developed on base of os.walk and inspried by http://stackoverflow.com/questions/229186/os-walk-without-digging-into-directories-below/234329#23432
