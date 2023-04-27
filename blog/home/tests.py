from rest_framework.test import APITestCase
from rest_framework import status
class MyApiTestCase(APITestCase):
    
    def test_my_endpoint(self):
        response = self.client.get("http://127.0.0.1:8000/blog/Public/")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
