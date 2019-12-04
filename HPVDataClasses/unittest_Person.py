import unittest
from Person import Person

class Test_unittest_Person(unittest.TestCase):
    def test_Name_Length(self):
        o = Person(name="asd")
        self.assertGreater(len(o.name), 0)

    def test_Person_validation_empty(self):
        a = Person()
        self.assertRaises(Person.ValidationError, a.validate)

    def test_validation_personal_identification_number(self):
        # An empty id is not valid
        self.assertRaises(Person.ValidationError,
                          Person(personal_identification_number = "").validate)
        # A negative negative number
        self.assertRaises(Person.ValidationError,
                          Person(personal_identification_number = "-1").validate)
        # Non valid numbers
        self.assertRaises(Person.ValidationError,
                          Person(personal_identification_number = "654654").validate)
        self.assertRaises(Person.ValidationError,
                          Person(personal_identification_number = "654654654654654").validate)
        # Valid numbers
        try:
            self.assertEqual(Person(personal_identification_number= "900101-4159").validate(), True)
        except Person.ValidationError as ex:
            self.fail("Didn't except a ValidationError here\n%s" % ex.message)

if __name__ == '__main__':
    unittest.main()
