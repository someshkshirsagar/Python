from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TestString(models.Model):
    string = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return self.string

# Create your models here.
class Entry(models.Model):
    date_added=models.DateTimeField(default=timezone.now)
    pattern=models.CharField(max_length=200)
    test_string = models.ManyToManyField(TestString)
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
                           )
    class Meta:
        #make Entry appearance change to this appearence
        verbose_name_plural="entries"
    
class UserProfile(models.Model):
    nickname=models.CharField(max_length=225)
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

