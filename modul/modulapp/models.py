from django.db import models


class OtherModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}. {self.name}'


class MyModel(models.Model):
    name = models.CharField(max_length=255)
    my_list_field = models.ManyToManyField('OtherModel' )

    def __str__(self):
        return f'{self.id}. {self.name}'

