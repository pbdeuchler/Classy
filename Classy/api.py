# -*- coding: utf-8 -*-

from __future__ import division
from collections import Counter
import threading
import math

'''
Abandoning this branch for now, as I don't think any type of multiprocessing will provide real performance gains due to the GIL
'''

STOP_WORDS = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']

class ClassifierNotTrainedException(Exception):

	def __str__(self):
		return "Classifier is not trained."
		
class ClassifierNotAsyncException(Exception):

	def __str__(self):
		return "This classifier object is not async ready"

class Classy(object):

	def __init__(self, async=False):
		self.async=async
		self.term_count_store = {}
		self.data = {
			'class_term_count': {},
			'beta_priors': {},
			'class_doc_count': {},
		}
		self.total_term_count = 0
		self.total_doc_count = 0
		
	def make_async(self, pool_count):
		self.async = pool_count

	def train(self, document_source, class_id):
		'''
		Trains the classifier.

		'''
		count = Counter(document_source)
		try:
			self.term_count_store[class_id]
		except KeyError:
			self.term_count_store[class_id] = {}
		for term in count:
			try:
				self.term_count_store[class_id][term] += count[term]
			except KeyError:
				self.term_count_store[class_id][term] = count[term]
		try:
			self.data['class_term_count'][class_id] += document_source.__len__()
		except KeyError:
			self.data['class_term_count'][class_id] = document_source.__len__()
		try:
			self.data['class_doc_count'][class_id] += 1
		except KeyError:
			self.data['class_doc_count'][class_id] = 1
		self.total_term_count += document_source.__len__()
		self.total_doc_count += 1
		self._compute_beta_priors()
		return True
		
	def async_train(self, document_sources, class_id):
		if not self.async: raise ClassifierNotAsyncException()
		
		for source in document_sources:
			threading.Thread(target=self.train, args=(source, class_id), kwargs={}).start()

	def classify(self, document_input):
		if not self.total_doc_count: raise ClassifierNotTrainedException()

		term_freq_matrix = Counter(document_input)
		arg_max_matrix = []
		for class_id in self.data['class_doc_count']:
			summation = 0
			for term in document_input:
				try:
					conditional_probability = (self.term_count_store[class_id][term] + 1)
					conditional_probability = conditional_probability / (self.data['class_term_count'][class_id] + self.total_doc_count)
					summation += term_freq_matrix[term] * math.log(conditional_probability)
				except KeyError:
					break
			arg_max = summation + self.data['beta_priors'][class_id]
			arg_max_matrix.insert(0, (class_id, arg_max))
		arg_max_matrix.sort(key=lambda x:x[1])
		return (arg_max_matrix[-1][0], arg_max_matrix[-1][1])

	def _compute_beta_priors(self):
		if not self.total_doc_count: raise ClassifierNotTrainedException()

		for class_id in self.data['class_doc_count']:
			tmp = self.data['class_doc_count'][class_id] / self.total_doc_count
			self.data['beta_priors'][class_id] = math.log(tmp)
			
	def clean_text(self, text_input, parse_stop_words=True, stop_list=STOP_WORDS):
		term_vector = []
		if parse_stop_words:
			for term in text_input.split():
				term_vector.insert(0, term)
			return term_vector
		for term in text_input.split():
			if term not in stop_list:
				term_vector.insert(0, term)
		return term_vector	