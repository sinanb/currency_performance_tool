import sys
import requests
import json
import time

EXPECTED_ARGUMENT_COUNT = 2

def httpRequest(url) :
	#print(url)
	r = requests.get(url)
	# print(len(r.content))
	# print(r.json())
	return len(r.content) , r.json()

def help() :
	print("Please see the usage details")
	print("\t%s url" % (sys.argv[0]))
	return None

if __name__== "__main__":
	if (len(sys.argv) != EXPECTED_ARGUMENT_COUNT) :
		help()
	else :
		start = time.time()
		length, json_data = httpRequest(sys.argv[1])
		# Handle negative case
		end = time.time()
		time_elapsed = end - start
		print(time_elapsed)
		print(length)
		print(length / time_elapsed)

 