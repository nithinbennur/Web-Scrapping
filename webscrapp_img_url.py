import urllib.request
if __name__ == '__main__':
	url='http://data.pr4e.org/cover.jpg'
	data=urllib.request.urlopen(url).read()
	
	my_file=open(file='newimage.jpg',mode='wb')
	new_data=my_file.write(data)
	print(new_data)
	print('Image got scrapped!!!!')
