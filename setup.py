#! /usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from os import path
import codecs
import os
import re
import sys



here = path.abspath(path.dirname(__file__))

# pompé sur django-fluent-contents
# https://github.com/edoburu/django-fluent-contents/blob/99f9c4531255f5510ef802fdda4f1aa8da5e69b5/setup.py
def read(*parts):
    file_path = path.join(here, *parts)
    return codecs.open(file_path, encoding='utf-8').read()

# le PEP 396 décourage l'import du __init__ dans le setup.py
# donc on va parser
# pompé sur django-fluent-contents
# https://github.com/edoburu/django-fluent-contents/blob/99f9c4531255f5510ef802fdda4f1aa8da5e69b5/setup.py
def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")

setup(
    name='wsb-django-devutils',
    version=find_version('devutils', '__init__.py'),

    description=u'A couple utilities for django developpers',
    long_description=read('README.rst'),

    install_requires=[
        # nothing yet actually
        ],

    requires=[
        'Django (>=1.4)',
        ],

    author='WSB-agency',
    url='http://projets.websiteburo.com/projects/wsb-django-devutils/',

    packages=find_packages(),
    include_package_data=True,

    classifiers=[
        'Development status :: 0.0.1'
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System:: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Softare Development :: Libraries :: Application Frameworks',
        'Topic :: Softare Development :: Libraries :: Python Modules',
    ],
)


