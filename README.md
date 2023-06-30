# Overview

MyDose is an app for cancer patients and their doctors to keep track of how much radiation they receive in their treatments. 

To use, clone the repository, and to get the right libraries run, 
```python
pip install -r requirements.txt
```
To start the app, open up a command prompt and go to the first "mysite" directory (it contains a file named 'manage.py'). Run the following code to start a test webserver:

```powershell
py manage.py runserver
```

Then, open a web browser and go to [localhost:8000/mydose](localhost:8000/mydose). This should show you the app's homepage. From there you can choose to log in as a doctor or a patient. 

To try out the functionality, use the username: 'admin' and the password: 'password'

I am writing this software because cancer patients often aren't aware of how much radiation they are receiving from their treatments, or how much is safe and healthy. This app (when it's done) will prove a reliable way to log how much radiation the patients are receiving, and what a safe amount is, educating patients and keeping doctors organized and accountable.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

The web pages currently in this project are:

mydose/
- The app's homepage.
- Creates links for user
- Links to mydose/login/patient
- Links to mydose/login/doctor
  
mydose/login/patient
- A login screen specifically for patient users
- Upon successful login, redirects to mydose/patient_portal
- Upon unsuccessful login, displays an error message and allows patient to try again
  
mydose/login/doctor
- A login screen specifically for doctor users
- Upon successful login, redirects to mydose/doctor_portal
- Upon unsuccessful login, displays an error message and allows doctor to try again
  
mydose/patient_portal
- Page designed for patient to see their lifetime of radiation and recent radiation
- Links back to home

mydose/doctor_portal
- Page designed for doctor to input a treatment for the patient
- Links back to home

# Development Environment

I developed this WebApp using VSCode. I used python and the Django library. 

# Useful Websites

* [Tutorial to set up a Django app](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
* [How to use Django's built in login pages](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
* [Multiple types of users](https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html)

# Future Work

* Clean up the models in the doctor_portal app
* Add functionality to create an account
* Add models to save the patient and doctor users in their own tables in the database
* Add functionality to both doctor and patient portals
* Add CSS to make the website prettier.
