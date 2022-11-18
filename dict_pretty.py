import json

def dict_pretty(msg):
	return json.dumps(msg, indent=4, sort_keys=False)