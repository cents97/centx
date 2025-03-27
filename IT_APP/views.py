from django.shortcuts import render
from .models import Product,  ContactMessage, Service, TeamMember, YouTubeVideo, FAQ
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, Project, Category
from .forms import ProductRequestForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

from django.shortcuts import render
from .models import Product, Project, Testimonial

def index(request):
    
    featured_projects = Project.objects.filter(status='completed')[:6]  # Get only 6 completed projects
    testimonials = Testimonial.objects.all().order_by('-created_at')[:3]  # Get the most recent 3 testimonials
    categories = Category.objects.all() 

    return render(request, 'index.html', {
        'featured_projects': featured_projects,
        'categories': categories,
        
        'testimonials': testimonials  # Pass testimonials to the template
    })


def about(request):
    # Fetch team members and testimonials from the database
    team_members = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()
    categories = Category.objects.all() 

    return render(request, 'about.html', {
        'team_members': team_members,
        'testimonials': testimonials,
        'categories': categories
    })

def service(request):
    services = Service.objects.all()
    categories = Category.objects.all()
    return render(request, 'service.html', {'services': services, 'categories': categories})

def team(request):
    team_members = TeamMember.objects.all()
    categories = Category.objects.all()
    return render(request, 'team.html', {'team_members': team_members, 'categories': categories})

def contact(request):
    categories = Category.objects.all()
    return render(request, 'contact.html', {'categories': categories})

def project(request):
    all_projects = Project.objects.filter(status='completed')
    categories = Category.objects.all()
    return render(request, 'project.html', {'all_projects': all_projects, 'categories': categories})



def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()  # Get all categories
    return render(request, 'product.html', {'products': products, 'categories': categories})

def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()  # Get all categories
    return render(request, 'category_products.html', {'category': category, 'products': products, 'categories': categories})

def request_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()  # Get all categories

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

    return render(request, 'request_product.html', {'product': product, 'form': form, 'categories': categories})



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




def video_list(request):
    videos = YouTubeVideo.objects.all()

    # Process video URLs to extract the video ID
    for video in videos:
        video.video_id = video.video_url.split('v=')[1].split('&')[0]  # Get the video ID
    return render(request, 'video.html', {'videos': videos})

def faq_page(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})




# def home(request):
#     return render(request, 'home.html')

# def home(request):
#     return render(request, 'home.html')  

