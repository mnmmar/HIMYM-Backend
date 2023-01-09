# HIMYM-Backend

``` 
python manage.py migrate
python manage.py makemigrations blog_api
python manage.py sqlmigrate blog_api 0001
python manage.py createsuperuser
python manage.py runserver
 ```

Approach Taken

Since we wanted to use an external 3rd party API for our site, we didn't need to make our own. However, to meet the requirements for the project, we decided to add a blog portion to our site. That allowed us to make a database specifically tied to it and we made a model according to the information we wanted on the blog/forum section. We didn't want cast or episodes to be editted or deleted since it isn't an ongoing show and it didn't feel right so the discussion board was a perfect way to implement the requirements.

Technologies Used

* Python
* PSQL

Unsolved Problems

We don't really have unsolved problems on the backend as it was pretty straight forward to work with.

Resource Links

The main resources to make the backend was from the markdowns and lessons.
