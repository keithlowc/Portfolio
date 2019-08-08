from django.db import models

'''
Model created for the portfolio projects
using url's since Heroku does not manage 
static files.
'''

class Projects(models.Model):
    title = models.CharField(
        max_length=50, blank=False,null=False)
    description = models.TextField(
        max_length=450, blank=False, null=False)
    image_url = models.CharField(
        max_length=150, blank=False, null=False)
    project_url = models.CharField(
        max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(
        auto_now_add=True)
    
    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f'{self.title}'


