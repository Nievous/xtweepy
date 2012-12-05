# -*- coding=utf-8 -*-
import sys
import os
from setuptools import setup

reload(sys)
sys.setdefaultencoding('utf-8')

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

files = ['xtweepy/*']


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'xtweepy',
    version = '0.0.1',
    author = 'Daniel Mondaca Seguel',
    author_email = 'dnielm@gmail.com',
    description = ('tweepy based library with 1.1 search api support'),
    license = 'MIT',
    keywords = 'twitter library',
    url = 'http://www.example.com',
    packages=['xtweepy'],
    install_requires = ['simplejson', 'tweepy'],
    long_description=read('README.txt'),
    package_data = {'package' : files },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development',
        'License :: custom',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],
)