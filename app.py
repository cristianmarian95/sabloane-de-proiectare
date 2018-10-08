from src.Book import Book

book = Book("Hello")
book.setAuthor("Fainisi Marian Cristian", "23", "marian.fainisi95@e-uvt.ro")

book.createChapter(1, "Welcome")
book.createSubChapter(1, 1, "Introduction")

book.createParagraph(1, "Paragraph 1")
book.createParagraph(1, "Paragraph 2")
book.createParagraph(1, "Paragraph 3")
book.createParagraph(1, "Paragraph 4")
book.createParagraph(1, "Paragraph 5")

if __name__ == "__main__":
    print("\n")
    book.showAuthorInfo()
    print("\n")
    book.showSummary()
    print("\n")
    book.showBookContent()
