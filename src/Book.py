from src.Chapter import Chapter
from src.SubChapter import SubChapter
from src.Paragraph import Paragraph
from src.Author import Author


class Book:

    def __init__(self, name):
        self.name = name
        self.author = None
        self.chapters = set()
        self.subChapters = set()
        self.paragraphs = set()

    def setAuthor(self, name, age, mail):
        self.author = Author(name, age, mail)

    def createChapter(self, number, name):
        self.chapters.add(Chapter(number, name))

    def createSubChapter(self, chapter, number, name):
        self.subChapters.add(SubChapter(chapter, number, name))

    def createParagraph(self, subChapter, text):
        line = len(self.paragraphs) + 1
        self.paragraphs.add(Paragraph(subChapter, line, text))

    def showAuthorInfo(self):
        print("Author Information")
        print("Name:" + self.author.getName())
        print("Age:" + self.author.getAge())
        print("Email:" + self.author.getMail())

    def showSummary(self):
        print("Summary")
        for chapter in self.chapters:
            print(str(chapter.getNumber()) + " " + chapter.getName())
            for subChapter in self.subChapters:
                if subChapter.getChapter() is chapter.getNumber():
                    print("->" + str(chapter.getNumber()) + "." + str(subChapter.getNumber()) + " " + subChapter.getName())

    def showBookContent(self):
        for chapter in self.chapters:
            print(str(chapter.getNumber()) + " " + chapter.getName())
            for subChapter in self.subChapters:
                if subChapter.getChapter() is chapter.getNumber():
                    print(" " + str(chapter.getNumber()) + "." + str(subChapter.getNumber()) + " " + subChapter.getName())
                    for paragraph in self.paragraphs:
                        if paragraph.getSubChapter() is subChapter.getNumber():
                            print("  " + paragraph.getText() + str(paragraph.getLine()))


