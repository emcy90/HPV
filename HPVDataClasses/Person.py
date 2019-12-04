import re
import datetime

class Person:
    """Class for handling personal data and test-results"""
    def __init__(self, name: str=None, birthdate: str=None, personal_identification_number: str=None):
        self.name = name
        self.birthdate = birthdate
        self.personal_identification_number = personal_identification_number
        self.check_id()
        self.check_date()

    def check_id(self):
        # Only validate id if id is given
        if self.personal_identification_number:
            # Clean up spaces
            self.personal_identification_number = self.personal_identification_number.strip()

            # Add century
            if re.match(r'[0-9]{6}-[0-9]{4}', self.personal_identification_number):
                # Match id but without century, add it
                self.personal_identification_number = '19'+self.personal_identification_number
            #if valid id parse date
            if re.match(r'[0-9]{8}-[0-9]{4}', self.personal_identification_number):
                parsed_date = datetime.datetime.strptime(self.personal_identification_number[:8], "%Y%m%d")
                self.birthdate = parsed_date.strftime('%Y-%m-%d')

    def check_date(self):
        if self.birthdate:
            # Convert string to datetime
            err = None
            try:
                self.birthdate = datetime.date.fromisoformat(self.birthdate)
            except ValueError as ex:
                if hasattr(ex, 'message'):
                    raise self.ValidationError("Birthdate %s is not valid (%s)" % (self.birthdate, ex.message))
                else:
                    raise self.ValidationError("Birthdate %s is not valid (%s)" % (self.birthdate, ex))

                
    def validate(self) -> bool:
        # Only validate id if id is given
        if self.personal_identification_number:
            if not re.match(r'[0-9]{8}-[0-9]{4}', self.personal_identification_number):
                raise self.ValidationError("Personal Identification Number: %s don't match  format ########-#### (19710321-1234)" % self.personal_identification_number)
        #raise Exception()
        if not self.birthdate: 
            raise self.ValidationError("No birthdate given")

        return True

    class ValidationError(Exception):
        def __init__(self, message):
            self.message = message

    def __str__(self):
        return "Person: %s\nYear: %d" % (self.name, self.birthyear)
