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


"""
UserPerf Model
    given that the following user perfs are added to database, one for each user

    {
        "user": USER_1 <-- has username test1,
        "age": "b",
        "gender": "m",
        size: "s"
    }

        {
        "user": USER_2 <-- has username test2,
        "age": "a",
        "gender": "m",
        size: "l"
    }

    [x]: return count of 2 on user_perf models
    [x]: if user perf of pk=1 is retrieved, it should have username of test1
    [x]: if user perf of pk=1 is retrieved, it should have age of b
    [x]: if user perf of pk=1 is retrieved, it should have gender of m
    [x]: if user perf of pk=1 is retrieved it should have size of s

    [x]: if user perf of pk=2 is retrieved, it should have username of test2
    [x]: if user perf of pk=2 is retrieved, it should have age of a
    [x]: if user perf of pk=2 is retrieved, it should have gender of m
    [x]: if user perf of pk=2 is retrieved, it shuld have size of l
"""
class UserPerfTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username="test1",
            password="12345"
        )

        self.user2 = User.objects.create(
            username="test2",
            password="12345"
        )

        self.userPerf1 = models.UserPerf.objects.create(
            user=self.user1,
            age="b",
            gender="m",
            size="s"
        )

        self.userPerf2 = models.UserPerf.objects.create(
            user=self.user2,
            age="a",
            gender="m",
            size="l"
        )

    def test_return_count_of_2_when_all_retrived(self):
        expected = 2

        result = models.UserPerf.objects.all().count()

        self.assertEqual(expected, result)

    def test_return_user_perf_pk_1_with_username_of_test1(self):
        expected = 'test1'

        user_perf = models.UserPerf.objects.get(pk=1)
        result = user_perf.user.username

        self.assertEqual(expected, result)

    def test_return_user_perf_pk_1_with_age_b(self):
        expected = 'b'

        user_perf = models.UserPerf.objects.get(pk=1)
        result = user_perf.age

        self.assertEqual(expected, result)


    def test_return_user_perf_pk_1_with_gender_m(self):
        expected = 'm'

        user_perf = models.UserPerf.objects.get(pk=1)
        result = user_perf.gender

        self.assertEqual(expected, result)


    def test_return_user_perf_pk_1_with_size_s(self):
        expected = 's'

        user_perf = models.UserPerf.objects.get(pk=1)
        result = user_perf.size

        self.assertEqual(expected, result)

    def test_return_user_perf_pk_2_with_username_of_test2(self):
        expected = 'test2'

        user_perf = models.UserPerf.objects.get(pk=2)
        result = user_perf.user.username

        self.assertEqual(expected, result)

    def test_return_user_perf_pk_2_with_age_a(self):
        expected = 'a'

        user_perf = models.UserPerf.objects.get(pk=2)
        result = user_perf.age

        self.assertEqual(expected, result)


    def test_return_user_perf_pk_2_with_gender_m(self):
        expected = 'm'

        user_perf = models.UserPerf.objects.get(pk=2)
        result = user_perf.gender

        self.assertEqual(expected, result)


    def test_return_user_perf_pk_2_with_size_l(self):
        expected = 'l'

        user_perf = models.UserPerf.objects.get(pk=2)
        result = user_perf.size

        self.assertEqual(expected, result)



"""
Dog Model
    given that the following dogs are added to database

    {
        "name": "Francesca",
        "image_filename": "1.jpg",
        "breed": "Labrador",
        "age": 72,
        "gender": "f",
        "size": "l"
    },
    {
        "name": "Hank",
        "image_filename": "2.jpg",
        "breed": "French Bulldog",
        "age": 14,
        "gender": "m",
        "size": "s"
    }

    []: When all are retrieved, it should return the count of 2
    []: if a dog with pk=1 is retrieved, it should have name of Francesca
    []: if a dog with pk=1 is retrieved, it should have image_filename of "1.jpg"
    []: if a dog with pk=1 is retrieved, it should have breed of Labrador
    []: if a dog with pk=1 is retrieved it should have age of 72
    []: if a dog with pk=1 is retrieved it should have gender of f
    []: if a dog with pk=1 is retrieved it should have size of l

    []: if a dog with pk=1 is retrieved, it should have name of Hank
    []: if a dog with pk=1 is retrieved, it should have image_filename of "2.jpg"
    []: if a dog with pk=1 is retrieved, it should have breed of French Bulldog
    []: if a dog with pk=1 is retrieved it should have age of 14
    []: if a dog with pk=1 is retrieved it should have gender of m
    []: if a dog with pk=1 is retrieved it should have size of s
"""

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
[x]: When successful, should return the status code of 200
[x]: When accessed by non-authenticated user, should return the status code of 401
[x]: When successful, should create and store the userPerf information, if userPerf of a user didn't exist
[x]: When successful, database should contain the matching information, if userPref of a user already exists
[x]: When a field is empty, then should return status code 400
"""

class TestPreferencesPUTRequest(PreferenceTest):

    def test_return_status_code_200_if_okay(self):
        expected = 200

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_preference = self.client.put('/api/user/preferences/', {
            "age": "b,y",
            "gender": "m,f",
            "size": "s,m,l"
        })

        result = resp_preference.status_code

        self.assertEqual(expected, result)

    def test_return_status_401_if_accessed_by_unauthenticated_user(self):
        expected = 401

        resp_preference = self.client.put('/api/user/preferences/', {
            "age": "b,y",
            "gender": "m,f",
            "size": "s,m,l"
        })

        result = resp_preference.status_code

        self.assertEqual(expected, result)

    def test_return_status_code_400_if_age_is_empty(self):
        expected = 400

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_preference1 = self.client.put('/api/user/preferences/', {
            "age": "",
            "gender": "m,f",
            "size": "s,m,l"
        })

        resp_preference2 = self.client.put('/api/user/preferences/', {
            "gender": "m,f",
            "size": "s,m,l"
        })

        result1 = resp_preference1.status_code
        result2 = resp_preference2.status_code

        self.assertEqual(expected, result1)
        self.assertEqual(expected, result2)

    def test_return_status_code_400_if_gender_is_empty(self):
        expected = 400

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_preference1 = self.client.put('/api/user/preferences/', {
            "age": "b,y",
            "gender": "",
            "size": "s,m,l"
        })

        resp_preference2 = self.client.put('/api/user/preferences/', {
            "age": "b,y",
            "size": "s,m,l"
        })

        result1 = resp_preference1.status_code
        result2 = resp_preference2.status_code

        self.assertEqual(expected, result1)
        self.assertEqual(expected, result2)


    def test_return_status_code_400_if_size_is_empty(self):
        expected = 400

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_preference1 = self.client.put('/api/user/preferences/', {
            "age": "b,y",
            "gender": "m,f",
            "size": ""
        })

        resp_preference2 = self.client.put('/api/user/preferences/', {
            "age": "b,y",
            "gender": "m,f"
        })

        result1 = resp_preference1.status_code
        result2 = resp_preference2.status_code

        self.assertEqual(expected, result1)
        self.assertEqual(expected, result2)

    def test_return_user_perf_as_new_entry_in_table_with_info_if_it_did_not_exist(self):
        expected_db_size = 1
        expected_age = "b,y"
        expected_gender = "m,f"
        expected_size = "s,m,l"

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.put('/api/user/preferences/', {
            "age": "b,y",
            "gender": "m,f",
            "size": "s,m,l"
        })

        user_perf = models.UserPerf.objects.get(pk=1)

        result_db_size = models.UserPerf.objects.all().count()

        result_age =  user_perf.age
        result_gender = user_perf.gender
        result_size = user_perf.size

        self.assertEqual(expected_db_size, result_db_size)
        self.assertEqual(expected_age, result_age)
        self.assertEqual(expected_gender, result_gender)
        self.assertEqual(expected_size, result_size)

    def test_return_modified_user_perf_if_already_exists(self):
        expected_db_size = 1
        expected_age = "b,y"
        expected_gender = "m,f"
        expected_size = "s,m,l"

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        user = User.objects.get(pk=1)
        userperf = models.UserPerf.objects.create(
            user=user,
            age="b,a",
            gender="m",
            size="s"
        )

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.put('/api/user/preferences/', {
            "age": "b,y",
            "gender": "m,f",
            "size": "s,m,l"
        })

        user_perf = models.UserPerf.objects.get(pk=1)

        result_db_size = models.UserPerf.objects.all().count()

        result_age =  user_perf.age
        result_gender = user_perf.gender
        result_size = user_perf.size

        self.assertEqual(expected_db_size, result_db_size)
        self.assertEqual(expected_age, result_age)
        self.assertEqual(expected_gender, result_gender)
        self.assertEqual(expected_size, result_size)
