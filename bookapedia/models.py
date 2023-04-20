from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    def __str__(self):
        return str(self.email)

    class Meta(AbstractUser.Meta):
        ordering = ["-date_joined"]
        db_table = "users"

print("test")

class Book(models.Model):
    title = models.CharField(max_length=500, null=False)
    author = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000, null=True)
    date_published = models.DateField(null=True)
    marked_read = models.BooleanField(null=True)
    image_link = models.URLField()
    saved_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title