from django.shortcuts import render
from .models import Product,  ContactMessage, Service, TeamMember
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, Project
from .forms import ProductRequestForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

from django.shortcuts import render
from .models import Product, Project, Testimonial

def index(request):
    
    featured_projects = Project.objects.filter(status='completed')[:6]  # Get only 6 completed projects
    testimonials = Testimonial.objects.all().order_by('-created_at')[:3]  # Get the most recent 3 testimonials

    return render(request, 'index.html', {
        'featured_projects': featured_projects,
        
        'testimonials': testimonials  # Pass testimonials to the template
    })


def about(request):
    # Fetch team members and testimonials from the database
    team_members = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()

    return render(request, 'about.html', {
        'team_members': team_members,
        'testimonials': testimonials,
    })

def service(request):
    services = Service.objects.all()
    return render(request, 'service.html', {'services': services})

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team.html', {'team_members': team_members})

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

