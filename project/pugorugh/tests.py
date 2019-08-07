from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from . import models

# ----------
# MODEL TESTS
# ----------

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username='hello',
            password='hello'
        )

        self.user2 = User.objects.create(
            username='world',
            password='world'
        )

    def test_return_user_model_with_query_count_of_2(self):
        expected = 2

        result = User.objects.all().count()

        self.assertEqual(expected, result)

    def test_return_hello_as_username_and_password_when_queried_with_pk_of_1(self):
        expected_username = 'hello'
        expected_password = 'hello'

        user = User.objects.get(pk=1)
        result_username = user.username
        result_password = user.password

        self.assertEqual(expected_username, result_username)
        self.assertEqual(expected_password, result_password)

    def test_return_world_as_username_and_password_when_queried_with_pk_of_2(self):
        expected_username = 'world'
        expected_password = 'world'

        user = User.objects.get(pk=2)
        result_username = user.username
        result_password = user.password

        self.assertEqual(expected_username, result_username)
        self.assertEqual(expected_password, result_password)

    def test_return_username_when_queried_object_is_type_casted(self):
        expected = 'hello'

        result = str(User.objects.get(pk=1))

        self.assertEqual(expected, result)



# -----------
# API TESTS
# -----------

"""
"/api/user/preferences"

GET Request
[x]: When retrieved, should return status code of 200 if authenticated
[x]: When retrieved, should return status code of 401 if not authenticated
[x]: When retrieved, should return object without user field
[x]: When retrieved the first time, it should return fields with empty values
    i.e.

        {
            "age": "",
            "gender": "",
            "size": ""
        }

[x]: when the following values have been added to user preferences
    {
        "user": [1], <-- referencing the account for testing
        "age": "b,y",
        "gender": "m,f",
        "size": "s,m,l"
    }

    the same except user is returned
"""
class PreferenceTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.resp_register = self.client.post(
            '/api/user/',
            {
                'username':'test',
                'password':'12345'
            },
            format='json'
        )

class TestPreferencesGETRequest(PreferenceTest):
    def test_return_status_code_200_if_authenticated(self):
        expected = 200

        # authenticate as user test
        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_preference = self.client.get('/api/user/preferences/')
        result = resp_preference.status_code

        self.assertEqual(expected, result)


    def test_return_status_code_401_if_not_authenticated(self):
        expected = 401

        resp_preference = self.client.get('/api/user/preferences/')
        result = resp_preference.status_code

        self.assertEqual(expected, result)

    def test_return_empty_user_pref_when_retrieved_first_time(self):
        expected_age = ""
        expected_gender = ""
        expected_size = ""

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_preference = self.client.get('/api/user/preferences/')
        result_age = resp_preference.data['age']
        result_gender = resp_preference.data['gender']
        result_size = resp_preference.data['size']

        self.assertEqual(expected_age, result_age)
        self.assertEqual(expected_gender, result_gender)
        self.assertEqual(expected_size, result_size)

    def test_return_without_user_field_when_retrieved(self):
        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_preference = self.client.get('/api/user/preferences/')

        with self.assertRaises(KeyError):
            resp_preference.data['user']

    def test_return_correct_values_when_non_empty_pref_is_retrieved(self):
        expected_age = "b,y"
        expected_gender = "m,f"
        expected_size = "s,m,l"

        user = User.objects.get(pk=1)
        models.UserPerf.objects.create(user=user, age='b,y', gender='m,f', size='s,m,l')

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_preference = self.client.get('/api/user/preferences/')
        result_age = resp_preference.data['age']
        result_gender = resp_preference.data['gender']
        result_size = resp_preference.data['size']

        self.assertEqual(expected_age, result_age)
        self.assertEqual(expected_gender, result_gender)
        self.assertEqual(expected_size, result_size)


"""
"/api/user/preferences"

PUT Request
[]: When successful, should return the status code of 200
[]: When accessed by non-authenticated user, should return the status code of 401
[]: When successful, should create and store the userPerf information, if userPerf of a user didn't exist
[]: When successful, database should contain the matching information, if userPref of a user already exists
[]: When a field is empty, then should return status code 400
"""
