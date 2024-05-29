from django.contrib import admin

from modulapp.models import MyModel, OtherModel

# Register your models here.
admin.site.register(MyModel)
admin.site.register(OtherModel)