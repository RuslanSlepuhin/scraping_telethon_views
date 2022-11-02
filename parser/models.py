from django.db import models

# Create your models here.
class MexModel(models.Model):
    tag = models.CharField(max_length=70, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mex'


class CurrentSession(models.Model):
    session = models.CharField(unique=True, max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_session'

    def __str__(self):
        return self.session



class AdminLastSession(models.Model):
    chat_name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=6000, blank=True, null=True)
    profession = models.CharField(max_length=30, blank=True, null=True)
    vacancy = models.CharField(max_length=700, blank=True, null=True)
    vacancy_url = models.CharField(max_length=150, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    english = models.CharField(max_length=100, blank=True, null=True)
    relocation = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=700, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    salary = models.CharField(max_length=300, blank=True, null=True)
    experience = models.CharField(max_length=700, blank=True, null=True)
    contacts = models.CharField(max_length=500, blank=True, null=True)
    time_of_public = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    agregator_link = models.CharField(max_length=200, blank=True, null=True)
    session = models.ForeignKey('CurrentSession', models.DO_NOTHING, db_column='session', to_field='session', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_last_session'

class PatternModel(models.Model):
    key = models.CharField(max_length=100, blank=True, null=True)
    ma = models.BooleanField(blank=True, null=True)
    mex = models.BooleanField(blank=True, null=True)
    value = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pattern'


