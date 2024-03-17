# Product
class Document:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def __str__(self):
        return "\n".join(self.parts)


# Builder
class DocumentBuilder:
    def __init__(self):
        self.document = Document()

    def add_header(self, header):
        self.document.add(f"Header: {header}")

    def add_paragraph(self, paragraph):
        self.document.add(f"Paragraph: {paragraph}")

    def add_footer(self, footer):
        self.document.add(f"Footer: {footer}")

    def reset(self):
        self.document = Document()

    def build(self):
        return self.document


# Director
class DocumentDirector:
    def __init__(self, builder: DocumentBuilder):
        self.builder = builder

    def construct_report(self):
        self.builder.reset()
        self.builder.add_header("Report Header")
        self.builder.add_paragraph("Report Content")
        self.builder.add_footer("Report Footer")

    def construct_letter(self):
        self.builder.reset()
        self.builder.add_header("Letter Header")
        self.builder.add_paragraph("Dear recipient, ...")
        self.builder.add_footer("Letter Footer")


# Client Code
if __name__ == "__main__":
    builder = DocumentBuilder()
    director = DocumentDirector(builder)

    director.construct_report()
    report = builder.build()
    print(report)

    print("\n")

    director.construct_letter()
    letter = builder.build()
    print(letter)
