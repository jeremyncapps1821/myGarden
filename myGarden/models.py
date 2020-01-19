from django.db import models

class MyGrow(models.Model):
    grow_title = models.CharField(max_length=200)
