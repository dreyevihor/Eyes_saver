#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import time


if __name__ == "__main__":
	while True:
		time.sleep(60*1)
		subprocess.call("python3 open_image.py", shell=True)
		
