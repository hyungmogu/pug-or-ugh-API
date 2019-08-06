from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


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
[]: When retrieved, should return status code of 200 if authenticated
[]: When retrieved, should return status code of 403 if not authenticated
[]: When retrieved, should return object without user field
[]: When retrieved the first time, it should return fields with empty values
    i.e.

        {
            "age": "",
            "gender": "",
            "size": ""
        }

[]: when the following values have been added to user preferences
    {
        "user": [1], <-- referencing the account for testing
        "age": "b,y",
        "gender": "m,f",
        "size": "s,m,l"
    }

    the same except user is returned
"""
