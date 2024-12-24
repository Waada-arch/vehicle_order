from django.shortcuts import redirect, render
from django.http import HttpResponse
from v_order.models import login,driver,Contact
from django.contrib import messages

# Simulated database of users
users = []  # Global variable to store user data for testing purposes



# Create your views here.
def index(request):
    return render(request, 'index.html')

# View to handle form submission
def handle_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        message = request.POST.get('message')
        gender = request.POST.get('gender')
        login_entry = login(name=name, email=email, age=age, message=message, gender=gender)
        login_entry.save()

        # Redirect to a success page or the index page
        return redirect('detail') 
    return render(request, 'login.html')

def login_or_register(request):
   if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        aadhaar = request.POST.get('aadhaar')
        license_number = request.POST.get('license')
        password = request.POST.get('password')
        vehicle = request.POST.get('vehicle')
        availability = request.POST.get('availability')

        # Save the data to the database
        det = driver(
            name=name,
            phone=phone,
            email=email,
            address=address,
            aadhaar=aadhaar,
            license=license_number,
            password=password,
            vehicle=vehicle,
            availability=availability,
        )
        det.save()
        return redirect('dlog') 
       

   return render(request, 'lar.html')

def dlog(request):
    return render(request, 'dlog.html')
   
def detail(request):
    data =driver.objects.all()
    return render(request, 'detail.html', {'data':data})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the data
        contact_entry = Contact(name=name, email=email, subject=subject, message=message)
        contact_entry.save()

        # Show success message
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return render(request, 'contact.html')

    return render(request, 'contact.html')

def info(request):
    # Pass any additional context if needed
    return render(request, 'info.html')