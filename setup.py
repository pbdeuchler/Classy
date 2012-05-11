#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    ______   __                                        
#   /      \ /  |                                       
#  /$$$$$$  |$$ |  ______    _______  _______  __    __ 
#  $$ |  $$/ $$ | /      \  /       |/       |/  |  /  |
#  $$ |      $$ | $$$$$$  |/$$$$$$$//$$$$$$$/ $$ |  $$ |
#  $$ |   __ $$ | /    $$ |$$      \$$      \ $$ |  $$ |
#  $$ \__/  |$$ |/$$$$$$$ | $$$$$$  |$$$$$$  |$$ \__$$ |
#  $$    $$/ $$ |$$    $$ |/     $$//     $$/ $$    $$ |
#   $$$$$$/  $$/  $$$$$$$/ $$$$$$$/ $$$$$$$/   $$$$$$$ |
#  										      /  \__$$ |
#  										      $$    $$/ 
#  											   $$$$$$/ 

from distutils.core import setup
import Classy
import os
import sys


if sys.argv[-1] == 'publish':
	os.system('python setup.py sdist upload')
	sys.exit()

def get_file_contents(file_path):
  """Get the context of the file using full path name"""
  full_path = os.path.join(package_directory, file_path)
  return open(full_path, 'r').read()

setup(
	name='Classy',
	version= Classy.__version__,
	author='Philip Deuchler',
	author_email='pbdeuchler@gmail.com',
	packages=['Classy'],
	package_data={'': ['LICENSE', 'README']},
	scripts=[],
	url='http://pypi.python.org/pypi/classy/',
	license=open('LICENSE.txt').read(),
	description='Abstracted naive Bayes classifier for rest of us (Requires Python 2.7 or later)',
	long_description=open('README').read(),
	install_requires=[],
)