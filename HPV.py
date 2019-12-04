#!/usr/bin/python3
from HPVDataClasses.Person import Person
import datetime 

#current date is for help with checking age and determine next step
currentdate = datetime.datetime.now()


persons = [Person(name="malin bengtsson", birthyear=1995),
           Person(name="svant svevnsson", birthyear=1999)]

if __name__ == '__main__':
    print(currentdate.strftime("%Y-%m-%d"))
    print("hello world")
    for person in persons:
        print(person)
