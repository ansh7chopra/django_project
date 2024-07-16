from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True ,primary_key=True)
    password = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    user_role = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'


class RMovie(models.Model):
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    starring = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)

    class Meta:
        db_table = 'rmovies'

    def __str__(self):
        return self.title
    


class UMovie(models.Model):
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    starring = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    release_date = models.CharField(max_length=150)

    class Meta:
        db_table = 'umovies'

    def __str__(self): 
        return self.title
    


class PVR (models.Model):
    pvr_name=models.CharField(max_length=150)
    show_1=models.CharField(max_length=150)
    show_2=models.CharField(max_length=150)
    show_3=models.CharField(max_length=150)

    class Meta:
        db_table = 'pvr_details'


class Booking(models.Model):
    movie = models.CharField(max_length=255)
    pvr = models.CharField(max_length=255)
    show_time = models.CharField(max_length=255)
    date = models.DateField()
    seats = models.TextField()

    class Meta:
        db_table = 'bookings'

    def __str__(self):
        return f'{self.movie} - {self.pvr} - {self.show_time} - {self.date} - Seats: {self.seats}'
   






# ////////////////////////////////////////////////////////////////////////////////////
# deactivate
# rmdir /s /q myenv
# python -m venv myenv
# .\myenv\Scripts\activate
# pip install django mysqlclient

# python manage.py makemigrations
# python manage.py migrate

# python manage.py runserver
