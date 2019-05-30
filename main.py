import requests
from bs4 import BeautifulSoup

# Next we declare a variable for the url of the page.
#specify the url
quote_page = 'https://dailyhive.com/vancouver'

# Then make use of the Python urllib2 to get the HTML page of the url declared.
# query the website and return the html to the variable 'page'
page = requests.get(quote_page)

# Finally, parse the page into BeautifulSoup format so we can use BeautifulSoup to work on it (Create a BeautifulSoup object).
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page.text, 'html.parser')

# Now we have a variable named 'soup' that contains the HTML of the page. Here's where we can start coding
# the part that extracts the data.

print (soup)