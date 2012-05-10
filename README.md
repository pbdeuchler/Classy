Classy: A naive bayes classifier package for Python
=========================

Bayes all the things!

Classy is an MIT liscensed library written in Python.

Classy is built for simplistic document classification, and is built with web application usage in mind. Classy simplifies
the process down for you, so all you need to do is train it.

::

	>>> c = Classy()
	>>> c.train(['cpu', 'RAM', 'ALU', 'io', 'bridge', 'disk'], 'architecture')
	>>> c.train(['monitor', 'mouse', 'keyboard', 'microphone', 'headphones'], 'input_devices')
	>>> c.train(['desk', 'chair', 'cabinet', 'lamp'], 'office furniture')
	>>> my_office = ['cpu', 'monitor', 'mouse', 'chair']
	>>> c.classify(my_office)
	('input_devices', -7.58003228654052)
	...

Classy has been designed with dynamicism in mind, so it will work with any range of uses- blog entry categorization, ir systems, tag clouds, reccomendation engines and so on.


Features
--------

- Being Awesome


Installation
------------

Fork/clone and pull the code to your local machine and run:

	$ make alpha




Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
#. Fork `the repository`_ on Github to start making your changes to the **develop** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.


.. _`the repository`: http://github.com/pbdeuchler/Classy
.. _AUTHORS: https://github.com/pbdeuchler/Classy/blob/master/AUTHORS.rst

README shamelessly ripped from [requests] [1]

[1]: https://github.com/kennethreitz/requests