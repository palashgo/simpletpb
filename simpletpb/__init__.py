#!/usr/bin/env python
# -*- coding: utf-8 -*
from requests import get
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
from .categories import ALL
from .order_by import DEFAULT

import datetime
import PTN
import re
from dateutil.parser import parse

class Torrent:
    def __init__(self,title,seeds,peers,size,magnet,uploaded_time):
        self.title = title
        self.seeds = int(seeds)
        self.peers = int(peers)
        self.size  = size
        self.magnet = magnet
        self.hash = re.match(".+?([\w]{40})",self.magnet).group(1)
        
        now = datetime.datetime.now()
        if "ago" in uploaded_time:
            minutes = uploaded_time.split(" ")[0]
            self.uploaded_time = now - datetime.timedelta(minutes=int(minutes))
        elif "Y-day" in uploaded_time:
            yesterday = now - datetime.timedelta(1)
            self.uploaded_time = parse(uploaded_time.replace("Y-day",yesterday.strftime("%Y-%m-%d")))
        elif "Today" in uploaded_time:
            self.uploaded_time = parse(uploaded_time.replace("Today",now.strftime("%Y-%m-%d")))
        else:
            self.uploaded_time = parse(uploaded_time)
        
        self.extracted_info = PTN.parse(self.title)

class TPBSearch:
    def __init__(self,query, category=ALL, order_by=DEFAULT, page=0):
        self.soup = self._fetch(query, category, order_by, page)
        self.result = self._parse(self.soup)
    
    def _fetch(self,query, category, order_by, page):
        url = 'https://thepiratebay.org/search/'
        url += quote_plus(query) + '/' + str(page) + '/' + str(order_by) + '/' + str(category)
        print(url)
        return bs(get(url).text, 'html.parser')

    def _parse(self,soup):
        result = []
        for tag in soup.select("#searchResult tr")[1:]:
            title = tag.select_one("a.detLink").text
            seeds = tag.select_one("td:nth-child(3)").text
            peers = tag.select_one("td:nth-child(4)").text
            desc = tag.select_one("font.detDesc").text
            magnet = tag.select_one("a[title=\"Download this torrent using magnet\"]").attrs.get('href')
            size = re.search("Size\s(.+?),", desc).group(1).replace('\xa0',' ')
            uploaded_time = re.search("Uploaded\s(.+?),", desc).group(1).replace('\xa0',' ')
            tr_torrent = Torrent(title,seeds,peers,size,magnet,uploaded_time)
            result.append(tr_torrent)
        return result
