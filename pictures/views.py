from django.shortcuts import render

# Create your views here.
def index(request):
       
    return render(request, 'index.html')

def display(request):
    images = Image.objects.all()
    location = Location.objects.all()
    return render(request, 'display.html',{"images":images, "location":location})