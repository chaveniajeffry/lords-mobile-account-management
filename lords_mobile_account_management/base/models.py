from django.db import models

class LMAccount(models.Model):
    id = models.AutoField(primary_key=True)
    IGN = models.CharField(max_length=20)
    reset_time = models.IntegerField()
    email = models.EmailField(max_length=255)

    class Meta:
        db_table = "lm_account"