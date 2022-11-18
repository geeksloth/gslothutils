def get_mac():
	from uuid import getnode
	return ':'.join(("%012X" % getnode())[i:i+2] for i in range(0, 12, 2))