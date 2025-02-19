from django.db import models

class Project(models.Model):
    name = models.TextField()
    description = models.TextField()
    date = models.TextField()
    img = models.ImageField()
    github = models.TextField(blank=True,null=True)
    website = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.TextField()
    category = models.TextField()
    years = models.IntegerField()
    
    def __str__(self):
        return self.name