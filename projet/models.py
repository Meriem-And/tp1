from django.db import models


class Projet(models.Model):
    titre = models.CharField(max_length=50)
    descriotion = models.TextField(max_length=1000)
    image_url = models.CharField(max_length=2000)
