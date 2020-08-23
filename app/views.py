from django.shortcuts import render
from .models import Registry
from django.views.generic.edit import CreateView

def index(request):
   
    num_records=Registry.objects.all().count()

    all_records=Registry.objects.all()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_records': num_records,
                 'all_records': all_records,
        }
    )

class RegistryCreate(CreateView):
    model = Registry
    fields = '__all__'