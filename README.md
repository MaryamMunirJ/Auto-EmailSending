# Internship Assignment using Selenium and Django

## Project Overview
In this project, the Google Form submission process will be automated with Selenium. A screenshot of the form submission will be taken, and it will be sent as an email attachment using Django.

## Approach
-*Selenium* script was used to fill up and submit the Google Form. A screenshot of the form submission was then taken.

-*Django*: Set up a Django project to manage email attachment delivery of the screenshot.

## Setup Instructions
1. Clone the repository:
   bash
   git clone https://github.com/MaryamMunirJ/Auto-EmailSending.git
   cd Auto-EmailSending
2. Install dependecies and setup env varaiables:
    bash
    pip install -r requirements.txt
    export username=email_username@domain.com
    export password=password
3. Apply migrations and start the Django server:
    ```bash
    python manage.py migrate
    python manage.py runserver

## Sending Email
Visit "http://localhost:8000/EmailCompose/" to start the email sending proccess.
You can change the email info in Emailing_App/views