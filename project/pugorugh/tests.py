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

    [x]: When all are retrieved, it should return the count of 2
    [x]: if a dog with pk=1 is retrieved, it should have name of Francesca
    [x]: if a dog with pk=1 is retrieved, it should have image_filename of "1.jpg"
    [x]: if a dog with pk=1 is retrieved, it should have breed of Labrador
    [x]: if a dog with pk=1 is retrieved it should have age of 72
    [x]: if a dog with pk=1 is retrieved it should have gender of f
    [x]: if a dog with pk=1 is retrieved it should have size of l

    [x]: if a dog with pk=2 is retrieved, it should have name of Hank
    [x]: if a dog with pk=2 is retrieved, it should have image_filename of "2.jpg"
    [x]: if a dog with pk=2 is retrieved, it should have breed of French Bulldog
    [x]: if a dog with pk=2 is retrieved it should have age of 14
    [x]: if a dog with pk=2 is retrieved it should have gender of m
    [x]: if a dog with pk=2 is retrieved it should have size of s
"""

class DogTestCase(TestCase):
    def setUp(self):
        self.dog1 = models.Dog.objects.create(
            name="Francesca",
            image_filename="1.jpg",
            breed="Labrador",
            age=72,
            gender="f",
            size="l"
        )

        self.dog2 = models.Dog.objects.create(
            name="Hank",
            image_filename="2.jpg",
            breed="French Bulldog",
            age=14,
            gender="m",
            size="s"
        )

    def test_return_count_of_2_when_all_retrived(self):
        expected = 2

        result = models.Dog.objects.all().count()

        self.assertEqual(expected, result)


    def test_return_dog_pk_1_with_name_francesca(self):
        expected = 'Francesca'

        dog = models.Dog.objects.get(pk=1)
        result = dog.name

        self.assertEqual(expected, result)

    def test_return_dog_pk_1_with_image_file_1_jpg(self):
        expected = '1.jpg'

        dog = models.Dog.objects.get(pk=1)
        result = dog.image_filename

    def test_return_dog_pk_1_with_breed_labrador(self):
        expected = 'Labrador'

        dog = models.Dog.objects.get(pk=1)
        result = dog.breed

        self.assertEqual(expected, result)

    def test_return_dog_pk_1_with_age_72(self):
        expected = 72

        dog = models.Dog.objects.get(pk=1)
        result = dog.age

        self.assertEqual(expected, result)

    def test_return_dog_pk_1_with_gender_f(self):
        expected = 'f'

        dog = models.Dog.objects.get(pk=1)
        result = dog.gender

        self.assertEqual(expected, result)

    def test_return_dog_pk_1_with_size_l(self):
        expected = 'l'

        dog = models.Dog.objects.get(pk=1)
        result = dog.size

        self.assertEqual(expected, result)

    def test_return_dog_pk_2_with_name_hank(self):
        expected = 'Hank'

        dog = models.Dog.objects.get(pk=2)
        result = dog.name

        self.assertEqual(expected, result)

    def test_return_dog_pk_2_with_image_file_2_jpg(self):
        expected = '2.jpg'

        dog = models.Dog.objects.get(pk=2)
        result = dog.image_filename

        self.assertEqual(expected, result)

    def test_return_dog_pk_2_with_breed_french_bulldog(self):
        expected = 'French Bulldog'

        dog = models.Dog.objects.get(pk=2)
        result = dog.breed

        self.assertEqual(expected, result)

    def test_return_dog_pk_2_with_age_14(self):
        expected = 14

        dog = models.Dog.objects.get(pk=2)
        result = dog.age

        self.assertEqual(expected, result)

    def test_return_dog_pk_2_with_gender_m(self):
        expected = 'm'

        dog = models.Dog.objects.get(pk=2)
        result = dog.gender

        self.assertEqual(expected, result)

    def test_return_dog_pk_2_with_size_s(self):
        expected = 's'

        dog = models.Dog.objects.get(pk=2)
        result = dog.size

        self.assertEqual(expected, result)

"""
UserDog Model

Given that the following sets of data are added to database

    dog1 = {
        "name": "Francesca",
        "image_filename": "1.jpg",
        "breed": "Labrador",
        "age": 72,
        "gender": "f",
        "size": "l"
    }

    dog2 = {
        "name": "Hank",
        "image_filename": "2.jpg",
        "breed": "French Bulldog",
        "age": 14,
        "gender": "m",
        "size": "s"
    }

    user1 = {
        username='hello',
        password='hello'
    }

    user2 = {
        username='world',
        password='world'
    }

    user_dog1 = {
        user: user1,
        dog: dog1,
        status: 'l'
    }

    user_dog2 = {
        user: user1,
        dog: dog2,
        status 'd'
    }

    user_dog3 = {
        user: user2,
        dog: dog1,
        status: 'l'
    }


[x]: When all are retrieved, it should return the count of 3
[x]: if user_dog with pk=1 is retrieved, it should return user with username hello
[x]: if user_dog with pk=1 is retrieved, it should return dog with name Francesco
[x]: if user_dog with pk=1 is retrieved, it should return status with l as its value

[x]: if user_dog with pk=2 is retrieved, it should return user with username of hello
[x]: if user_dog with pk=2 is retrieved, it should return dog with name of Hank
[x]: if user_dog with pk=2 is retrieved, it should return status with d as its value

[x]: if user_dog with pk=3 is retrieved, it should return user with username of world
[x]: if user_dog with pk=3 is retrieved, it should return dog with name Francesco
[x]: if user_dog with pk=3 is retrieved, it should return status with l as its value

"""



class DogTestCase(TestCase):
    def setUp(self):
        self.dog1 = models.Dog.objects.create(
            name="Francesca",
            image_filename="1.jpg",
            breed="Labrador",
            age=72,
            gender="f",
            size="l"
        )

        self.dog2 = models.Dog.objects.create(
            name="Hank",
            image_filename="2.jpg",
            breed="French Bulldog",
            age=14,
            gender="m",
            size="s"
        )

        self.user1 = User.objects.create(
            username='hello',
            password='hello'
        )

        self.user2 = User.objects.create(
            username='world',
            password='world'
        )


        self.user_dog1 = models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog1,
            status= 'l'
        )

        self.user_dog2 = models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog2,
            status='d'
        )

        self.user_dog3 = models.UserDog.objects.create(
            user=self.user2,
            dog=self.dog1,
            status='l'
        )

    def test_return_count_of_3_when_all_user_dog_is_retrived(self):
        expected = 3

        result = models.UserDog.objects.all().count()

        self.assertEqual(expected, result)

    def test_return_user_dog_pk_1_with_user_username_valued_hello(self):
        expected = 'hello'

        user_dog = models.UserDog.objects.get(pk=1)
        result = user_dog.user.username

        self.assertEqual(expected, result)

    def test_return_user_dog_pk_1_with_dog_name_valued_francesca(self):
        expected = 'Francesca'

        user_dog = models.UserDog.objects.get(pk=1)
        result = user_dog.dog.name

        self.assertEqual(expected, result)

    def test_return_user_dog_pk_1_with_status_l_as_its_value(self):
        expected = 'l'

        user_dog = models.UserDog.objects.get(pk=1)
        result = user_dog.status

        self.assertEqual(expected, result)

    def test_return_user_dog_pk_2_with_user_username_valued_hello(self):
        expected = 'hello'

        user_dog = models.UserDog.objects.get(pk=2)
        result = user_dog.user.username

        self.assertEqual(expected, result)

    def test_return_user_dog_pk_2_with_dog_name_valued_hank(self):
        expected = 'Hank'

        user_dog = models.UserDog.objects.get(pk=2)
        result = user_dog.dog.name

        self.assertEqual(expected, result)

    def test_return_user_dog_pk_2_with_status_d_as_its_value(self):
        expected = 'd'

        user_dog = models.UserDog.objects.get(pk=2)
        result = user_dog.status

        self.assertEqual(expected, result)

    def test_return_user_dog_pk_3_with_user_username_valued_world(self):
        expected = 'world'

        user_dog = models.UserDog.objects.get(pk=3)
        result = user_dog.user.username

        self.assertEqual(expected, result)

    def test_return_user_dog_pk_3_with_dog_name_valued_francesca(self):
        expected = 'Francesca'

        user_dog = models.UserDog.objects.get(pk=3)
        result = user_dog.dog.name

        self.assertEqual(expected, result)

    def test_return_user_dog_pk_3_with_status_d_as_its_value(self):
        expected = 'l'

        user_dog = models.UserDog.objects.get(pk=3)
        result = user_dog.status

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
[x]: When successful, should return the status code of 200
[x]: When accessed by non-authenticated user, should return status code of 401
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


"""
/api/dogs/{id}/liked

PUT REQUEST
Given the following data

dog = {
        "name": "Francesca",
        "image_filename": "1.jpg",
        "breed": "Labrador",
        "age": 72,
        "gender": "f",
        "size": "l"
    }

user1 = {
    username='test',
    password='12345'
}


[x]: When successful should return the status code of 200
[x]: When accessed by non-authenticated user, it should return status code 401
[x]: When successful, should create and store information, if the information didn't exist
[x]: When successful, database should contain the matching information, if the entry of id already exists
[x]: When field is empty, should return status code 400
"""

class TestDogLikedPUTRequest(TestCase):

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
        self.user = User.objects.get(username='test')
        self.dog = models.Dog.objects.create(
            name="Francesca",
            image_filename="1.jpg",
            breed="Labrador",
            age=72,
            gender="f",
            size="l"
        )

    def test_return_status_code_200_if_okay(self):
        expected = 200

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_like = self.client.put('/api/dog/1/liked/')

        result = resp_like.status_code

        self.assertEqual(expected, result)

    def test_return_status_401_if_accessed_by_unauthenticated_user(self):
        expected = 401

        resp_liked = self.client.put('/api/dog/1/liked/')

        result = resp_liked.status_code

        self.assertEqual(expected, result)

    def test_return_user_dog_as_new_entry_in_the_table_if_it_did_not_exist(self):
        expected_db_size = 1
        expected_status = "l"

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.put('/api/dog/1/liked/')

        user_dog = models.UserDog.objects.get(pk=1)

        result_db_size = models.UserDog.objects.all().count()

        result_status = user_dog.status

        self.assertEqual(expected_db_size, result_db_size)
        self.assertEqual(expected_status, result_status)

    def test_return_modified_user_perf_if_already_exists(self):
        expected_db_size = 1
        expected_status = 'l'

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        models.UserDog.objects.create(
            user=self.user,
            dog=self.dog,
            status='d'
        )

        self.client.put('/api/dog/1/liked/')

        user_dog = models.UserDog.objects.get(pk=1)

        result_db_size = models.UserDog.objects.all().count()

        result_status =  user_dog.status

        self.assertEqual(expected_db_size, result_db_size)
        self.assertEqual(expected_status, result_status)



"""
/api/dogs/{id}/disliked

PUT REQUEST
Given the following data

dog = {
        "name": "Francesca",
        "image_filename": "1.jpg",
        "breed": "Labrador",
        "age": 72,
        "gender": "f",
        "size": "l"
    }

user1 = {
    username='test',
    password='12345'
}


[x]: When successful should return the status code of 200
[x]: When accessed by non-authenticated user, it should return status code 401
[x]: When successful, should create and store information, if the information didn't exist
[x]: When successful, database should contain the matching information, if the entry of id already exists
[x]: When field is empty, should return status code 400
"""

class TestDogDislikedPUTRequest(TestCase):

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
        self.user = User.objects.get(username='test')
        self.dog = models.Dog.objects.create(
            name="Francesca",
            image_filename="1.jpg",
            breed="Labrador",
            age=72,
            gender="f",
            size="l"
        )

    def test_return_status_code_200_if_okay(self):
        expected = 200

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_like = self.client.put('/api/dog/1/disliked/')

        result = resp_like.status_code

        self.assertEqual(expected, result)

    def test_return_status_401_if_accessed_by_unauthenticated_user(self):
        expected = 401

        resp_liked = self.client.put('/api/dog/1/disliked/')

        result = resp_liked.status_code

        self.assertEqual(expected, result)

    def test_return_user_dog_as_new_entry_in_the_table_if_it_did_not_exist(self):
        expected_db_size = 1
        expected_status = 'd'

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.put('/api/dog/1/disliked/')

        user_dog = models.UserDog.objects.get(pk=1)

        result_db_size = models.UserDog.objects.all().count()

        result_status = user_dog.status

        self.assertEqual(expected_db_size, result_db_size)
        self.assertEqual(expected_status, result_status)

    def test_return_modified_user_perf_if_already_exists(self):
        expected_db_size = 1
        expected_status = 'd'

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        models.UserDog.objects.create(
            user=self.user,
            dog=self.dog,
            status='l'
        )

        self.client.put('/api/dog/1/disliked/')

        user_dog = models.UserDog.objects.get(pk=1)

        result_db_size = models.UserDog.objects.all().count()

        result_status =  user_dog.status

        self.assertEqual(expected_db_size, result_db_size)
        self.assertEqual(expected_status, result_status)


"""
/api/dogs/{id}/undecided

PUT REQUEST
Given the following data

dog = {
        "name": "Francesca",
        "image_filename": "1.jpg",
        "breed": "Labrador",
        "age": 72,
        "gender": "f",
        "size": "l"
    }

user1 = {
    username='test',
    password='12345'
}


[x]: When successful should return the status code of 200
[x]: When accessed by non-authenticated user, it should return status code 401
[x]: When successful, should create and store information, if the information didn't exist
[x]: When successful, database should contain the matching information, if the entry of id already exists
[x]: When field is empty, should return status code 400
"""

class TestDogUndecidedPUTRequest(TestCase):

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
        self.user = User.objects.get(username='test')
        self.dog = models.Dog.objects.create(
            name="Francesca",
            image_filename="1.jpg",
            breed="Labrador",
            age=72,
            gender="f",
            size="l"
        )

    def test_return_status_code_200_if_okay(self):
        expected = 200

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )
        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp_undecided = self.client.put('/api/dog/1/undecided/')

        result = resp_undecided.status_code

        self.assertEqual(expected, result)

    def test_return_status_401_if_accessed_by_unauthenticated_user(self):
        expected = 401

        resp_undecided = self.client.put('/api/dog/1/undecided/')

        result = resp_undecided.status_code

        self.assertEqual(expected, result)

    def test_return_user_dog_as_new_entry_in_the_table_if_it_did_not_exist(self):
        expected_db_size = 1
        expected_status = ''

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.client.put('/api/dog/1/undecided/')

        user_dog = models.UserDog.objects.get(pk=1)

        result_db_size = models.UserDog.objects.all().count()

        result_status = user_dog.status

        self.assertEqual(expected_db_size, result_db_size)
        self.assertEqual(expected_status, result_status)

    def test_return_modified_user_perf_if_already_exists(self):
        expected_db_size = 1
        expected_status = ''

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        models.UserDog.objects.create(
            user=self.user,
            dog=self.dog,
            status='l'
        )

        self.client.put('/api/dog/1/undecided/')

        user_dog = models.UserDog.objects.get(pk=1)

        result_db_size = models.UserDog.objects.all().count()

        result_status =  user_dog.status

        self.assertEqual(expected_db_size, result_db_size)
        self.assertEqual(expected_status, result_status)



"""
/api/dogs/{id}/liked/next/

GET REQUEST
Given an example endpoint '/api/dog/1/liked/next' with the following UserDog data

[
    {
        "id": 1,
        "user":1,
        "dog": 1,
        "status": "l"
    },
    {
        "id": 2,
        "user": 2,
        "dog": 1,
        "status": "l"
    },
    {
        "id": 3,
        "user": 1,
        "dog": 2,
        "status": "d"
    },
    {
        "id": 4,
        "user": 1,
        "dog": 2,
        "status": "l"
    }

]

user1 = {
    username='test',
    password='12345'
}

user2 = {
    username='world',
    password='world'
}


dog1 = {
    "name": "Francesca",
    "image_filename": "1.jpg",
    "breed": "Labrador",
    "age": 72,
    "gender": "f",
    "size": "l"
}

dog2 = {
    "name": "Hank",
    "image_filename": "2.jpg",
    "breed": "French Bulldog",
    "age": 14,
    "gender": "m",
    "size": "s"
}

[x]: When not authenticated, return status code of 401
[x]: When empty, return status code of 404
[x]: When out of bound, return status code of 404
[x]: when successful, return status code 200
[x]: When successful, return item with id of 4
[x]: When successful, return item with username of 'test'
[x]: When successful, return item with dog name of 'Hank'
"""

class TestNextDogLikedGETRequest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.client.post(
            '/api/user/',
            {
                'username':'test',
                'password':'12345'
            },
            format='json'
        )

        self.client.post(
            '/api/user/',
            {
                'username':'world',
                'password':'world'
            },
            format='json'
        )

        self.user1 = models.User.objects.get(username='test')
        self.user2 = models.User.objects.get(username='world')

        self.dog1 = models.Dog.objects.create(
            name='Francesca',
            image_filename='1.jpg',
            breed='Labrador',
            age=72,
            gender='f',
            size='l'
        )

        self.dog2 = models.Dog.objects.create(
            name='Hank',
            image_filename='2.jpg',
            breed='French Bulldog',
            age=14,
            gender='m',
            size='s'
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog1,
            status='l'
        )

        models.UserDog.objects.create(
            user=self.user2,
            dog=self.dog1,
            status='l'
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog2,
            status='d'
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog2,
            status='l'
        )

    def test_return_status_code_401_if_not_authenticated(self):
        expected = 401

        response = self.client.get('/api/dog/1/liked/next/')
        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_status_code_404_if_empty_or_out_of_bound(self):
        expected = 404

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.get('/api/dog/10/liked/next/')
        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_status_code_200_if_successful(self):
        expected = 200

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/dog/1/liked/next/')
        result = response.status_code

        self.assertEqual(expected, result)

    def test_return_user_dog_object_with_id_4_if_successful(self):
        expected = 4

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/dog/1/liked/next/')
        result = response.data['id']

        self.assertEqual(expected, result)


    def test_return_user_dog_object_with_user_name_test_if_successful(self):
        expected = 'test'

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/dog/1/liked/next/')
        user = models.User.objects.get(pk=response.data['user'])
        result = user.username

        self.assertEqual(expected, result)

    def test_return_user_dog_object_with_dog_name_hank_if_successful(self):
        expected = 'Hank'

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/dog/1/liked/next/')
        dog = models.Dog.objects.get(pk=response.data['dog'])
        result = dog.name

        self.assertEqual(expected, result)

