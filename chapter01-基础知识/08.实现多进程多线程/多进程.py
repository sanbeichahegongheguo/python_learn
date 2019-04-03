#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Title     : TODO
# Objective : TODO
# Created by: liumian
# Created on: 2019/3/10

import time
import requests
import multiprocessing
from multiprocessing import Pool
from bs4 import BeautifulSoup

MAX_WORKER_NUM = multiprocessing.cpu_count()

t1 = time.time()

urls = ['<https://movie.douban.com/top250?start={}&filter=>'.format(i) for i in range(0, 226, 25)]

def job(url):
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    item = soup.select(".item")
    for i in item:
        print(i.select(".title")[0].text)

p = Pool(MAX_WORKER_NUM)
for url in urls:
    p.apply_async(job, args=(url, ))
p.close()
p.join()
print("耗时:", time.time()-t1)
