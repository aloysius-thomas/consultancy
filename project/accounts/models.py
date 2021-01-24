from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN_TYPE = (
        ('hr_admin', 'HR Admin'),
        ('event_admin', 'Event Admin'),
        ('construction_admin', 'Construction Admin'),
        ('tour_admin', 'Tour Admin'),
    )
    admin_type = models.CharField(choices=ADMIN_TYPE, blank=True, null=True, max_length=64)

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.username
