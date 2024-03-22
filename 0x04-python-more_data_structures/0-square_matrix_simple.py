#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	new_matrix = list(map(lambda raw : list(map(lambda x : x ** 2, raw)), matrix))
