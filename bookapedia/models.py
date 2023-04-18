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

# Started models for the saved book and the bookshelf
# The table SHOULD be a many-to-many table
# It is not at the moment so I can visualize it
# The table should have the ID of the user which is always the same
# And should reference the ID in the API of the book
# I think getting the ID from the API ID of the book
# would be more consistant because each book has a special ID
# This is because if the same book is saved between
# different users, I don't want the same book listed twice
# with different ID'set
# This way the table will grab the books API ID instead

class Book(models.Model):
    title = models.CharField(max_length=500, null=False)
    author = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000, null=True)
    # genre = models.CharField(max_length=300, null=True)
    date_published = models.DateField(null=True)
    marked_read = models.BooleanField(null=True)
    image_link = models.URLField()
    saved_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title