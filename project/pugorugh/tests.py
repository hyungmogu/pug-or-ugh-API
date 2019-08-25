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
/api/user/ (POST)
"""
class TestUserRegisterationPOSTRequest(TestCase):
    def setUp(self):
        self.client = APIClient()

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

        self.resp_register = self.client.post(
            '/api/user/',
            {
                'username':'test',
                'password':'12345'
            },
            format='json'
        )
        self.user = User.objects.get(username='test')

    def test_return_user_with_length_1(self):
        expected = 1

        result = User.objects.all().count()

        self.assertEqual(expected, result)

    def test_return_user_with_username_test(self):
        expected = 'test'

        result = User.objects.get(pk=1).username

        self.assertEqual(expected, result)

    def test_return_user_dogs_with_length_matching_dogs(self):
        expected = 2

        result = User.objects.get(pk=1).user_dog.all().count()

        self.assertEqual(expected, result)




"""
/api/user/preferences" (GET)
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
"/api/user/preferences" (PUT)
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
/api/dogs/{id}/liked (PUT)
"""
class StatusTypePUTTestCase(TestCase):
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

class TestDogLikedPUTRequest(StatusTypePUTTestCase):
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
/api/dogs/{id}/disliked (PUT)
"""

class TestDogDislikedPUTRequest(StatusTypePUTTestCase):
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
/api/dogs/{id}/undecided (PUT)
"""

class TestDogUndecidedPUTRequest(StatusTypePUTTestCase):
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
/api/dogs/{id}/liked/next/ (GET)
"""

class NextGETTestCase(TestCase):
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

        models.UserPerf.objects.create(
            user=self.user1,
            age="b,a,y,s",
            gender="m",
            size="s,m,l,xl"
        )

        models.UserPerf.objects.create(
            user=self.user2,
            age="b,a,y,s",
            gender="m",
            size="s"
        )

        self.dog1 = models.Dog.objects.create(
            name='Francesca',
            image_filename='1.jpg',
            breed='Labrador',
            age=72,
            gender='f',
            size='l'
        )

        self.dog2 = models.Dog.objects.create(
            name='Captain Jack',
            image_filename='12.jpg',
            breed='Pug Mix',
            age=14,
            gender='f',
            size='s'
        )

        self.dog3 = models.Dog.objects.create(
            name='Hank',
            image_filename='2.jpg',
            breed='French Bulldog',
            age=14,
            gender='m',
            size='s'
        )


class TestNextDogLiked(NextGETTestCase):
    def setUp(self):
        super().setUp()

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
            dog=self.dog3,
            status='d'
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog2,
            status='l'
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog3,
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

    def test_return_user_dog_object_with_name_hank_if_successful(self):
        expected = 'Hank'

        resp_login = self.client.post('/api/user/login/', {
                'username':'test',
                'password':'12345'
            }
        )

        token = resp_login.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/dog/1/liked/next/')
        result = response.data['name']

        self.assertEqual(expected, result)


"""
/api/dogs/{id}/disliked/next/ (GET)
"""
class TestNextDogDisliked(NextGETTestCase):
    def setUp(self):
        super().setUp()

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog1,
            status='d'
        )

        models.UserDog.objects.create(
            user=self.user2,
            dog=self.dog1,
            status='d'
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog3,
            status='l'
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog2,
            status='d'
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog3,
            status='d'
        )

    def test_return_status_code_401_if_not_authenticated(self):
        expected = 401

        response = self.client.get('/api/dog/1/disliked/next/')
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

        response = self.client.get('/api/dog/10/disliked/next/')
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
        response = self.client.get('/api/dog/1/disliked/next/')
        result = response.status_code

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
        response = self.client.get('/api/dog/1/disliked/next/')
        result = response.data['name']

        self.assertEqual(expected, result)


"""
/api/dogs/{id}/undecided/next/ (GET)
"""
class TestNextDogUndecided(NextGETTestCase):
    def setUp(self):
        super().setUp()

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog1,
            status=''
        )

        models.UserDog.objects.create(
            user=self.user2,
            dog=self.dog1,
            status=''
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog3,
            status='l'
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog2,
            status=''
        )

        models.UserDog.objects.create(
            user=self.user1,
            dog=self.dog3,
            status=''
        )

    def test_return_status_code_401_if_not_authenticated(self):
        expected = 401

        response = self.client.get('/api/dog/1/undecided/next/')
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

        response = self.client.get('/api/dog/10/undecided/next/')
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
        response = self.client.get('/api/dog/1/undecided/next/')
        result = response.status_code

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
        response = self.client.get('/api/dog/1/undecided/next/')
        result = response.data['name']

        self.assertEqual(expected, result)


