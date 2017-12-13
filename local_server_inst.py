""" Connects to localmachine, using 8080 server address and open the directory page as well of the current directory"""

import sys, os, subprocess
from subprocess import Popen

file=os.getcwd()
a = open('webserver1.py','w') #creates the important webserver file for connection
a.write('\nimport os, sys\nfrom http.server import HTTPServer, CGIHTTPRequestHandler\n\nwebdir = "' + file + '"\nport = 8080\n\nos.chdir(webdir)\nsrvraddr = ("", port)\nsrvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)\nsrvrobj.serve_forever()\n\n')
a.close()

if sys.platform=='win32':     #Platform dependencies
    os.startfile('http://localhost:8080')
elif sys.platform=='darwin':
    subprocess.Popen(['open', 'http://localhost:8080'])
else:
    try:
        subprocess.Popen(['xdg-open', 'http://localhost:8080'])
    except OSError:
        print ('Please open a browser on: http://localhost:8080')
os.system('python3 webserver1.py') #Runs only on Python3 & >

