from unittest import TestCase
from mock import patch
import sys

import MainWC

class TestMainWC(TestCase):

  def test_should_return_number_of_words(self):
    testargs = ['test_PyWC', '-w',"TestFileForPyWC.dat"]
    with patch.object(sys, 'argv', testargs):
      self.assertEqual(MainWC.mainWC(), "File =  TestFileForPyWC.dat : W =  11")

