def nested_dict(n, type):
	# usage:
	# nested_dict(3, list)
	#
	from collections import defaultdict
	if n == 1:
		return defaultdict(type)
	else:
		return defaultdict(lambda: nested_dict(n-1, type))
