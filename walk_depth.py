import os, sys, string

path = 'docs_in_test'
path = os.path.normpath(path)
res = []
for root,dirs,files in os.walk(path, topdown=True):
    depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
    if depth == 0: 
	    print depth, " root=", root, "\n", "children -dirs=",dirs,"\n","\n"
	        
	    if depth == 2:
	        # We're currently two directories in, so all subdirs have depth 3
	        res += [os.path.join(root, d) for d in dirs]
	        dirs[:] = [] # Don't recurse any deeper
print res

# developed on base of os.walk and inspried by http://stackoverflow.com/questions/229186/os-walk-without-digging-into-directories-below/234329#23432
