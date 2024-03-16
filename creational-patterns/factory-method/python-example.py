from abc import ABC, abstractmethod


# Abstract Product
class Document(ABC):
    @abstractmethod
    def parse_content(self) -> str:
        pass


# Concrete Products
class XMLDocument(Document):
    def parse_content(self) -> str:
        return "XML Document"


class JSONDocument(Document):
    def parse_content(self) -> str:
        return "JSON Document"


# Abstract Creator
class DocumentLoader(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

    def load_document(self) -> str:
        document = self.create_document()
        return document.parse_content()


# Concrete Creators
class XMLDocumentLoader(DocumentLoader):
    def create_document(self) -> Document:
        return XMLDocument()


class JSONDocumentLoader(DocumentLoader):
    def create_document(self) -> Document:
        return JSONDocument()


def client_code(creator: DocumentLoader) -> None:
    print(f"Loaded: {creator.load_document()}")


# Client Code
if __name__ == "__main__":
    print("Loading Document...")
    client_code(XMLDocumentLoader())

    print("\n")

    print("Loading another Document...")
    client_code(JSONDocumentLoader())
