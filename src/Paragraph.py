class Paragraph:

    def __init__(self, subChapter, line, text):
        self.subChapter = subChapter
        self.line = line
        self.text = text

    def getSubChapter(self):
        return self.subChapter

    def getLine(self):
        return self.line

    def getText(self):
        return self.text
