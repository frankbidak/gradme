from django.shortcuts import render
from .forms import ContactForm  # Import the form

def home(request):
    tasks = [
        {'task': 'Learn Django', 'status': 'Completed'},
        {'task': 'Build a website', 'status': 'In Progress'},
        {'task': 'Deploy to the web', 'status': 'Not Started'}
    ]

    submitted_name = None
    submitted_email = None
    submitted_message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)  # Bind the form to POST data
        if form.is_valid():  # Validate the form
            submitted_name = form.cleaned_data['name']
            submitted_email = form.cleaned_data['email']
            submitted_message = form.cleaned_data['message']
    else:
        form = ContactForm()  # Empty form for a GET request

    context = {
        'greeting': 'Hello, welcome to my dynamic page!',
        'description': 'This page shows data passed from the Django view to the template.',
        'tasks': tasks,
        'form': form,  # Pass the form to the template
        'submitted_name': submitted_name,
        'submitted_email': submitted_email,
        'submitted_message': submitted_message
    }
    return render(request, 'home.html', context)
