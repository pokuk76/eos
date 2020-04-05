from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.functions import Concat
from django.db.models import CharField, Value

from .managers import CustomUserManager

"""
Extracted from <https://testdriven.io/blog/django-custom-user-model/>
"""


"""
CHANGE THE FOLLOWING SO THAT IT IS TIED INTO THE DEPARTMENT MODEL
"""
DEPARTMENTS = [
        ('IS', 'Information Systems'),
        ('HR', 'Human Resources'),
        ('EHS', 'Environment, Health, and Safety'),
        ('F', 'Facilities'),
        ('SC', 'Supply Chain'),
        ('T', 'Telecommunications'),
        ('ENG', 'Engineering')
    ]

def get_department():
    return Department.objects.get(id=1)

DEFAULT_DEPARTMENT_ID = 1
"""
class FullNameField(models.Field):

    def __init__(self, first_name, last_name, *args, **kwargs):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.exp_field = kwargs.pop('exp_field', None)
        kwargs['max_length'] = 104
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def get_full_name(self):
        return self.first_name + " " + self.last_name
"""

class Department(models.Model):
    """
    This is the Department model, which represents one department added to the database i.e.
    every department is an instance of our Department model
    """

    dept_name = models.CharField(max_length=200)

    def __str__(self):
        return self.dept_name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    This is our user model which inherits from Django's built-in AbstractBaseUser model
    """
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_active = models.BooleanField(_('active'),default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    full_name = models.CharField(_('full name'), max_length=41, default="Full Name")
    #full_name = FullNameField(first_name=first_name, last_name=last_name, max_length=41).get_full_name()
    #full_name = Concat('first_name', Value(' '), 'last_name', output_field=CharField())

    dept = models.ForeignKey(Department, default=DEFAULT_DEPARTMENT_ID, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


def user_directory_path(instance, filename):
    """
    This function creates the name of the directory that a video object with a file upload
    will be saved to.
    TODO: Make this more robust i.e. deal with department names that have things like "and",
    commas, etc
    """

    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dept_token_list = instance.dept.dept_name.split(' ')
    dept = ''
    for word in dept_token_list:
        dept += word[0].lower()
    return '{0}/{1}'.format(dept,filename)

class Video(models.Model):
    """
    This is the Video model, which represents one video added to the database i.e. every
    video is an instance of our Video model
    """

    """
    TODO: Change Video to have a many-to-many relationship with Department so that one video
    can belong to multiple departments
    """
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=200)
    video_url = models.URLField(max_length=200, blank=True)
    video_upload = models.FileField(upload_to=user_directory_path, blank=True)
    description = "Here is a nice description that someone did not have time to type up"
    video_description = models.TextField(blank=True, default = description)

    def __str__(self):
        return self.video_name

class Resource(models.Model):
    """
    to be added in later versions
    """
    pass
