#!/bin/bash

# A simple bash command for starting the GAE dev_appserver. The GAE SDK must be installed locally.
dev_appserver.py --host=0.0.0.0 --use_mtime_file_watcher yes .
