from unittest import TestCase

import BookParser


class TestBookParser(TestCase):
  testFileName = BookParser.testFileName

  def test_catalogName(self):
    cat = BookParser.BookParser(self.testFileName)
    self.assertEqual(cat.catalogName(),"catalog")

  def test_numberOfBooks(self):
    cat = BookParser.BookParser(self.testFileName)
    self.assertEqual(cat.numberOfBooks(),12)

  def test_catalog(self):
    cat = BookParser.BookParser(self.testFileName)
    books = cat.catalog()
    self.assertEqual(len(books),12)
    self.assertEqual(len(books[0]),7)
    self.assertEqual(books[0][0],'bk101')

  def test_tagsInTuple(self):
    cat = BookParser.BookParser(self.testFileName)
    tags = cat.tagsInTuple()
    self.assertEqual(len(tags),7)
    self.assertEqual(tags[0],'id')
    self.assertEqual(tags[1],'author')

  def test_indexOfTags(self):
    cat = BookParser.BookParser(self.testFileName)
    tags = cat.tagsInTuple()
    for i in range(len(tags)):
      self.assertEqual(i,cat.indexOfTags(tags[i]))

    self.assertRaises(ValueError,cat.indexOfTags,"asdasdasdas")

  def test_tupleBook_tag(self):
    cat = BookParser.BookParser(self.testFileName)
    self.assertEqual(cat.tupleBook_tag("id","bk101")[cat.indexOfTags("id")][0], "bk101")
    booksFan = cat.tupleBook_tag("genre","Fantasy")
    self.assertEqual(len(booksFan),4)
    for book in booksFan:
      self.assertEqual(book[cat.indexOfTags("genre")], "Fantasy")


  def test_tupleBook_idx(self):
    cat = BookParser.BookParser(self.testFileName)
    books = cat.catalog()
    for i in range(0,len(books),4):
      self.assertEqual(books[i],cat.tupleBook_idx(i))
