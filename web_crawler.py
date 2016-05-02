#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import sys

arg_num = len(sys.argv)

if(arg_num == 2):
    url = "http://www.shopping.com/products?KW=%s" % sys.argv[1]
    contents = urllib2.urlopen(url).read()
    soup = BeautifulSoup(contents, "lxml")
    soup.prettify()
    total = soup.find('span', {'class': 'numTotalResults'})
    print "The total number of results for the given keyword \"%s\" is: %s" % (sys.argv[1], total.text[19:])

if(arg_num == 3):
    url = "http://www.shopping.com/products~PG-%s?KW=%s" % (sys.argv[1], sys.argv[2])
    contents = urllib2.urlopen(url).read()
    soup = BeautifulSoup(contents, "lxml")
    soup.prettify()
    product = soup.findAll('div', {'class': 'gridItemBtm'})
    count = len(product)
    print "The total number of results in page \"%s\" for the given keyword \"%s\" is: %s" % (sys.argv[1], sys.argv[2], count)
    print "The results are :"
    for i in range(0, count):
        title = product[i].find('span').get('title')
        if(title is None):
            title1 = product[i].find('a').get('title')
            print ("%s: %s") % (i+1, title1)
        else:
            print ("%s: %s") % (i+1, title)
