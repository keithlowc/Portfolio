from django.db import models

'''
Model created for the portfolio projects
using url's since Heroku does not manage 
static files.
'''

class Projects(models.Model):
    title = models.CharField(max_length=50, blank=False,null=False)
    description = models.TextField(max_length=450, blank=False, null=False)
    image_url = models.CharField(max_length=150, blank=False, null=False)
    project_url = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f'{self.title}'

class Contacts(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=150, blank=False, null=False)
    contact_message = models.TextField(max_length=450, blank=False, null=False)

    class Meta:
        verbose_name = "Contacts"
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return f'{self.subject} - from {self.full_name}'

