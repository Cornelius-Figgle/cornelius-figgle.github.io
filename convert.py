#!/usr/bin/env python3

'''
A short Python script to convert markdown files to html. Requires `markdown`
from PyPI or `python3-markdown` from XBPS 
'''


from sys import argv

from markdown import markdown


with open(argv[1], 'r') as infile:
    md_file = infile.read()

html_file = markdown(md_file)

with open(argv[1].replace('md', 'html'), 'w') as outfile:
    outfile.write(html_file)
