#!/usr/bin/env python
# -*- coding: utf-8 -*
from requests import get
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
from .categories import ALL
from .order_by import DEFAULT


def search(query, category=ALL, order_by=DEFAULT, page=0):
    """Query to The Pirate Bay
    
    Makes a Request.get() to thepiratebay.org and parses the response text
    with BeautifulSoup

    Returns:
        beautiful soup parsed HTML
    """
    url = 'https://thepiratebay.org/search/'
    url += quote_plus(query) + '/' + str(page) + '/' + str(order_by) + '/' + str(category)
    print(url)
    return bs(get(url).text, 'html.parser')


def get_magnets(bs_html):
    """Gets magnet links from HTML
    
    Searches for the string "magnet" into attribute href of <a> tags from given HTML
    and returns the occurrences as a list
    
    Args:
        bs_html: beautiful soup parsed HTML
    """
    hrefs = list(map(lambda link: link.get('href'), bs_html.find_all('a')))
    return list(filter(lambda href: href.startswith('magnet'), hrefs))


