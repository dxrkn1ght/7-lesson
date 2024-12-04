from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.title
