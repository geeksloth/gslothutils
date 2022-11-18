import json

def pprint(msg):
	print(json.dumps(msg, indent=4, sort_keys=False))