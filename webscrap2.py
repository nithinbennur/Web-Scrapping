from threading import *
import urllib.request
import requests
import bs4
def Finding_link():
	my_condition.acquire()
	res=requests.get('https://rirm.in')
	soup=bs4.BeautifulSoup(res.text,'lxml')
	for link in soup.find_all('a',href=True):
		print(link['href'])
	my_condition.notify()
	my_condition.release()


def contact_info():
	my_condition.acquire()
	url='https://rirm.in/contact'
	data=urllib.request.urlopen(url)
	count=dict()
	
	for i in data:
		new_data=i.decode().split()
		print(new_data)


		for j in new_data:
			count[j]=count.get(j,0)+1

	print(count)
	my_condition.notify()
	my_condition.release()

def about_info():
	my_condition.acquire()
	url='https://rirm.in/about'
	data=urllib.request.urlopen(url)
	count=dict()
	
	for i in data:
		new_data=i.decode().split()
		print(new_data)


		for j in new_data:
			count[j]=count.get(j,0)+1

	print(count)
	my_condition.notify()
	my_condition.release()

def perspective_info():
	my_condition.acquire()
	url='https://rirm.in/perspectives'
	data=urllib.request.urlopen(url)
	count=dict()
	
	for i in data:
		new_data=i.decode().split()
		print(new_data)


		for j in new_data:
			count[j]=count.get(j,0)+1

	print(count)
	my_condition.notify()
	my_condition.release()

if __name__ == '__main__':
	my_condition=Condition()
	find_link=Thread(target=Finding_link,name='findinglinks')
	contact_thread=Thread(target=contact_info,name='contactinformation')
	about_thread=Thread(target=about_info,name='aboutinformation')
	perspective_thread=Thread(target=perspective_info,name='perspectivesinformation')
	find_link.start()
	contact_thread.start()
	about_thread.start()
	perspective_thread.start()
