def parse(url):
	from urllib.parse import urlparse
	print(urlparse(url))

url = input("Insira a URL a ser tirada o Parse: ")
parse(url)