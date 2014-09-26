#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HR1


from lxml import html

def parse_playlist(data):
    playlist = []

    root = html.fromstring(data)
    #print data
    laenge = len(root.xpath('//tr'))
    #print laenge
    for x in range(2, laenge + 1):
        date_ = root.xpath("//tr["+str(x)+"]/td[1]/text()")[0].split('.')
        date = date_[2] + "-" + date_[1] + "-" + date_[0]
        time = root.xpath("//tr["+str(x)+"]/td[2]/text()")[0] + ':00'
        artist = root.xpath("//tr["+str(x)+"]/td[3]/text()")[0]
        title = root.xpath("//tr["+str(x)+"]/td[4]/text()")[0]
        duration = ''
        
        playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title, 'duration': duration})
    return reversed(playlist)
