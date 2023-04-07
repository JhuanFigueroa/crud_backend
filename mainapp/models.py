from django.db import models

# Create your models here.

class User(models.Model):
    """Model definition for User."""
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=16)     
    file = models.FileField(null=True)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

   