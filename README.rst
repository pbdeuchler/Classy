Classy: A naive bayes classifier package for Python
=========================

Bayes all the things!

Classy is an MIT licensed library written in Python.

Classy is built for document classification with web application usage in mind. Classy simplifies
the process down for you, so all you need to do is train it.

::

	>>> c = Classy()
	>>> c.train(['cpu', 'RAM', 'ALU', 'io', 'bridge', 'disk'], 'architecture')
	True
	>>> c.train(['monitor', 'mouse', 'keyboard', 'microphone', 'headphones'], 'input_devices')
	True
	>>> c.train(['desk', 'chair', 'cabinet', 'lamp'], 'office furniture')
	True
	>>> my_office = ['cpu', 'monitor', 'mouse', 'chair']
	>>> c.classify(my_office)
	('input_devices', -1.0986122886681098)
	...

Classy has been designed with flexibility in mind, so it will work with any range of uses- blog entry categorization, ir systems, tag clouds, recommendation engines and so on. Classy treats each document as a "bag of words" and is thus agnostic to content.


Features
--------

- Being Awesome


Installation
------------

To install on your machine: ::

	$ pip install Classy
	
or: ::

	$ easy_install Classy

(But you should use pip)


Contribute
----------
 

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
#. Fork the `repository`_ on Github to start making your changes to the **develop** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to `AUTHORS`_.


README shamelessly ripped from `requests`_


.. _`repository`: https://github.com/pbdeuchler/Classy/
.. _`AUTHORS`: https://github.com/pbdeuchler/Classy/blob/master/AUTHORS.rst
.. _`requests`: https://github.com/kennethreitz/requests/