import re
import os
from datetime import datetime
import time
import email.utils

from mutagen.mp3 import MP3
from pathlib import Path
import math

xml1 = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
    xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>The Ruth Barnes ♥</title>
    <itunes:author>Readerabi</itunes:author>
    <description>Good voice acting takes a lot of hard work, patience, and tenacity, but can also be a fun and rewarding. Vocal qualities include volume, pace, pitch, rate, rhythm, fluency, articulation, pronunciation, enunciation, tone, to name a few.</description>
    <itunes:image href="https://perwad.in/x/rb/ruth.jpg"/>
    <language>en-uk</language>
    """


with open('ruth.txt') as f:
    lines = f.readlines()
data = []
count = 11
for line in lines:
    line = line.strip()
    title = line[8:-4].replace(" - ", "HYPHEN").replace("-", " ").replace("HYPHEN", " - ")

    reg = re.compile(r'^(....)(..)__')
    mo = reg.search(line)
    year = int(mo.group(1))
    month = int(mo.group(2))
    dt = datetime(year=year, month=month, day=count)
    count+=1
    dd = email.utils.format_datetime(dt) # time.mktime(dt.timetuple())
    p = Path(line)
    duration = 12*60+34;
    if os.path.isfile(p.name):
        audio = MP3(p.name)
        duration = audio.info.length
    data.append({
        "title": title,
        "datet": dd,
        "url": "https://perwad.in/x/rb/" + line,
        "dur": duration
    })


'''
    f = open(line.strip(), "r")
    fc = f.read()
    reg = re.compile(r'<meta property="og:title" content="([^"]*)')
    mo = reg.search(fc)
    title = mo.group(1)
    title = re.sub(" [–-] Podcast$", "", title,flags=re.IGNORECASE)
    reg = re.compile(r'<meta property="article:published_time" content="([^"]*)')
    mo = reg.search(fc)
    datet = mo.group(1)
    reg = re.compile(r'<meta name="description" content="([^"]*)"')
    mo = reg.search(fc)
    desc = mo.group(1)
    reg = re.compile(r'href="([^"]*.mp3)"')
    mo = reg.search(fc)
    url = mo.group(1)
    p = Path(url)
    duration = 12*60+34;
    if os.path.isfile("mp3/"+p.name):
        audio = MP3("mp3/"+p.name)
        duration = audio.info.length
    data.append({
        "title": title, 
        "datet": datet, 
        "desc":desc, 
        "url":url,
        "dur": duration
        })
'''
import json


from dateutil import parser
strtime = '2009-03-08T00:27:31.807Z'

def takeSecond(d):
    epoch = parser.parse(d["datet"]).timestamp()
    return epoch

#data.sort(key=takeSecond)
count=0
for d in data:

    min = math.floor(d["dur"]/60)
    sec = round((d["dur"]-min*60))
    xml1 += "\n<item>"
    #print('"'+d["title"]+'",')
    xml1 += "\n  <title>😍 {}</title>".format(d["title"])
    #xml1 += "\n  <description>{}</description>".format(d["desc"])
    xml1 += "\n  <pubDate>{}</pubDate>".format(d["datet"])
    xml1 += "\n  <enclosure url=\"{}\" type=\"audio/mpeg\" length=\"34216300\"/>".format(d["url"])
    xml1 += "\n  <itunes:duration>{:02}:{:02}</itunes:duration>".format(min, sec)
    xml1 += "\n</item>\n"

xml1 += "</channel></rss>"

print(xml1)
