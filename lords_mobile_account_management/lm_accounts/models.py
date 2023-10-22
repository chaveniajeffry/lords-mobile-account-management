from django.db import models

# Create your models here.
class LMUserAccount(models.Model):
    CHOICES = (
        ('google', 'Google'),
        ('facebook', 'Facebook'),
    )
    id = models.AutoField(primary_key=True)
    IGN = models.CharField(max_length=20)
    reset_time = models.IntegerField()
    email = models.CharField(max_length=255)
    provider = models.CharField(
        max_length=10,  # Adjust the max length as needed
        choices=CHOICES,
        default='google'  # Default value is optional
    )

    class Meta:
        db_table = "LMUserAccount"