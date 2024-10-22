from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm
from django.core.paginator import Paginator


# Create your views here.

# def home(request):
#    return HttpResponse("Hello world!")


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

#For simple data
# def vehicle_list(request):
#     vehicles = Vehicle.objects.all()
#     return render(request, "vehicle_list.html", {"vehicles": vehicles})

#For huge data
def vehicle_list(request):
    vehicle_queryset = Vehicle.objects.all()
    
    # Set up pagination, 1000 items per page
    paginator = Paginator(vehicle_queryset, 1000)
    
    # Get the current page number from the request
    page_number = request.GET.get('page', 1)
    
    # Get the corresponding page of vehicles
    vehicles_page = paginator.get_page(page_number)
    
    return render(request, "vehicle_list.html", {"vehicles": vehicles_page})

def create_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vehicle_list")
    else:
        form = VehicleForm()
    return render(request, "create_vehicle.html", {"form": form})


def update_vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect("vehicle_list")
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, "update_vehicle.html", {"form": form})


def delete_vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == "POST":
        vehicle.delete()
        return redirect("vehicle_list")
    return render(request, "delete_vehicle.html", {"vehicle": vehicle})
