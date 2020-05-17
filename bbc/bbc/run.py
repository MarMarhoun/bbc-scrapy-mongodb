# -*- coding: utf-8 -*-
"""
Created on Thu May 14 05:25:43 2020

@author: Marouane
"""

from scrapy import cmdline


name = 'bbc'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())