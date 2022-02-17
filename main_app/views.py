from django.shortcuts import render

class Plant:
    def __init__(self, name, description, sunlight, water, issues):
        self.name = name
        self.description = description
        self.sunlight = sunlight
        self.water = water
        self.issues = issues

plants = [
    Plant('Monstera Deliciosa', 
    'Famous for their natural leaf-holes, this popular plant is fondly nicknamed the Swiss Cheese Plant.',
    'Bright to medium indirect light',
    'Every 1-2 weeks, depending on light level',
    'Fungus flies, root rot, underwatering')
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', { 'plants': plants })