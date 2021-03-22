#!/usr/bin/python3

import sys
import os

def get_size(path):

	total = 0

	for entry in os.scandir(path):
		try:
			if(entry.is_dir(follow_symlinks=False)):
				total += get_size(entry.path)
			else:
				total += entry.stat(follow_symlinks=False).st_size
		except Exception as e:
			print("Exception: ", e)
			total +=0
	return total


if __name__ == "__main__":
	path = "/home"
	print("Total arguments passed: ", len(sys.argv))

	dir = sys.argv[1] if len(sys.argv) >= 2 else path

	for entry in os.scandir(dir):
		print(entry)
		if (entry.is_dir(follow_symlinks=False)):
			print(entry.path + " is a dir")
			print(get_size(entry.path))
