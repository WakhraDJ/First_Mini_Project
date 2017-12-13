# First_Mini_Project
Python script for directely connection to local server for novice developers. A basic python script ran form any directory and any platform. Connection to local server 8080(No need for permission in unix or linux).

### Working Directory

Current working directory using System tools:
```sh
os.getcwd()
```

### Requirements
Python 3 or later.

### Quick Start

Used basic import of http.server:
```sh
from http.server import HTTPServer, CGIHTTPRequestHandler
```

Platform Dependent:
```sh
if sys.platform=='win32'
```

For more details please refer to -help:
```sh
help(http.server)
