from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=150, unique=True)
    parent = models.ForeignKey('self', models.CASCADE, 'children', null=True, blank=True)
    objects: models.Manager

    def __str__(self):
        return self.title
