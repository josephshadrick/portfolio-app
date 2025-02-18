from django.db import models

class Project(models.Model):
    name = models.TextField()
    description = models.TextField()
    date = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.TextField()
    years = models.IntegerField()
    
    def __str__(self):
        return self.name