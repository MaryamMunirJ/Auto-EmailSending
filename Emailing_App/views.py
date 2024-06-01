from django.shortcuts import render
from django.core.mail import EmailMessage
from form_submission import Form_Submission
from django.http import HttpResponse

# Create your views here.
def Sending_Email(request):
    Form_Submission()
    
    email = EmailMessage(
        'Python (Selenium) Assignment - Maryam Munir',
        'Please find the attached screenshot of the form submission.',
        'maryammunir677@gmail.com',
        ['tech@themedius.ai'],
        cc=['HR@themedius.ai']
    )
    email.attach_file('form_screenshot.png')
    email.send()
    
    return HttpResponse('Email Sent')