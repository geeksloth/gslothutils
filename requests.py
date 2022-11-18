import requests
import time
from .log import log
import os


class FakeResponse:
	def __init__(self, text, status_code, data):
		self.text=text
		self.status_code=status_code
		self.data=data
	def json(self):
		return {"text":self.text,"status_code":self.status_code, "data":self.data}

def get(url=None, headers=None, verify=False, retry=1, retry_delay=0.25, fake=False):
	if fake:
		response=FakeResponse(text="Fake-OK", status_code=200, data={"timestamp":time.time()})
		return response
	try:
		response = requests.get(url, headers=headers, verify=verify)
	except requests.exceptions.RequestException as e:
		log.critical(e)
		response=FakeResponse(text="FAIL", status_code=400, data={"timestamp":time.time()})

	if response.status_code == 200:
		result = os.path.basename(__file__) + " get successful"
		log.debug(result)  
	else:
		if retry > 1:
			time.sleep(retry_delay)
			response = get(url=url, headers=headers, retry=retry-1, verify=verify)
			if response.status_code == 200:
				result = os.path.basename(__file__) + " re-get successful"
				log.debug(result)
			else:
				log.warning(response.text)
			result = response.text
	return response


def post(url=None, headers=None, verify=False, retry=1, retry_delay=0.25, fake=False):
	if fake:
		class FakeResponse:
			def __init__(self, text, status_code, data):
				self.text=text
				self.status_code=status_code
				self.data=data
			def json(self):
				return {"text":self.text,"status_code":self.status_code, "data":self.data}
		response=FakeResponse(text="OK", status_code=200, data={"timestamp":timetime()})
		return response
	if verify:
		response = requests.post(url, headers=headers, verify=verify)
	else:
		response = requests.post(url, headers=headers, verify=False)
	if response.status_code == 200:
		result = os.path.basename(__file__) + " post successful"
		log.debug(result)  
	else:
		if retry > 1:
			time.sleep(retry_delay)
			response = post(url=url, headers=headers, retry=retry-1, verify=verify)
			if response.status_code == 200:
				result = os.path.basename(__file__) + " re-post successful"
				log.debug(result)
			else:
				log.warning(response.text)
			result = response.text
	return response