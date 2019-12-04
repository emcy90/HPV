class Person:
    """Class for handling personal data and test-results"""
    def __init__(self, name: str='', personal_identification_number: str=''):
        self.name = name
        self.personal_identification_number = personal_identification_number.strip()

    def validate(self) -> bool:
        #self.personnummer
        raise self.ValidationError("Random error")
        #raise Exception()
        return True

    class ValidationError(Exception):
        def __init__(self, message):
            self.message = message

    def __str__(self):
        return "Person: %s\nYear: %d" % (self.name, self.birthyear)
