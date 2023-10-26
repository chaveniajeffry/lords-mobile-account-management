from django.db import models


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

class LMUserBagUnique(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = "lm_user_bag_unique"

class LMUserBagResources(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = "lm_user_bag_resources"

class LMUserBagSpeedUp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = "lm_user_bag_speedup"

class LMUserBagCombat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = "lm_user_bag_combat"

class LMUserBagChest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = "lm_user_bag_chest"

class LMUserBag(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(LMUserAccount, on_delete=models.CASCADE)
    unique_id = models.ForeignKey(LMUserBagUnique, on_delete=models.CASCADE)
    resources_id = models.ForeignKey(LMUserBagResources, on_delete=models.CASCADE)
    speedup_id = models.ForeignKey(LMUserBagSpeedUp, on_delete=models.CASCADE)
    combat_id = models.ForeignKey(LMUserBagCombat, on_delete=models.CASCADE)
    chest_id = models.ForeignKey(LMUserBagChest, on_delete=models.CASCADE)

    class Meta:
        db_table = "lm_user_bag"