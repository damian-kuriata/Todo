from django.db import models

class TestModel(models.Model):
    test = models.CharField(max_length=10)