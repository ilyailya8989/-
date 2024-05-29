from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=255)
    my_list_field = models.ManyToManyField('OtherModel' )

class OtherModel(models.Model):
    name = models.CharField(max_length=255)


