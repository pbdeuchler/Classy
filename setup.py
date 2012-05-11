#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 
    _____   __                                        
   /      \ /  |                                       
  /$$$$$$  |$$ |  ______    _______  _______  __    __ 
  $$ |  $$/ $$ | /      \  /       |/       |/  |  /  |
  $$ |      $$ | $$$$$$  |/$$$$$$$//$$$$$$$/ $$ |  $$ |
  $$ |   __ $$ | /    $$ |$$      \$$      \ $$ |  $$ |
  $$ \__/  |$$ |/$$$$$$$ | $$$$$$  |$$$$$$  |$$ \__$$ |
  $$    $$/ $$ |$$    $$ |/     $$//     $$/ $$    $$ |
   $$$$$$/  $$/  $$$$$$$/ $$$$$$$/ $$$$$$$/   $$$$$$$ |
  										     /  \__$$ |
  										     $$    $$/ 
  									  		  $$$$$$/ 
'''


from distutils.core import setup
import Classy
import os
import sys

if sys.argv[-1] == 'publish':
	os.system('python setup.py sdist upload')
	sys.exit()
	
if sys.argv[-1] == 'uninstall':
	os.system('pip uninstall Classy')
	sys.exit()
	
if sys.argv[-1] == "install":
	os.system('pip install Classy')
	sys.exit()
	

setup(
	name='Classy',
	version= Classy.__version__,
	author='Philip Deuchler',
	author_email='pbdeuchler@gmail.com',
	packages=['Classy'],
	package_data={'': ['LICENSE', 'README.rst']},
	scripts=[],
	url='http://pypi.python.org/pypi/classy/',
	license=open('LICENSE.txt').read(),
	description='Abstracted naive Bayes classifier for rest of us (Requires Python 2.7 or later)',
	long_description= open('README.rst').read() + '\n\n' +
					  open('HISTORY.rst').read(),
	install_requires=[],
)