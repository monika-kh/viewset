from django.urls import reverse

from std.models import University, Student
from django.test import TestCase

from rest_framework.test import APIClient, APITestCase


class University_Student_Test(APITestCase):
    def test_student(self):

        data = {"name": "data"}                       # university model
        res = self.client.post('/university/universities/',data, format="json")
        self.assertEqual(res.status_code, 201)
        res_g = self.client.get('/university/universities/1/',data, format="json")
        self.assertEqual(res_g.status_code, 200)

        # student model
        id_id =  res.data.get('id')                   # id of university
        data = {
            "first_name":"dee",
            "last_name":'dets',
            "university_name":id_id
        }
        res1 = self.client.post('/university/students/',data, format="json")
        self.assertEqual(res1.status_code, 201)

        res1 = self.client.get('/university/students/1/', format="json")
        self.assertEqual(res1.status_code, 200)



