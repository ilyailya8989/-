from django.shortcuts import render

from .models import MyModel


def my_view(request):

    for i in range(5):
        MyModel.objects.create(name='Пример {}'.format(i))

        my_model_objs = MyModel.objects.all()


    for obj in my_model_objs:
        obj.name = '{} ({})'.format(obj.name, obj.id)
        obj.save()

    for obj in my_model_objs:
        if any(char.isdigit() and int(char) % 2 != 0 for char in obj.name):
            obj.delete()

    ctx = {
        'my_model_objs': my_model_objs
    }

    return render(request, 'modulapp/index.html', context=ctx)





