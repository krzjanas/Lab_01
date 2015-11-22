#!/usr/bin/env python3

import logging

loggerWC = logging.getLogger('wc_log')
fh = logging.FileHandler('wcLog.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(message)s'))
loggerWC.addHandler(fh)

wc_log = logging.getLogger('wc_log.module')
wc_log.setLevel(logging.DEBUG)

def decor(fun,log):
    msg = "Func: "+fun.__qualname__
    def wrapper(*args, **kwargs):
        res = fun(*args, **kwargs)
        log.info(msg+'\t Ans = '+str(res))
        return res
    return wrapper

def decorMod(fun):
    return decor(fun,wc_log)


class PyWC:
    def __init__(self, fileName):
        wc_log.info("Constr: PyWC obiect creation for file "+fileName)

        self.fileName = fileName

        with open(fileName) as fileWC:
            lines = fileWC.readlines()

        self.linesCounter     = len(lines)
        self.wordsCounter      = sum( len(l.split()) for l in lines )
        self.charaktersCounter = sum( len(l) for l in lines )

    @decorMod
    def usedFile(self):
        return self.fileName

    @decorMod
    def countLines(self):
        return self.linesCounter

    @decorMod
    def countWords(self):
        return self.wordsCounter

    @decorMod
    def countCharakters(self):
        return self.charaktersCounter




testFileName = "TestFileForPyWC.dat"
# TestFile:
  #Ala ma kota
  #a kot ma Ale
  #Czy to dziala?
  #Odpowiedz

if __name__ == "__main__":
    mainMod = logging.getLogger('wc_log.module.main')
    mainMod.info('\tStart main in PyWC module')


    try:
        TestWC = PyWC(testFileName)

        print("File for testing: ", TestWC.usedFile())
        print("\tLines      = ", TestWC.countLines())
        print("\tWords      = ", TestWC.countWords())
        print("\tCharakters = ", TestWC.countCharakters())

    except IOError:
        mainMod.error('\tUsuniety plik testowy!\n')

        print("Ktos usunal plik testowy!")
        print("Stworz nowy plik testowy: \n\tTest_PyWC.dat\n a nastepnie umiesc w nim nastepujace linijki:\n")
        print("Ala ma kota\na kot ma Ale\nCzy to dziala?\nOdpowiedz");


    mainMod.info('\tFinish main in PyWC module')

