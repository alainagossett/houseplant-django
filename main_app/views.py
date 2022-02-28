from django.shortcuts import redirect, render
from .models import Plant, Watering, Accessory
from .forms import WateringForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants': plants })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()

    accessories_plant_doesnt_have = Accessory.objects.exclude(id__in = plant.accessories.all().values_list('id'))

    return render(request, 'plants/detail.html', {
        'plant': plant,
        'watering_form': watering_form,
        'accessories': accessories_plant_doesnt_have
        })

def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

def assoc_accessory(request, plant_id, accessory_id):
    Plant.objects.get(id=plant_id).accessories.add(accessory_id)
    return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ('description', 'issues', 'water')

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

class AccessoryList(ListView):
    model = Accessory
    template_name = 'accessories/index.html'

class AccessoryDetail(DetailView):
    model = Accessory
    template_name = 'accessories/detail.html'

class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'
    success_url = '/accessories/'

class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ('name', 'description')

class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'
