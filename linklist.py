# -*- coding: UTF-8 -*-
import random
from Link import *

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_LEN = len(LETTERS)

if __name__ == '__main__':
  link = Link()
  link.read_file('/home/sakebow/python/linklist/linklist.csv')
  # link.delete_node_by_index(link.length)
  link.delete_node_by_data('3')
  link.output()
  pass