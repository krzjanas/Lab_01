#!/usr/bin/env python3

from unittest import TestCase
from unittest.mock import patch

import PyWC

import logging

testWC_log = logging.getLogger('wc_log.test')
testWC_log.setLevel(logging.DEBUG)

def decorTest(fun):
    return PyWC.decor(fun,testWC_log)

class TestPyWC(TestCase):

    @decorTest
    @patch('PyWC.PyWC._setValues', return_value=None)
    def test_usedFile(self, mock_question):
        testFileName = "TEST.dat"
        TestWC = PyWC.PyWC(testFileName)
        self.assertEqual(TestWC.usedFile(),testFileName)

    @decorTest
    @patch('PyWC.PyWC._setValues', return_value=None)
    def test_countLines(self, mock_question):
        TestWC = PyWC.PyWC("")
        TestWC.linesCounter = 5
        linNumber = 5
        self.assertEqual(TestWC.countLines(),linNumber)

    @decorTest
    @patch('PyWC.PyWC._setValues', return_value=None)
    def test_countWords(self, mock_question):
        TestWC = PyWC.PyWC("")
        TestWC.wordsCounter = 11
        wordsNumber = 11
        self.assertEqual(TestWC.countWords(),wordsNumber)

    @decorTest
    @patch('PyWC.PyWC._setValues', return_value=None)
    def test_countCharakters(self, mock_question):
        TestWC = PyWC.PyWC("")
        TestWC.charaktersCounter = 49
        charNumber = 49
        self.assertEqual(TestWC.countCharakters(),charNumber)


if __name__ == "__main__":
    TestCase.main()
