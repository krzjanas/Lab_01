#!/usr/bin/env python3

from BookParser import BookParser
from optparse import OptionParser

if __name__ == "__main__":
    parser = OptionParser("usage: %prog [options] -f FILE")
    parser.add_option("-f", "--file",  action="store", type="string",   dest="filename",    metavar="FILE",   help="specify FILE with catalog")
    parser.add_option("-i", "--index", action="store", type="int",      dest="index",       metavar="INDEX",  help="print book according to index in catalog")
    parser.add_option("-t", "--tag",   action="store", type="string",   dest="tag",         metavar="TAG",    help="print book according to value of tag (value specified with -v)")
    parser.add_option("-v", "--val",   action="store", type="string",   dest="val",         metavar="VALUE",  help="print book according to value of tag (tag specified with -t)")
    parser.add_option("-a", "--all",   action="store_true",             dest="printAll",    help="print all books")

    (options, args) = parser.parse_args()

    if(options.filename==''):
        parser.error("file not specified")

    try:
        catalog = BookParser(options.filename)

        if options.index!=None:
            print(catalog.tupleBook_idx(options.index))
        if options.tag!=None and options.val!=None:
            for book in catalog.tupleBook_tag(options.tag,options.val):
                print(book)
        if options.printAll:
            print("ALL")
            for book in catalog.catalog():
                print(book)

    except FileNotFoundError:
        print('File',f,'do not exist')
    except ValueError:
        print("You specified wrong tag. Here is list of tags in catalog:");
        print(catalog.tagsInTuple())
    except IndexError:
        print("You specified wrong index. Choose index between 0 -",catalog.numberOfBooks()-1)