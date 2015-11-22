#!/usr/bin/env python3

from unittest import TestCase

import PyWC

import logging

testWC_log = logging.getLogger('wc_log.test')
testWC_log.setLevel(logging.DEBUG)

def decorTest(fun):
    return PyWC.decor(fun,testWC_log)

class TestPyWC(TestCase):
    testFileName = PyWC.testFileName

    @decorTest
    def test_usedFile(self):
        TestWC = PyWC.PyWC(self.testFileName)
        self.assertEqual(TestWC.usedFile(),self.testFileName)

    @decorTest
    def test_countLines(self):
        TestWC = PyWC.PyWC(self.testFileName)
        linNumber = 4
        self.assertEqual(TestWC.countLines(),linNumber)

    @decorTest
    def test_countWords(self):
        TestWC = PyWC.PyWC(self.testFileName)
        wordsNumber = 11
        self.assertEqual(TestWC.countWords(),wordsNumber)

    @decorTest
    def test_countCharakters(self):
        TestWC = PyWC.PyWC(self.testFileName)
        charNumber = 49
        self.assertEqual(TestWC.countCharakters(),charNumber)


if __name__ == "__main__":
    TestCase.main()
