import unittest
from datetime import date
from Person import Person

class Test_unittest_Person(unittest.TestCase):
    def test_Name_Length(self):
        o = Person(name="asd")
        self.assertGreater(len(o.name), 0)

    def test_Person_validation_empty(self):
        a = Person()
        self.assertRaises(Person.ValidationError, a.validate)

    def test_validation_personal_identification_number_invalid(self):
        # An empty id is not valid
        self.assertRaises(Person.ValidationError,
                          Person(personal_identification_number="").validate)
        # A negative negative number
        self.assertRaises(Person.ValidationError,
                          Person(personal_identification_number="-1").validate)
        # Non valid numbers
        self.assertRaises(Person.ValidationError,
                          Person(personal_identification_number="654654").validate)
        self.assertRaises(Person.ValidationError,
                          Person(personal_identification_number="654654654654654").validate)

    def test_validation_personal_identification_number_valid(self):
        # Valid numbers
        try:
            self.assertEqual(Person(personal_identification_number="19910101-4159").validate(), True)
            self.assertEqual(Person(personal_identification_number="900101-4159").validate(), True)
        except Person.ValidationError as ex:
            self.fail("Didn't except a ValidationError here\n%s" % ex.message)

    def test_birthyear_valid(self):
        try:
            self.assertEqual(Person(birthdate='2003-12-04').validate(), True)
            self.assertEqual(Person(birthdate='1910-11-30').validate(), True)
            self.assertEqual(Person(birthdate='1980-12-04').validate(), True)
            self.assertEqual(Person(birthdate='1991-06-30').validate(), True)
        except Person.ValidationError as ex:
            self.fail("Didn't except a ValidationError here\n%s" % ex.message)

    def test_birthyear_invalid(self):
        try:
            Person(birthdate='1991-06-31').validate()
        except Person.ValidationError as ex:
            pass  # We except to get Validation error here, 31 is not a valid day for june
        except Exception as ex:
            self.fail("Didn't except exception (%s) here." % ex)
        try:
            Person(birthdate='19911131').validate()
        except Person.ValidationError as ex:
            pass  # We except to get Validation error here, no dashes
        except Exception as ex:
            self.fail("Didn't except exception (%s) here." % ex)



if __name__ == '__main__':
    unittest.main()
