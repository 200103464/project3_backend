from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
import datetime
from  django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
from django_countries.fields import CountryField
from django.utils.translation import gettext as _
YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]



# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    date_of_birth = models.DateField(verbose_name=("Date of birth"), blank=True, null=True)
    email = models.EmailField(blank=True, unique=True)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=10)

    def str(self):
        return self.username
class Movie(models.Model):
    Боевик= 'Боевик'
    Комедия = 'Комедия'
    Приключения= 'Приключения'
    Мультфильм= 'Мультфильм'
    Ужасы= 'Ужасы'
    Спорт= 'Спорт'
    Фантастика= 'Фантастика'
    Фэнтези= 'Фэнтези'
    Триллер='Триллер'
    Детектив= 'Детектив'
    История= 'История'
    ДокументальныйФильм= 'Документальный фильм'
    Семейный= 'Семейный'
    genre_in_choices =[
        (Боевик, 'Боевик'),
        (Комедия,'Комедия'),
        (Приключения,'Приключения'),
        (Мультфильм,'Мультфильм'),
        (Ужасы,'Ужасы'),
        (Спорт,'Спорт'),
        (Фантастика,'Фантастика'),
        (Фэнтези,'Фэнтези'),
        (Триллер,'Триллер'),
        (Детектив,'Детектив'),
        (История,'История'),
        (ДокументальныйФильм,'Документальный фильм'),
        (Семейный, 'Семейный'),

    ]
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='movie')
    description= models.TextField()
    year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    country = CountryField(multiple=True)
    film_director= models.TextField()
    actors= models.TextField()
    genre = MultiSelectField(
        max_length=30,
        choices=genre_in_choices,
        default=Комедия,
    )
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
