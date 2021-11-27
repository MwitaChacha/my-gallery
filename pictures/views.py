from django.shortcuts import render

# Create your views here.
def index(request):
       
    return render(request, 'index.html')

def display(request):
    images = Image.objects.all()
    location = Location.objects.all()
    return render(request, 'display.html',{"images":images, "location":location})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"images":searched_images})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})