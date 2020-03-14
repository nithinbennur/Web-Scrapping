# Web-Scrapping
Make a  multithreaded web scraper which can recursively crawl a website ( along with it’s sub pages) and find a list of all outgoing links.

	For example, if the input is rirm.in

	the web scraper should find all internal links in rirm.in like (rirm.in/about/  , rirm.in/contact/ etc etc still a user specified number of pages say(100/200)) 	then create a CSV of all outgoing links to external websites.

Answer:---->

	Library used in this project are:-->
		a) urllib Module: If webscrapping is done using socket,then all the information of the server will be fetched out so in order to avoid that,
				  we will make use of "urllib".
				   
				  To perform web scrapping using "urllib", we have to use "urlopen()" function present within request module.
			
				  This function takes url as the argument and it will establish the connection with the server as well as it will specify the type 
				   of web request.

				  strip() function is used to eliminate the white spaces.

		b) requests Module: Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to 				    form-encode your POST data.
		
		c) bs4 Module: Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic 				ways of navigating, searching, and modifying the parse tree.
			
		d) lxml Module: lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.



