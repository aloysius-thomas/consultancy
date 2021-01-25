from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from accounts.models import User

STATUS = (
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('pending', 'Pending'),
)


class Company(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=64)
    pin_code = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    company_type = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    CANDIDATE_TYPE = (
        ('student', 'Student'),
        ('working', 'Working'),
    )
    added_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CANDIDATE_TYPE)
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(99), MinValueValidator(18)])
    qualification = models.CharField(max_length=255)
    skills = models.TextField()
    job_position = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    pin_code = models.IntegerField()
    email = models.EmailField()
    resume = models.FileField(upload_to='candidate/resume/')

    def __str__(self):
        return f'Candidate {self.full_name}'


class Vacancy(models.Model):
    posted_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, blank=True, null=True)
    post_name = models.CharField(max_length=256)
    number_of_post = models.IntegerField()
    skills = models.TextField()
    salary_package = models.CharField(max_length=256)
    job_description = models.CharField(max_length=512)
    experience = models.CharField(max_length=256)
    date_of_interview = models.DateField()
    venue = models.CharField(max_length=256)
    time = models.TimeField()

    def __str__(self):
        return self.post_name


class Event(models.Model):
    FOOD_TYPE = (
        ('veg', 'Vegetarian'),
        ('non-veg', 'Non-Vegetarian'),
    )
    TYPE_OF_VENUE = (
        ('ac', 'AC'),
        ('non-ac', 'Non-AC'),
    )
    TYPE_OF_EVENT = (
        ('product_launch', 'Product Launch'),
        ('business_meeting', 'Business Meeting'),
        ('live_show', 'Live Show'),
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday')
    )
    booked_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    event_type = models.CharField(choices=TYPE_OF_EVENT, max_length=24)
    date_of_event = models.DateField()
    type_of_venue = models.CharField(choices=TYPE_OF_VENUE, max_length=12)
    number_of_person = models.IntegerField()
    food_items = models.CharField(choices=FOOD_TYPE, max_length=12)
    light_and_sound = models.TextField()
    number_of_days = models.IntegerField(blank=True, null=True)
    number_of_security = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    transportation = models.IntegerField(blank=True, null=True)
    photography = models.IntegerField(blank=True, null=True)
    beautician = models.IntegerField(blank=True, null=True)
    status = models.CharField(choices=STATUS, default='pending', max_length=16)

    def __str__(self):
        return f'{self.get_event_type_display()}  booked by {str(self.booked_by)}'


class Construction(models.Model):
    SERVICE_TYPE = (
        ('construction', 'Construction'),
        ('interior_2d', 'Interior 2D Drawing'),
        ('interior_3d', 'Interior 3D Drawing'),
    )
    booked_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    service_type = models.CharField(choices=SERVICE_TYPE, max_length=16)
    number_of_day = models.IntegerField()
    square_feet = models.CharField(max_length=128)
    work_progress = models.CharField(max_length=64)
    construction_plan = models.ImageField(upload_to='construction-plan')
    status = models.CharField(choices=STATUS, default='pending', max_length=16)

    def __str__(self):
        return f'{self.get_service_type_display()} booked by {str(self.booked_by)}'


class Tour(models.Model):
    TOUR_TYPE = (
        ('solo', 'Solo Tour'),
        ('family', 'Family Tour'),
        ('college', 'College Tour'),
        ('honeymoon', 'Honeymoon'),
    )
    TYPE_OF_HOTEL = (
        ('ac', 'AC'),
        ('non-ac', 'Non-AC'),
    )
    FOOD_TYPE = (
        ('veg', 'Vegetarian'),
        ('non-veg', 'Non-Vegetarian'),
    )
    YES_OR_NO = (
        ('y', 'Yes'),
        ('n', 'No'),
    )
    booked_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    tour_type = models.CharField(choices=TOUR_TYPE, max_length=16)
    date = models.DateField()
    number_of_days = models.IntegerField()
    type_of_hotel = models.CharField(choices=TYPE_OF_HOTEL, max_length=12)
    food_items = models.CharField(choices=FOOD_TYPE, max_length=12)
    number_of_person = models.IntegerField()
    number_of_room = models.IntegerField(default=1)
    transportation = models.IntegerField(blank=True, null=True)
    number_of_boys = models.IntegerField(blank=True, null=True)
    number_of_girls = models.IntegerField(blank=True, null=True)
    number_of_staff = models.IntegerField(blank=True, null=True)
    need_tour_guid = models.CharField(choices=YES_OR_NO, max_length=1)
    status = models.CharField(choices=STATUS, default='pending', max_length=16)

    def __str__(self):
        return f'{self.get_tour_type_display()} booked by {str(self.booked_by)}'
