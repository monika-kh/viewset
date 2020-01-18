import factory
import factory.fuzzy

from faker import Factory

from std.models import University, Student


class UniversityFactory(factory.Factory):
    class Meta:
        model = University

    name = factory.Sequence(lambda n: 'name_{}'.format(n))
    # factory.Sequence(lambda n: 'name_{}'.format(n))- used for charfield in model


class StudentFactory(factory.Factory):
    class Meta:
        model = Student


    first_name = factory.Sequence(lambda n: 'first_name_{}'.format(n))
    last_name = factory.Sequence(lambda n: 'last_name_{}'.format(n))
    university_name = factory.SubFactory(UniversityFactory)
    # subfactory used for Foreignkey





