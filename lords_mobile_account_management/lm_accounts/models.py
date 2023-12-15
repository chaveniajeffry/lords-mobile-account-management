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

class LMUserBag(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(LMUserAccount, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_bag"

class LMUserBagChest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()
    bag_id = models.ForeignKey(LMUserBag, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_bag_chest"

class LMUserBagUnique(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()
    bag_id = models.ForeignKey(LMUserBag, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_bag_unique"

class LMUserBagSpeedUp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()
    bag_id = models.ForeignKey(LMUserBag, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_bag_speedup"

class LMUserBagCombat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()
    bag_id = models.ForeignKey(LMUserBag, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_bag_combat"

class LMUserBagResources(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    count = models.IntegerField()
    bag_id = models.ForeignKey(LMUserBag, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_bag_resources"

class LMUserResearch(models.Model):
    id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(LMUserAccount, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research"

class LMUserResearchEconomy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_economy"

class LMUserResearchDefense(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_defense"

class LMUserResearchMilitary(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_military"

class LMUserResearchMonsterHunt(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_monster_hunt"

class LMUserResearchUpgradeDefenses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_upgrade_defenses"

class LMUserResearchUpgradeMilitary(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_upgrade_military"

class LMUserResearchArmyLeadership(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_army_leadership"

class LMUserResearchMilitaryCommand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_military_command"

class LMUserResearchFamiliar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_familiar"

class LMUserResearchFamiliarBattles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_familiar_battles"

class LMUserResearchSigil(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_sigil"

class LMUserResearchWonderBattles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_wonder_battles"

class LMUserResearchGear(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_gear"

class LMUserResearchAdvancedWonderBattles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    research = models.ForeignKey(LMUserResearch, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "lm_user_research_advanced_wonder_battles"

