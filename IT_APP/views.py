from django.shortcuts import render
from .models import Product, ProductRequest
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, Project
from .forms import ProductRequestForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage
import json

# Create your views here.

def index(request):
    products = Product.objects.all()[:6]  # Get only 6 products
    featured_projects = Project.objects.filter(status='completed')[:6]  # Get only 6 completed projects
    return render(request, 'index.html', {
        'featured_projects': featured_projects,
        'products': products
    })



 

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')

def project(request):
    all_projects = Project.objects.filter(status='completed')
    return render(request, 'project.html', {'all_projects': all_projects})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})



def request_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductRequestForm(request.POST)
        if form.is_valid():
            product_request = form.save(commit=False)
            product_request.product = product  # Link request to product
            product_request.save()
            messages.success(request, "Your request has been submitted successfully. We will contact you soon.")
            form = ProductRequestForm()  # Reset form after submission

    else:
        form = ProductRequestForm()

    return render(request, 'request_product.html', {'product': product, 'form': form})




@csrf_exempt
def save_contact_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        project = request.POST.get("project", "")
        message = request.POST.get("message")

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, project=project, message=message)
            return JsonResponse({"message": "Message sent successfully!"})
        else:
            return JsonResponse({"error": "Please fill in all required fields."}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)



# def home(request):
#     return render(request, 'home.html')

# def home(request):
#     return render(request, 'home.html')  

