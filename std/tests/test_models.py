from std.models import University, Student
from django.test import TestCase
from .factories import UniversityFactory, StudentFactory


class UniversityModelTest(TestCase):
    def test_university(self):
        university = UniversityFactory(name='SGSITS')
        self.assertEqual(university.name, 'SGSITS')


class StudentModelTest(TestCase):
    def test_student(self):
        # for University.instance error-create object of related foreignkey model
        university_obj = UniversityFactory(name='SGSITS')

        student = StudentFactory(first_name="monika",
                                 last_name="singh",
                                 university_name=university_obj)


        self.assertEqual(student.first_name, 'monika')
        self.assertEqual(student.last_name, 'singh')
        self.assertEqual(student.university_name, university_obj)
# def setUp(self):
    #
    #     # Set up non-modified objects used by all test methods
    #     University.objects.create(name='BITS')
    #
    # def test_name_label(self):
    #     university = University.objects.get(id=1)
    #     field_lable = university._meta.get_field('name').verbose_name
    #     self.assertEquals(field_lable, 'name')
    #
    #
    #
    # def test_name_max_length(self):
    #     university = University.objects.get(id=1)
    #     max_length = university._meta.get_field('name').max_length
    #     self.assertEquals(max_length, 50)
    #
    #
    #
    # def test_object_name(self):
    #     university = University.objects.get(id=1)
    #     expected_object_name = f'{university.name}'
    #     self.assertEquals(expected_object_name, str(university))



#     def setUp(self):
#         u = University.objects.create(
#             name='Xcellence'
#         )
#
#     def test_u(self):
#         qs = University.objects.all()
#         self.assertEqual(qs[0].name, 'Xcellence')
#
#
# class StudentModelTest(TestCase):
#     def setUp(self):
#         s = Student.objects.create(first_name='soni',
#                                    last_name='singh',
#                                    university_name= Student.university_name )
#
#     def test_s(self):
#         qs = Student.objects.all()
#         self.assertEqual(qs[0].first_name, 'soni')
#         self.assertEqual(qs[0].last_name, 'singh')
#         self.assertEqual(qs[0].university_name, Student.university_name)
#








