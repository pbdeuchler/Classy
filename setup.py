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
import os

def get_file_contents(file_path):
  """Get the context of the file using full path name"""
  full_path = os.path.join(package_directory, file_path)
  return open(full_path, 'r').read()

setup(
	name='Classy',
	version= classy.__version__,
	author='Philip Deuchler',
	author_email='pbdeuchler@gmail.com',
	packages=['classy', 'classy.Classy', 'classy.adapters'],
	scripts=[],
	url='http://pypi.python.org/pypi/classy/',
	license=get_file_contents('LICENSE'),
	description='Abstracted naive Bayes classifier for rest of us',
	long_description=open('README.txt').read(),
	install_requires=[],
)