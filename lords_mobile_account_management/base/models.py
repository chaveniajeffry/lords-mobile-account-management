from django.db import models

class LMAccount(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    IGN = models.CharField(max_length=20)
    reset_time = models.IntegerField()
    email = models.EmailField(max_length=255)

    class Meta:
        db_table = "lm_account"

class Bag(models.Model):
    id = models.AutoField(primary_key=True)
    

    class Meta:
        db_table = "lm_account_bag"