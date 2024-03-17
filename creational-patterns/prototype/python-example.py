import copy


# Prototype
class DocumentPrototype:
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return self.__class__.__name__


# Concrete Prototype
class Report(DocumentPrototype):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"Report - {self.content}"


# Client Code
if __name__ == "__main__":
    report_template = Report("Prototype Pattern Example")
    report_clone = report_template.clone()

    print(report_template)
    print(report_clone)
