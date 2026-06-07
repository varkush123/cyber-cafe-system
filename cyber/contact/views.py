'''from django.shortcuts import render, redirect
from django.contrib import messages

def contaction(request):
    if request.method == 'POST':
        # Process your form submission here
        # If the message is successfully sent, you can call show_message
        show_message(request)
        return redirect('contaction')  # Redirect back to the contact page
    else:
        return render(request, 'contact.html')

def show_message(request):
    messages.success(request, 'Your message has been sent successfully!')'''
from django.shortcuts import render
from django.contrib import messages

def show_message(request):
    #messages.success(request, 'Your message has been sent successfully!')
    return render(request, 'contact.html', {'show_message_script': True})