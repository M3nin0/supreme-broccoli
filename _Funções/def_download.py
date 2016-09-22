def download(url):
	import urllib.request
	site_page, cabec  = urllib.request.urlretrieve(url)
	html = open(site_page)
	print(html)

url = input("Insira a url do site que será feito o download: ")
download(url)
