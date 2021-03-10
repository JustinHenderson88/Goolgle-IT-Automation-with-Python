#!/usr/bin/env python3

import unittest
from emails import find_email

class TestFile(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "bree@abc.edu"
    self.assertEqual(find_email(testcase), expected)

  def test_one_name(self):
    '''Test for a single parameter when expecting two'''
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)
  
  def test_two_name(self):
      '''Test for if employee not found'''
      testcase = [None, "Roy", "Cooper"]
      expected = "No email address found"
      self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
  unittest.main()