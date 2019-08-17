from django.db import models
from django.contrib.postgres.fields import ArrayField

'''
Model created for the portfolio projects
using url's since Heroku does not manage 
static files.
'''
class Projects(models.Model):
    title = models.CharField(max_length=50, blank=False,null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    image_url = models.CharField(max_length=150, blank=False, null=False)
    project_url = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f'{self.title}'


'''
Model created to manage the contact information of people
when they send me a message.
'''
class Contacts(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=150, blank=False, null=False)
    message = models.TextField(max_length=450, blank=False, null=False)

    class Meta:
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return f'{self.subject} - from {self.full_name}'


'''
Model created to capture analytics from social media clicks
and portfolios. Will later use these data to plot it on graphs.
'''
class Analytics(models.Model):
    TYPES_OF_ANALYTICS = (
        ('G', 'GitHub'),
        ('L', 'LinkedIn'),
        ('I', 'Instagram'),
    )
    type_of_analytics = models.CharField(max_length=50, choices=TYPES_OF_ANALYTICS)
    date_clicked = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Analytic'
        verbose_name_plural = 'Analytics'
    
    def __str__(self):
        return f'{self.type_of_analytics} - @ {self.date_clicked.strftime("%b %d %Y %H:%M:%S")}'

'''
Model controls the about page data
'''
class PageData(models.Model):
    profile_url = models.CharField(max_length=150, blank=False, null=False)
    about = models.TextField(max_length=1000, blank=False,null=False)

    class Meta:
        verbose_name = 'Page Data'
        verbose_name_plural = 'Page Data'

    def __str__(self):
        return 'Website Main Data'
