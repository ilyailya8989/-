from django.shortcuts import render

from .models import MyModel


def my_view(request):
    for i in range(5):
        MyModel.objects.create(name=f'Пример {i}')
        my_model_objs = MyModel.objects.all()


    for obj in my_model_objs:
        obj.name = f'{obj.name} ({obj.id})'
        obj.save()
        my_model_objs = MyModel.objects.all()

    for obj in my_model_objs:
        name_parts = obj.name.split('(')
        model = name_parts[-1]
        model = model.strip(')')
        my_model = int(model)
        if my_model % 2 != 0:
            obj.delete()

    ctx = {
        'my_model_objs': MyModel.objects.all()
    }

    return render(request, 'modulapp/index.html', context=ctx)

