#!/usr/bin/env python3

import xml.etree.ElementTree as ET

class BookParser:

    def __init__(self, fileName):
        tree = ET.parse(fileName)
        self.root = tree.getroot()
        self.books = []

        for child in self.root:
            tmpList = [ child.attrib["id"] ]
            for tag in self.tagsInTuple()[1:]:
                if child.find(tag) != None:
                    tmpList.append(child.find(tag).text)
                else:
                    tmpList.append("-")
            tmpList[-1] ="".join([lin.strip() for lin in tmpList[-1].splitlines()])
            self.books.append( tuple( tmpList ) )

    def catalogName(self):
        return self.root.tag

    def numberOfBooks(self):
        return len(self.books)

    def catalog(self):
        return self.books

    def tagsInTuple(self):
        entry = self.root[0]
        listOfChildren = [ child.tag for child in entry]
        listOfChildren.insert(0,"id")
        return tuple(listOfChildren)

    def indexOfTags(self,tag):
        if self.tagsInTuple().count(tag) == 0:
            raise ValueError
        return self.tagsInTuple().index(tag)

    def tupleBook_tag(self,tag,attrib):
        index = self.indexOfTags(tag)
        tagBooks = []
        for book in self.books:
            if book[index] == attrib:
                tagBooks.append( book );
        return tagBooks

    def tupleBook_idx(self,index):
        return self.books[index]

    def print(self,tags='author',first=0,last=-1):
        for tag in tags:
            self.indexOfTags(tag)

        for book in self.books[first:last]:
            for tag in tags:
                print(book[self.indexOfTags(tag)],"\t",end="")
            print()


testFileName = "TestFileForBookParser.xml"

###################################

if __name__ == "__main__":
    try:
        catalog = BookParser(testFileName)

        print("Catalog name    = ", catalog.catalogName() )
        print("Number of books = ", catalog.numberOfBooks() )
        print("Infos a. book   = ", catalog.tagsInTuple() )

        print("Find book acc. index (no id):")
        print(catalog.tupleBook_idx(2))
        print("Find books acc. author:")
        for book in catalog.tupleBook_tag('author','Corets, Eva'):
            print(book)


        print("\nWszystkie ksiazki z przedzialu 2-5, autor - tytul")
        catalog.print(('author','title'),2-7)


    except FileNotFoundError:
        print("Ktos usunal plik testowy!")