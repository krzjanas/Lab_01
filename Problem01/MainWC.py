#!/usr/bin/env python3

import PyWC
from optparse import OptionParser

import logging

def mainWC():
    mainWC_log = logging.getLogger('wc_log.main')
    mainWC_log.setLevel(logging.DEBUG)
    mainWC_log.info('\tStart MainWC program')


    parser = OptionParser("usage: %prog [options] FILE")
    parser.add_option("-l", action="store_true", dest="lineCount", help="count number of lines")
    parser.add_option("-w", action="store_true", dest="wordCount", help="count number of words")
    parser.add_option("-c", action="store_true", dest="charCount", help="count number of charakters")

    (options, args) = parser.parse_args()

    if(len(args)==0):
        mainWC_log.info('\tfile not specified')
        parser.error("file not specified")


    for f in args:
        try:
            wc = PyWC.PyWC(f)
            print("File = ",wc.usedFile(),":",end="")
            if options.lineCount:
                print("\tL = ",wc.countLines(),end="")
            if options.wordCount:
                print(" W = ",wc.countWords(),end="")
            if options.charCount:
                print("\tC = ",wc.countCharakters(),end="")
            if not(options.lineCount or options.wordCount or options.charCount):
                print("\tL = ",wc.countLines(),end="")
                print("\tW = ",wc.countWords(),end="")
            print()
        except IOError:
            mainWC_log.info('\tFile '+f+' do not exist')
            print('File',f,'do not exist')

    mainWC_log.info('\tFinish MainWC program')

if __name__ == "__main__":
    mainWC()