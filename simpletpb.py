#!/usr/bin/env python
# -*- coding: utf-8 -*
from requests import get
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
import categories as category
import order_by


def search(query, category=category.ALL, order_by=order_by.DEFAULT, page=0):
    """Query to The Pirate Bay
    
    Makes a Request.get() to thepiratebay.org and parses the response text
    with BeautifulSoup

    Args:
        query: a query to search
        category: optional value. Pirate Bay category param to put into the URL
        order_by: optional value. Pirate Bay order param to put into the URL
        category: optional value. Pirate Bay page param to put into the URL

    Returns:
        beautiful soup parsed html
    """
    url = 'https://thepiratebay.org/search/'
    url += quote_plus(query) + '/' + str(page) + '/' + str(order_by) + '/' + str(category)
    print(url)
    return bs(get(url).text, 'html.parser')


def get_magnets(bs_html, limit=1):
    """Gets magnet links from HTML
    
    Searches for the srting "magnet" into attribute href of tags <a> from given HTML.
    Stores the link if the string matches
    
    Args:
        bs_html: beautiful soup parsed html
        limit: An optional variable that determines the length of the
            returned list
    
    Returns:
        A list of magnets of length = limit found into the bs_html or None
    """
    magnets = []

    for link in bs_html.find_all('a'):
        href = link.get('href')
        if 'magnet' in href:
            magnets.append(href)
            limit -= 1
            if limit == 0:
                return magnets

    return None


if __name__ == '__main__':
    from sys import argv
    magnets = get_magnets(search(' '.join(argv[1:])))
    if magnets:
        print(magnets[0])
    else:
        print('No magnets found')
