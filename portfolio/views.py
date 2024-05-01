from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project
# Define the home view with login required

# def home(request):
#     username = request.user.username
#     return render(request, 'home.html', {'username': username})


def home(request):
    username = request.user.username
    
    # Retrieve all projects from the database
    projects = Project.objects.all()
    
    return render(request, 'home.html', {'username': username, 'projects': projects})

# Other views remain the same
def about(request):
    return render(request, 'about.html')

# def project_details(request):
#     return render(request, 'project_details.html')

def project_details(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'project_details.html', {'project': project})


def contact(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'contact.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to the home page after successful login
            return redirect('home')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    # Redirect to the home page after logout
    return redirect('home')




from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import ContactSubmission

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save form data to the ContactSubmission model
        contact_submission = ContactSubmission.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # Send email notification
        send_mail(
            'New Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,  # Sender's email address
            ['your_email@example.com'],  # Replace with your email address
            fail_silently=False,
        )

        return HttpResponse('Thank you for your message!')
    else:
        return HttpResponse('Method not allowed')


# portfolio/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feedback

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save form data to the Feedback model
        feedback = Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # Process the form data (e.g., send email, etc.)
        # You can add your code here to handle form submission
        
        return HttpResponse('Thank you for your feedback!')
    else:
        return HttpResponse('Method not allowed')
