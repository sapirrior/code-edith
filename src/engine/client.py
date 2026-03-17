from openai import OpenAI
from utils.console import console

def load_client(key, url):
	try:
		client = OpenAI(api_key=key,base_url=url)
		client.models.list() # do a tiny test without losing tokens
		return client
	except Exception as e:
		console.print("[Error] connecting with server.")
		exit(1)