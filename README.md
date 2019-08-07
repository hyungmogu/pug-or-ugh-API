# THPWD11 - Pug or Ugh

This is the eleventh project to team tree house's Python Web Tech Degree.

## Goal
- Provide service to the pre-existing front-end site by building the database and REST API backend using Django REST Framework.

## Deliverables / Objectives

1. Run script
    - Script runs correctly.

2. Display dogs
    - The correct dogs are shown.
    - The ability to add and delete dogs from the application has been added.

3. Dog Model
    - A Dog Model is properly configured and contains the required fields:
        * name
        * image_filename
        * breed
        * age - integer for months
        * gender, “m” for male, “f” for female, “u” for unknown
        * size, "s" for small, "m" for medium, "l" for large, "xl" for extra large, "u" for unknown

4. UserDog Model
    - A UserDog Model is properly configured and contains the required fields:
        * user
        * dog
        * status, “l” for liked, “d” for disliked

5. UserPref Model
    - A UserPref Model is properly configured and contains the required fields:
        * user
        * age, “b” for baby, “y” for young, “a” for adult, “s” for senior
        * gender, “m” for male, “f” for female
        * size, “s” for small, “m” for medium, “l” for large, “xl” for extra large

6. Serializers
    - Serializers for the Dog and UserPref Models are in place and reveals all fields except user from the UserPref Model.

7. Routes
    - The required routes are in place and function correctly:
        * `/api/dog/<pk>/liked/next/` (For gettting the next liked/disliked/undecided dog)
        * `/api/dog/<pk>/disliked/next/`
        * `/api/dog/<pk>/disliked/next/`
        * `To change the dog’s status:`
        * `/api/dog/<pk>/liked/`
        * `/api/dog/<pk>/disliked/`
        * `/api/dog/<pk>/undecided/`
        * `/api/user/preferences/` (For changing or set user preference)

8. Authentication
    - Uses Token-Based Authentication

9. Unit Test the App
    - Test coverage above 75%.

10. Python Code Style
    - The code is clean, readable, and well organized. It complies with most common PEP 8 standards of style.


## Steps to pre-populating data
1. Once in `project` folder of virtual environment (`step 3` under Steps to Running/Exiting the Program), navigate to `pugorugh/script` folder
2. Execute the pre-populating program by typing `python data_import.py`

## Steps to Running/Exiting the Program
1. Install pipenv by typing `pip install pipenv` or `pip3 install pipenv` for python3 users
2. In `project` folder, install dependencies by typing `pipenv install`
3. In `project` folder, enter virtual environment by typing `pipenv shell`
4. In `project` folder, run `python manage.py makemigrations menu`
5. In `project` folder, run `python manage.py migrate`
6. In `project` folder, run app by typing `python manage.py runserver`
7. View the project by opening a browser like Chrome and entering the provided url (i.e. `http://127.0.0.1:8000/`)
8. When done, exit by pressing `Ctrl`+`C` and virtual environment by typing `exit`